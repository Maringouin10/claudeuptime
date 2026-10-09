from __future__ import annotations

DOMAIN = "claude_status"
STATUS_API_URL = "https://status.claude.com/api/v2/summary.json"
INCIDENTS_API_URL = "https://status.claude.com/api/v2/incidents/all.json"
SCAN_INTERVAL_SECONDS = 300  # 5 minutes
UPTIME_DAYS = 60

INDICATOR_STATUS_MAP = {
    "none": "operational",
    "minor": "minor",
    "major": "major",
    "critical": "critical",
}
INDICATOR_OPTIONS = ["operational", "minor", "major", "critical", "unknown"]

COMPONENT_OPTIONS = [
    "operational",
    "degraded_performance",
    "partial_outage",
    "major_outage",
    "under_maintenance",
    "unknown",
]
