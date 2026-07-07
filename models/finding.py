from dataclasses import dataclass


@dataclass
class Finding:
    service: str
    check: str
    resource: str
    status: str
    severity: str
    message: str
    recommendation: str
    region: str = "global"