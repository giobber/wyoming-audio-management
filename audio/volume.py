import subprocess
import time
from pathlib import Path

import keyboard

from . import settings

CARD_ID = 1
STEP = 5


def on_volume_up():
    subprocess.Popen(
        [
            "amixer",
            "sset",
            "-c",
            f"{settings.CARD_ID}",
            settings.DEVICE_ID,
            f"{settings.VOLUME_STEP}%+",
        ]
    )
    subprocess.Popen(
        [
            "aplay",
            "--device",
            settings.DEVICE_FANCY_ID,
            str(settings.SOUND_VOLUME_CHANGE),
        ]
    )


def on_volume_down():
    subprocess.Popen(
        [
            "amixer",
            "sset",
            "-c",
            f"{settings.CARD_ID}",
            settings.DEVICE_ID,
            f"{settings.VOLUME_STEP}%-",
        ]
    )
    subprocess.Popen(
        [
            "aplay",
            "--device",
            settings.DEVICE_FANCY_ID,
            str(settings.SOUND_VOLUME_CHANGE),
        ]
    )


keyboard.add_hotkey(115, on_volume_up)
keyboard.add_hotkey(114, on_volume_down)


if __name__ == "__main__":
    while True:
        time.sleep(0.1)
