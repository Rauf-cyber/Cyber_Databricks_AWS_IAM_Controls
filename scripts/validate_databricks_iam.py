#!/usr/bin/env python3
"""
Databricks AWS IAM Policy Validator

Reviews sample IAM policy JSON files for risky patterns that commonly show up
in Databricks-on-AWS integrations.
"""

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

HIGH_RISK_ACTION_PREFIXES = (
    "iam:*",
    "kms:*",
    "s3:*",
    "ec2:*",
    "organizations:*",
    "cloudtrail:StopLogging",
    "cloudtrail:DeleteTrail",
    "guardduty:DeleteDetector",
    "config:DeleteConfigurationRecorder",
)


def as_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def add_finding(findings: List[Dict[str, Any]], file_name: str, severity: str, issue: str, details: Dict[str, Any]) -> None:
    findings.append(
        {
            "file": file_name,
            "severity": severity,
            "issue": issue,
            "details": details,
        }
    )


def evaluate_policy(path: Path) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []
    document = json.loads(path.read_text(encoding="utf-8"))

    for statement in as_list(document.get("Statement")):
        sid = statement.get("Sid", "NoSid")
        effect = statement.get("Effect", "")
        actions = as_list(statement.get("Action"))
        resources = as_list(statement.get("Resource"))
        principal = statement.get("Principal")
        condition = statement.get("Condition", {})

        if effect == "Allow" and "*" in actions:
            add_finding(findings, path.name, "high", "Wildcard action allowed", {"sid": sid})

        if effect == "Allow" and "*" in resources:
            add_finding(findings, path.name, "medium", "Wildcard resource allowed", {"sid": sid, "actions": actions})

        if effect == "Allow":
            for action in actions:
                for risky in HIGH_RISK_ACTION_PREFIXES:
                    if action.lower() == risky.lower():
                        add_finding(findings, path.name, "high", "High-risk action allowed", {"sid": sid, "action": action})

        if "trust" in path.name.lower():
            if principal == "*" or principal == {"AWS": "*"}:
                add_finding(findings, path.name, "critical", "Trust policy allows any principal", {"sid": sid})
            if "sts:AssumeRole" in actions and "sts:ExternalId" not in json.dumps(condition):
                add_finding(findings, path.name, "high", "Trust policy missing external ID condition", {"sid": sid})

    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Databricks AWS IAM policy samples.")
    parser.add_argument("--policy-dir", default="iam-policies", help="Directory containing IAM policy JSON files.")
    args = parser.parse_args()

    policy_dir = Path(args.policy_dir)
    all_findings: List[Dict[str, Any]] = []

    for policy_file in sorted(policy_dir.glob("*.json")):
        try:
            all_findings.extend(evaluate_policy(policy_file))
        except json.JSONDecodeError as error:
            add_finding(all_findings, policy_file.name, "critical", "Invalid JSON policy file", {"error": str(error)})

    report = {
        "policy_directory": str(policy_dir),
        "total_findings": len(all_findings),
        "findings": all_findings,
    }

    print(json.dumps(report, indent=2))

    high_or_critical = [item for item in all_findings if item["severity"] in {"high", "critical"}]
    if high_or_critical:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
