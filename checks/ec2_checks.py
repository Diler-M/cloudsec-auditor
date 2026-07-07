import boto3

from models.finding import Finding
from reporting.console import print_finding
from utils.aws import get_all_regions


def check_ec2_sg(summary):
    regions = get_all_regions()

    risky_ports = {
        22: "SSH",
        3389: "RDP",
    }

    found_risky_rule = False

    print("\nEC2 Security Group Audit:\n")

    for region in regions:
        region_name = region["RegionName"]

        regional_ec2 = boto3.client("ec2", region_name=region_name)

        security_groups = regional_ec2.describe_security_groups()

        for security_group in security_groups["SecurityGroups"]:
            security_group_name = security_group["GroupName"]
            security_group_id = security_group["GroupId"]

            for inbound_rule in security_group["IpPermissions"]:
                from_port = inbound_rule.get("FromPort")
                ip_ranges = inbound_rule.get("IpRanges", [])

                for ip_range in ip_ranges:
                    cidr = ip_range.get("CidrIp")

                    if cidr == "0.0.0.0/0" and from_port in risky_ports:
                        service = risky_ports[from_port]

                        finding = Finding(
                            service="EC2",
                            check="Security Group Exposure",
                            resource=f"{security_group_name} ({security_group_id})",
                            status="WARN",
                            severity="HIGH",
                            message=f"Allows {service} from 0.0.0.0/0",
                            recommendation="Restrict access to trusted IP ranges instead of 0.0.0.0/0.",
                            region=region_name,
                        )

                        print_finding(finding)
                        summary["WARN"] += 1
                        found_risky_rule = True

    if not found_risky_rule:
        finding = Finding(
            service="EC2",
            check="Security Group Exposure",
            resource="Security Groups",
            status="PASS",
            severity="INFO",
            message="No risky Security Group rules found",
            recommendation="No action required.",
        )

        print_finding(finding)
        summary["PASS"] += 1