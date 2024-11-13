#!/bin/bash

# Set GTK theme to Adwaita-dark (if installed)

wm_class=$(xprop | grep WM_CLASS)
if [ -z "$wm_class" ]; then
    yad --title="WM_CLASS Not Found" \
        --text="WM_CLASS not found. Click on a window to try again." \
        --button="OK:0" \
        --width=500 --height=200 \
        --fontname="Monospace 12" \
        --background="#2E3440" \  # Nord0 - dark background
        --foreground="#D8DEE9" \  # Nord4 - light text
        --button-background="#3B4252" \  # Nord1 - button background
        --no-buttons
else
    yad --title="WM_CLASS" \
        --form --field="WM_CLASS":TXT "$wm_class" \
        --button="OK:0" \
        --width=500 --height=200 \
        --fontname="Monospace 12" \
        --background="#2E3440" \  # Nord0 - dark background
        --foreground="#D8DEE9" \  # Nord4 - light text
        --button-background="#3B4252" \  # Nord1 - button background
        --no-buttons
fi
