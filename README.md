[![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<img width="200" height="200" alt="image" src="https://github.com/Geek-MD/Audio_Tools/blob/main/custom_components/audio_tools/brand/icon.png?raw=true" />

# Audio Tools

A [Home Assistant](https://www.home-assistant.io/) custom integration that provides audio processing tools, including format conversion and channel-mode selection, powered by `ffmpeg`.

---

## Features

- **Audio format conversion** — convert audio files between popular formats.
- **Supported output formats:** `mp3`, `flac`, `ogg`, `wav`, `aac`, `m4a`, `opus`.
- **Channel modes:** `mono` and `stereo`.
- **Config flow UI** — set up directly from the Home Assistant integrations page.
- **Optional Work Directory** — configure a default working directory shown in the UI.

---

## Requirements

| Requirement | Version |
|---|---|
| Home Assistant | ≥ 2024.6.0 |
| `ffmpeg` | available in system `PATH` |

---

## Installation

### Via HACS (recommended)

1. Open HACS in your Home Assistant instance.
2. Go to **Integrations** → click the three-dot menu → **Custom repositories**.
3. Add `https://github.com/Geek-MD/Audio_Tools` with category **Integration**.
4. Search for **Audio Tools** and install it.
5. Restart Home Assistant.

### Manual

1. Copy the `custom_components/audio_tools` directory into your Home Assistant `custom_components` folder.
2. Restart Home Assistant.

---

## Configuration

1. Go to **Settings → Devices & Services → Add Integration**.
2. Search for **Audio Tools** and click it.
3. Optionally enter a **Work Directory** path (e.g. `/media/audio`). This is informational — each service call always specifies the full file paths explicitly.
4. Click **Submit**.

---

## Usage

Once configured, Audio Tools exposes Home Assistant services for audio processing.  
Service calls always accept full absolute file paths for input and output files.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a full history of changes.

---

## License

This project is licensed under the [MIT License](LICENSE).
