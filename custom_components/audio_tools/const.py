"""Constants for the Audio Tools integration."""

DOMAIN = "audio_tools"
CONF_WORK_DIR = "work_dir"
DEFAULT_WORK_DIR = ""

# Sensor states
STATE_WORKING = "working"
STATE_IDLE = "idle"

# Supported audio formats (ffmpeg format id)
SUPPORTED_FORMATS: dict[str, str] = {
    "mp3": "mp3",
    "flac": "flac",
    "ogg": "ogg",
    "wav": "wav",
    "aac": "aac",
    "m4a": "m4a",
    "opus": "opus",
}

# Valid output formats for the service (user-facing)
VALID_OUTPUT_FORMATS = list(SUPPORTED_FORMATS.keys())

# Audio channel modes
CHANNEL_MONO = "mono"
CHANNEL_STEREO = "stereo"
VALID_CHANNEL_MODES = [CHANNEL_MONO, CHANNEL_STEREO]
