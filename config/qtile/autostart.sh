#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &

picom &
feh --bg-fill /home/david/.config/qtile/wallpaper.jpg
