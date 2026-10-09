from __future__ import annotations

DOMAIN = "claude_status"
STATUS_API_URL = "https://status.claude.com/api/v2/summary.json"
INCIDENTS_API_URL = "https://status.claude.com/api/v2/incidents/all.json"
SCAN_INTERVAL_SECONDS = 300  # 5 minutes
UPTIME_DAYS = 60

INDICATOR_STATUS_MAP = {
    "none": "operational",
    "minor": "minor_issues",
    "major": "major_issues",
    "critical": "critical",
}

COMPONENT_STATUS_MAP = {
    "operational": "operational",
    "degraded_performance": "degraded_performance",
    "partial_outage": "partial_outage",
    "major_outage": "major_outage",
    "under_maintenance": "under_maintenance",
}
