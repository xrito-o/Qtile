#!/bin/sh
xrandr --output HDMI-1 --mode 1920x1080 --rate 75 &
nitrogen --restore &
preload &
while pgrep -u $UID -x picom >/dev/null; do sleep 1; done
picom --config /home/xrito/.config/picom/picom.conf &
#picom --config /home/xrito/.config/picom/picom.conf --vsync &
nm-applet &
dunst -config .config/dunst/dunstrc &
volumeicon &
pulseaudio --start &
# pulseaudio -k &
# pulseaudio --start &
xfce4-clipman --daemon &
nohup firefox & disown &
com.spotify.Client --minimized &
dev.vencord.Vesktop &

#wallset --video .config/qtile/Live-wallpaper/mylivewallpapers.com-Cherry-Blossom-Japan-Street.mp4 &
#kitty &
