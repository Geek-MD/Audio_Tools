# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-03-16

### Added
- Initial release of the Audio Tools integration for Home Assistant.
- Config flow to set up the integration via the UI, with an optional **Work Directory** field.
- Support for audio format conversion using `ffmpeg` as the backend engine.
- Supported output formats: `mp3`, `flac`, `ogg`, `wav`, `aac`, `m4a`, `opus`.
- Audio channel mode selection: `mono` and `stereo`.
- Single-instance enforcement — only one configuration entry is allowed.
- HACS compatibility (`hacs.json` metadata).
- GitHub Actions workflow for automated releases based on `manifest.json` version changes.
- GitHub Actions workflow for code validation.
