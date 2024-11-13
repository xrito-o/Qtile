#!/bin/bash

yad --title="Terminal Shortcuts" \
    --text="Here are some common terminal shortcuts" \
    --list --column="Shortcut" --column="Description" \
    "Ctrl + A" "Move cursor to the beginning of the line" \
    "Ctrl + E" "Move cursor to the end of the line" \
    "Ctrl + U" "Delete everything from the cursor to the beginning of the line" \
    "Ctrl + K" "Delete everything from the cursor to the end of the line" \
    "Ctrl + W" "Delete the word before the cursor" \
    "Ctrl + Y" "Paste previously cut text" \
    "Ctrl + L" "Clear the terminal screen" \
    "Ctrl + C" "Terminate the current running command" \
    "Ctrl + D" "Log out of the terminal" \
    "Ctrl + Z" "Suspend the current process" \
    "Ctrl + R" "Reverse search through the command history" \
    "Up Arrow" "Go to the previous command in history" \
    "Down Arrow" "Go to the next command in history" \
    "Tab" "Auto-complete commands or file names" \
    "Alt + F" "Move cursor forward by one word" \
    "Alt + B" "Move cursor backward by one word" \
    --width=800 --height=600 \

