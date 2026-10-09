# Claude Status — Intégration Home Assistant

[English](README.md) · **Français**

Surveillez la disponibilité de Claude AI directement dans Home Assistant grâce à la page d'état officielle [status.claude.com](https://status.claude.com).

## Fonctionnalités

- **Capteur binaire** — `ON` quand tous les services Claude sont opérationnels, `OFF` dès qu'un problème est détecté
- **Capteur d'état général** — Opérationnel, Problèmes mineurs, Problèmes majeurs, Critique
- **Capteur d'incidents actifs** — nombre d'incidents en cours, détails dans les attributs
- **Capteurs par composant** — un capteur par service (Claude.ai, API Claude, etc.), mis à jour automatiquement
- **Disponibilité sur 60 jours** — globale et par composant
- Interrogation aux **5 minutes** via l'API JSON Statuspage
- Toutes les entités sont regroupées sous un seul appareil **Claude AI**
- Interface disponible en **français** et en anglais (selon la langue de Home Assistant)

> Les noms des composants (ex. « Claude API ») proviennent de la page d'état et ne sont pas traduits.

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

## Changement de la version 1.1.0

Les états des capteurs sont maintenant des valeurs internes traduites par l'interface
(`operational`, `minor`, `major`, `critical`, `degraded_performance`, etc.) au lieu de textes anglais.
Si vous avez des automatisations qui comparent l'état à `"Operational"` ou `"Major Issues"`,
mettez-les à jour avec ces nouvelles valeurs (ou utilisez le capteur binaire).

## Vie privée

L'intégration n'envoie aucune donnée personnelle : elle fait uniquement des requêtes GET anonymes vers `status.claude.com`. Aucun identifiant, aucun compte, aucune télémétrie.

## Prérequis

- Home Assistant 2024.4.0 ou plus récent
- Accès Internet à `status.claude.com`
