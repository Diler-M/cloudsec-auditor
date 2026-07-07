def print_finding(finding):
    print(f"{finding.status}: {finding.region} - {finding.resource} - {finding.message}")
    print(f"Recommendation: {finding.recommendation}\n")