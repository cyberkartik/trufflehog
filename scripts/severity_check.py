import json
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    findings = json.load(f)

for finding in findings:
    severity = finding.get("severity", "").lower()
    if severity in ["high", "critical"]:
        print(f"❌ High/Critical issue found: {severity}")
        sys.exit(1)

print("✅ No high or critical severity issues found.")
