import json
import os
from dataclasses import asdict


def write_json_report(findings, summary, output_path="reports/cloudsec-audit.json"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    report = {
        "summary": summary,
        "findings": [asdict(finding) for finding in findings],
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return output_path