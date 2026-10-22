# Changelog

All notable changes to the Create State Cursor plugin are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and the plugin uses [Semantic Versioning](https://semver.org/).

## [1.3.0] - 2026-10-14

### Added

- `readNode` guidance: load one record by the id a search printed.
- `updateNode` guidance: correct one saved record at the user's request.
  Correcting an Entity retracts the old record and reports the successor id.
- `searchImages` in the search tool table.

### Fixed

- `getProjectWorldModel` is addressed by `model_name`. A name passed as
  `model_id` was treated as a UUID and missed.

### Security

- General security hardening. Upgrading is recommended.

## [1.2.0] - 2026-06-05

### Added

- `captureImage` and `captureImageBatch` habits for screenshots, diagrams, and
  other visual assets.
- `capture_phase` documentation and the status mapping by phase.

## [1.1.0] - 2026-04-17

### Added

- Teams tier guidance: team management skill, team collaboration rule, and
  working capacity.

## [1.0.0] - 2026-03-11

- First public release: session workflow, knowledge capture, commit workflow,
  setup command, and the session start hook.
