import time

import alsaaudio as aa
import requests

from . import settings, volume


class HomeAssistantAPI:
    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "content-type": "application/json",
        }

    def get_entity_state(self, entity_id: str) -> dict:
        url = f"{self.url}/states/{entity_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            print(f"Connection error with code {response.status_code}")
            return {}
        return response.json()


if __name__ == "__main__":
    api = HomeAssistantAPI(settings.HA_URL, settings.HA_TOKEN)

    while True:
        time.sleep(2)

        state = api.get_entity_state(settings.HA_VOLUME_ENTITY)

        if (level := state.get("state")) is None:
            continue

        level = int(float(level))
        level = min(level, 100)
        level = max(level, 0)

        mixer = aa.Mixer(cardindex=settings.MIXER_CARD, control=settings.MIXER_CONTROL)
        current = mixer.getvolume()

        print(f"current: {current}, ha: {level}")
        for ch, cv in enumerate(current):
            if cv != level:
                mixer.setvolume(int(level), channel=ch)

        if any(ch != level for ch in current):
            volume.reproduce_sound()

        mixer.close()
