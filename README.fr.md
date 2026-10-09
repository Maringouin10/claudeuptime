# Claude Status — Intégration Home Assistant

Surveillez la disponibilité de Claude AI directement dans Home Assistant grâce à la page d'état officielle [status.claude.com](https://status.claude.com).

*English version: [README.md](README.md)*

## Fonctionnalités

- **Capteur binaire** — `ON` quand tous les services Claude sont opérationnels, `OFF` dès qu'un problème est détecté
- **Capteur d'état général** — Opérationnel, Problèmes mineurs, Problèmes majeurs, Critique
- **Capteur d'incidents actifs** — nombre d'incidents en cours, avec le détail en attributs
- **Capteurs par composant** — un capteur par service (Claude.ai, API Claude, etc.)
- **Disponibilité sur 60 jours** — globale et par composant
- Interrogation toutes les **5 minutes** via l'API JSON Statuspage
- Interface disponible en **français** et en anglais
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
| `sensor.claude_ai_overall_status` | Capteur | État général |
| `sensor.claude_ai_active_incidents` | Capteur | Nombre d'incidents actifs |
| `sensor.claude_ai_<composant>` | Capteur | État de chaque composant |

Les identifiants d'entités sont générés à partir des noms; ils peuvent varier selon la langue de Home Assistant.

## Changement de version 1.1.0

Les valeurs d'état des capteurs sont maintenant des clés stables traduites par l'interface (`operational`, `minor_issues`, `major_issues`, `critical`, `degraded_performance`, `partial_outage`, `major_outage`, `under_maintenance`). Mettez à jour vos automatisations qui comparaient l'ancien texte anglais (p. ex. « Operational »).

## Confidentialité (Loi 25)

Cette intégration ne recueille, ne conserve et ne transmet aucun renseignement personnel. Elle n'exige aucun identifiant. Elle envoie uniquement des requêtes HTTPS publiques et anonymes à `status.claude.com`; comme pour tout accès Internet, ce serveur peut voir l'adresse IP de votre installation Home Assistant. Aucune donnée n'est envoyée à l'auteur de l'intégration.

## Exigences minimales

- Home Assistant 2023.3.0 ou plus récent
- Accès Internet à `status.claude.com`
