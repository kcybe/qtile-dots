#!/bin/sh

# Display Settings
xrandr --output HDMI-0 --mode 3440x1440 --rate 100 &

# Wallpaper Settings
feh --bg-fill Pictures/Wallpapers/wallhaven-lmxrrp.png &

# Picom Settings
picom -b --experimental-backends & # Starting Picom 

# Mouse Settings
xinput set-prop "Logitech Gaming Mouse G502" "Coordinate Transformation Matrix" 2.000000, 0.000000, 0.000000, 0.000000, 2.000000, 0.000000, 0.000000, 0.000000, 1.000000 # Sensitivity
