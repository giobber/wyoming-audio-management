import astral
import datetime as dt
import pytz

from astral.sun import sun

location = astral.LocationInfo("Sassuolo", "Italy", "Europe/Rome", 44.55, 10.78)


if __name__ == "__main__":
    now = dt.datetime.now(tz=pytz.timezone(location.timezone))
    data = sun(location.observer)

    for key, value in data.items():
        print(now)
        print(value)

        if now > value:
            print(key)
            break

    print(sun(location.observer))
