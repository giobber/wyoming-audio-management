import datetime as dt

import alsaaudio as aa
import astral
import pytz
from astral.sun import sun

from . import settings


def attenuate(mixer: aa.Mixer, percentage: float = 0.25):
    current = mixer.getvolume()
    mixer.setvolume(int(current * (1 - percentage)))


if __name__ == "__main__":
    mixer = aa.Mixer(cardindex=settings.MIXER_CARD, control=settings.MIXER_CONTROL)

    now = dt.datetime.now(tz=pytz.timezone(location.timezone))
    data = sun(location.observer)

    attenuate(mixer)
