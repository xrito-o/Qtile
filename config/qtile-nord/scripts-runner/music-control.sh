#!/bin/bash

# Define music control commands
commands=(
  "Play:playerctl play"
  "Pause:playerctl pause"
  "Next:playerctl next"
  "Previous:playerctl previous"
  "Stop:playerctl stop"
)

# Use Rofi to display the commands
selected_command=$(printf "%s\n" "${commands[@]}" | rofi -dmenu -p "🎵 Select music action:" )

# Extract and execute the command
if [ -n "$selected_command" ]; then
  command=${selected_command#*:}
  eval "$command"
fi
