import subprocess
import time
import wave
from pathlib import Path

import alsaaudio as aa
import keyboard
import pyaudio

from . import settings


def reproduce_sound(sound_path: Path = settings.SOUND_VOLUME_CHANGE, **stream_options):
    stream_options.setdefault("output", True)
    stream_options.setdefault("output_device_index", settings.MIXER_CARD)

    with wave.open(str(sound_path), "rb") as wf:
        p = pyaudio.PyAudio()

        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            **stream_options,
        )

        while len(data := wf.readframes(1024)):
            stream.write(data)

        stream.close()
        p.terminate()


def increase_volume(step: int = settings.VOLUME_STEP):
    mixer = aa.Mixer(cardindex=settings.MIXER_CARD, control=settings.MIXER_CONTROL)
    for i, current in enumerate(mixer.getvolume()):
        mixer.setvolume(min(100, current + step), channel=i)
    reproduce_sound()
    mixer.close()


def decrease_volume(step: int = settings.VOLUME_STEP):
    mixer = aa.Mixer(cardindex=settings.MIXER_CARD, control=settings.MIXER_CONTROL)
    for i, current in enumerate(mixer.getvolume()):
        mixer.setvolume(max(0, current - step), channel=i)
    reproduce_sound()
    mixer.close()


if __name__ == "__main__":

    keyboard.add_hotkey(115, lambda: increase_volume())
    keyboard.add_hotkey(114, lambda: decrease_volume())

    keyboard.wait()
