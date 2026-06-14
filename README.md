# Claude Status — Home Assistant Integration

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

## Minimum Requirements

- Home Assistant 2023.3.0 or newer
- Internet access to reach `status.claude.com`

---

## Also in this repository: COBA / ColNET integration

A second, independent integration (`custom_components/coba`) connects to the
**COBA / ColNET** student portal (cégeps/collèges, Québec) using your **URL**,
**username** and **password**, and exposes: messages received, last message,
last grade, the next 5 courses, and the last follow-up.

See [`custom_components/coba/README.md`](custom_components/coba/README.md) for
details. Note: because HACS manages only one integration per repository, COBA is
best installed manually or moved to its own repository.
