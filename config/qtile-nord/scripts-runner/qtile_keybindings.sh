#!/bin/bash

yad --title="Qtile Keybindings" \
    --text="<b>Here are your current Qtile keybindings:</b>" \
    --list --column="Keybinding" --column="Description" \
    "Mod + Return" "Launch terminal" \
    "Mod + V" "Launch Rofi" \
    "Mod + B" "Open Web Browser" \
    "Mod + Tab" "Toggle between layouts" \
    "Mod + Q" "Kill focused window" \
    "Mod + Ctrl + R" "Reload the Qtile config" \
    "Mod + E" "Open File Manager (Thunar)" \
    "Mod + P" "Open Pavucontrol" \
    "Mod + S" "Run script-runner.sh" \
    "Mod + W" "Run get_wm_class.sh" \
    "Mod + Left" "Move focus to the left" \
    "Mod + Right" "Move focus to the right" \
    "Mod + Down" "Move focus down" \
    "Mod + Up" "Move focus up" \
    "Mod + Space" "Move focus to the next window" \
    "Mod + Shift + Left" "Move window to the left" \
    "Mod + Shift + Right" "Move window to the right" \
    "Mod + Shift + Down" "Move window down" \
    "Mod + Shift + Up" "Move window up" \
    "Mod + =" "Grow window to the left (BSP/Columns) / Grow (Monad)" \
    "Mod + -" "Grow window to the right (BSP/Columns) / Shrink (Monad)" \
    "Mod + Ctrl + Left" "Grow window to the left" \
    "Mod + Ctrl + Right" "Grow window to the right" \
    "Mod + Ctrl + Down" "Grow window down" \
    "Mod + Ctrl + Up" "Grow window up" \
    "Mod + N" "Normalize all window sizes" \
    "Mod + T" "Toggle floating mode" \
    "Mod + F" "Toggle fullscreen mode" \
    --width=1000 --height=800 \
