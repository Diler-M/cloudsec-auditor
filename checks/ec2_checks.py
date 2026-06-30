import boto3


def check_ec2_sg(summary):
    ec2 = boto3.client("ec2")

    security_groups = ec2.describe_security_groups()

    risky_ports = {
        22: "SSH",
        3389: "RDP",
    }

    found_risky_rule = False

    print("\nEC2 Security Group Audit:\n")

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
                    print(
                        f"WARN: {security_group_name} ({security_group_id}) "
                        f"allows {service} from 0.0.0.0/0"
                    )
                    summary["WARN"] += 1
                    found_risky_rule = True

    if not found_risky_rule:
        print("PASS: No risky Security Group rules found")
        summary["PASS"] += 1