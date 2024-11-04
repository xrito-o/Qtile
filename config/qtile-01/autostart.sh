#!/bin/sh
xrandr --output Virtual-1 --mode 1920x1080 &
nitrogen --restore &
#while pgrep -u $UID -x picom >/dev/null; do sleep 1; done
#picom --config /home/xrito/.config/picom/picom.conf &
#picom &
#rm -rf .wallpapers/video/ &
#nm-applet &
dunst &
volumeicon &
pulseaudio --start &
#polybar &
#firefox &
#kitty &
#dev.vencord.Vesktop &
#wallset --video .config/qtile/Live-wallpaper/mylivewallpapers.com-Cherry-Blossom-Japan-Street.mp4 &
