# wyoming-satellite-extension
This project aim to extend functionality for a wyoming satellites build on a raspberry pi.
This repo contains a couple of scripts I use on my raspberry pi with wyoming satellite installed.

My objective is to gradually move from the actual voice assistant I use (a google nest hub) to a raspberry pi based wyoming satellite.
Altought is impressive the results reach from the wyoming project, only a subset of the features and commodities expected from a voice assistant is available after installing it.

## Roadmap
- [x] A script to play a sound when volume keys is pressed (my microphone has physical buttons)
- [ ] Volume level available and editable in home assistant
- [ ] Volume level auto-adjusted on scheduled times (custom or based on local sunrise/sunset time)
- [ ] ...

## Install
On a raspberry pi with Raspberry Pi OS Lite and wyoming-satellite already installed
```shell
$ mkdir git && cd git
$ git clone https://github.com/giobber/wyoming-satellite-extension.git
$ cd wyoming-satellite-extension
$ sudo make install
```
