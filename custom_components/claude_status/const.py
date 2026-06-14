from __future__ import annotations

DOMAIN = "claude_status"
STATUS_API_URL = "https://status.claude.com/api/v2/summary.json"
SCAN_INTERVAL_SECONDS = 300  # 5 minutes

INDICATOR_STATUS_MAP = {
    "none": "Operational",
    "minor": "Minor Issues",
    "major": "Major Issues",
    "critical": "Critical",
}

COMPONENT_STATUS_MAP = {
    "operational": "Operational",
    "degraded_performance": "Degraded Performance",
    "partial_outage": "Partial Outage",
    "major_outage": "Major Outage",
    "under_maintenance": "Under Maintenance",
}
