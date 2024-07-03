import subprocess
import time
import wave
from pathlib import Path

import alsaaudio as aa
import keyboard
import pyaudio

from . import settings


def reproduce_sound(sound_path: Path = settings.SOUND_VOLUME_CHANGE):
    with wave.open(str(sound_path), "rb") as wf:
        p = pyaudio.PyAudio()

        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
        )

        while len(data := wf.readframes(1024)):
            stream.write(data)

        stream.close()
        p.terminate()


def increase_volume(mixer: aa.Mixer, step: int = settings.VOLUME_STEP):
    for i, current in enumerate(mixer.getvolume()):
        mixer.setvolume(min(100, current + step), channel=i)
    reproduce_sound()


def decrease_volume(mixer: aa.Mixer, step: int = settings.VOLUME_STEP):
    for i, current in enumerate(mixer.getvolume()):
        mixer.setvolume(max(0, current - step), channel=i)
    reproduce_sound()


if __name__ == "__main__":
    mixer = aa.Mixer(cardindex=settings.MIXER_CARD, control=settings.MIXER_CONTROL)

    keyboard.add_hotkey(115, lambda: increase_volume(mixer))
    keyboard.add_hotkey(114, lambda: decrease_volume(mixer))

    while True:
        time.sleep(0.1)
