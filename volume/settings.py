from pathlib import Path

from decouple import config

PROJECT_PATH = Path(__file__).parent.parent

VOLUME_STEP = config("VOLUME_STEP", 5, int)

CARD_ID = config("CARD_ID", 1, int)
DEVICE_ID = config("DEVICE_ID", "PCM,0")
DEVICE_FANCY_ID = config("DEVICE_FANCY_ID", "sysdefault:CARD=Phone")

SOUND_PATH = config("SOUND_PATH", PROJECT_PATH / "sounds", Path)
SOUND_VOLUME_CHANGE = config(
    "SOUND_VOLUME_CHANGE", SOUND_PATH / "volume_change.wav", Path
)
