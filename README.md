# Claude Status — Home Assistant Integration

**English** · [Français](README.fr.md)

Monitor Claude AI uptime directly in Home Assistant using the official [status.claude.com](https://status.claude.com) page.

## Features

- **Binary sensor** — `ON` when all Claude services are operational, `OFF` when any issue is detected
- **Overall status sensor** — human-readable status: Operational, Minor Issues, Major Issues, Critical
- **Active incidents sensor** — count of ongoing incidents with details in attributes
- **Per-component sensors** — one sensor per service component (Claude.ai, Claude API, etc.) updated automatically from the status page
- Polls every **5 minutes** via the Statuspage JSON API
- All entities grouped under a single **Claude AI** device

## Installation via HACS

1. Open HACS in Home Assistant
2. Go to **Integrations** → three-dot menu → **Custom repositories**
3. Add `https://github.com/Maringouin10/claudeuptime` as category **Integration**
4. Click **Download** on the Claude Status card
5. Restart Home Assistant
6. Go to **Settings → Devices & Services → Add Integration** and search for **Claude Status**

## Manual Installation

Copy the `custom_components/claude_status` folder into your Home Assistant `custom_components` directory, then restart Home Assistant.

## Entities Created

| Entity | Type | Description |
|--------|------|-------------|
| `binary_sensor.claude_ai_operational` | Binary sensor | `ON` = all systems operational |
| `sensor.claude_ai_overall_status` | Sensor | Overall status text |
| `sensor.claude_ai_active_incidents` | Sensor | Number of active incidents |
| `sensor.claude_ai_<component>` | Sensor | Status of each service component |

## Breaking change in 1.1.0

Sensor states are now translatable keys (`operational`, `minor`, `major`, `critical`, `degraded_performance`, …) shown translated in the UI (English/French). Update automations that compared against `"Operational"` or `"Major Issues"`.

## Minimum Requirements

- Home Assistant 2024.4.0 or newer
- Internet access to reach `status.claude.com`
