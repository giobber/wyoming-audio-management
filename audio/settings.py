from pathlib import Path

import astral
from decouple import config

PROJECT_PATH = Path(__file__).parent.parent

VOLUME_STEP = config("VOLUME_STEP", 5, int)

CARD_ID = config("CARD_ID", 0, int)
DEVICE_ID = config("DEVICE_ID", "PCM,0")
DEVICE_FANCY_ID = config("DEVICE_FANCY_ID", "sysdefault:CARD=Phone")

SOUND_PATH = config("SOUND_PATH", PROJECT_PATH / "sounds", Path)
SOUND_VOLUME_CHANGE = config(
    "SOUND_VOLUME_CHANGE", SOUND_PATH / "volume_change.wav", Path
)

MIXER_CONTROL = config("MIXER_CONTROL", "PCM")
MIXER_CARD = config("MIXER_CARD", 0, cast=int)


ASTRAL_CITY = config("ASTRAL_CITY", "Rome")
ASTRAL_COUNTRY = config("ASTRAL_COUNTRY", "Italy")
ASTRAL_TZ = config("ASTRAL_TZ", "Europe/Rome")
ASTRAL_LATITUDE = config("ASTRAL_LATITUDE", 41.89193, cast=float)
ASTRAL_LONGITUDE = config("ASTRAL_LONGITUDE", 12.51133, cast=float)

ASTRAL_LOCATION = astral.LocationInfo(
    ASTRAL_CITY, ASTRAL_COUNTRY, ASTRAL_TZ, ASTRAL_LATITUDE, ASTRAL_LONGITUDE
)
