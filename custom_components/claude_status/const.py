from __future__ import annotations

DOMAIN = "claude_status"
STATUS_API_URL = "https://status.claude.com/api/v2/summary.json"
INCIDENTS_API_URL = "https://status.claude.com/api/v2/incidents/all.json"
SCAN_INTERVAL_SECONDS = 300  # 5 minutes
UPTIME_DAYS = 60

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

INDICATOR_STATUS_MAP_FR = {
    "none": "Opérationnel",
    "minor": "Problèmes mineurs",
    "major": "Problèmes majeurs",
    "critical": "Critique",
}

COMPONENT_STATUS_MAP_FR = {
    "operational": "Opérationnel",
    "degraded_performance": "Performance dégradée",
    "partial_outage": "Panne partielle",
    "major_outage": "Panne majeure",
    "under_maintenance": "En maintenance",
}


def is_french(language: str | None) -> bool:
    """Return True if the Home Assistant language is French (fr, fr-CA, ...)."""
    return bool(language) and language.lower().startswith("fr")
