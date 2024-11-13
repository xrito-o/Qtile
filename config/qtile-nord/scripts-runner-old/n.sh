#!/bin/bash

# Define options
options=("Down" "Up")

# Use rofi to display the options
selected=$(printf "%s\n" "${options[@]}" | rofi -dmenu -p "Select WireGuard action:")

# Check the selected option and run the corresponding command
case $selected in
    "Down")
        sudo wg-quick down wg0
        ;;
    "Up")
        sudo wg-quick up wg0
        ;;
    *)
        echo "Invalid option"
        ;;
esac
