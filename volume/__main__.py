import keyboard

from volume.handlers import on_volume_down, on_volume_up

keyboard.add_hotkey(115, on_volume_up)
keyboard.add_hotkey(114, on_volume_down)


while True:
    pass
