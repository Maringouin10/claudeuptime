# Claude Status — Intégration Home Assistant

🇬🇧 [English version](README.md)

Surveillez la disponibilité de Claude AI directement dans Home Assistant grâce à la page officielle [status.claude.com](https://status.claude.com).

## Fonctionnalités

- **Capteur binaire** — `ON` quand tous les services Claude sont opérationnels, `OFF` dès qu'un problème est détecté
- **Capteur d'état général** — état lisible : Opérationnel, Problèmes mineurs, Problèmes majeurs, Critique
- **Capteur d'incidents actifs** — nombre d'incidents en cours, avec les détails en attributs
- **Capteurs par composant** — un capteur par service (Claude.ai, API Claude, etc.), mis à jour automatiquement
- **Capteurs de disponibilité sur 60 jours**, global et par composant
- Interrogation toutes les **5 minutes** via l'API JSON de Statuspage
- Toutes les entités sont regroupées sous un seul appareil **Claude AI**

## Installation avec HACS

1. Ouvrez HACS dans Home Assistant
2. Allez dans **Intégrations** → menu à trois points → **Dépôts personnalisés**
3. Ajoutez `https://github.com/Maringouin10/claudeuptime` comme catégorie **Intégration**
4. Cliquez sur **Télécharger** sur la carte Claude Status
5. Redémarrez Home Assistant
6. Allez dans **Paramètres → Appareils et services → Ajouter une intégration** et cherchez **Claude Status**

## Installation manuelle

Copiez le dossier `custom_components/claude_status` dans le dossier `custom_components` de Home Assistant, puis redémarrez.

## Entités créées

| Entité | Type | Description |
|--------|------|-------------|
| `binary_sensor.claude_ai_operational` | Capteur binaire | `ON` = tous les systèmes sont opérationnels |
| `sensor.claude_ai_overall_status` | Capteur | État général (texte) |
| `sensor.claude_ai_active_incidents` | Capteur | Nombre d'incidents actifs |
| `sensor.claude_ai_<composant>` | Capteur | État de chaque composant |

Les noms et les états s'affichent en français lorsque Home Assistant est configuré en français.

## Prérequis

- Home Assistant 2023.3.0 ou plus récent
- Accès Internet à `status.claude.com`

## Confidentialité

Cette intégration ne collecte, ne conserve et ne transmet aucun renseignement personnel. Elle lit uniquement l'API publique Statuspage de `status.claude.com` ; aucun compte, identifiant ou donnée d'utilisateur n'est utilisé. Elle est donc conforme à la Loi 25 du Québec (*Loi sur la protection des renseignements personnels dans le secteur privé*).
