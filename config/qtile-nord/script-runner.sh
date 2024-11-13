#!/bin/bash

# Specify the directory containing your scripts
script_dir="$HOME/.config/qtile/scripts-runner/"

# Get a list of scripts in the directory
scripts=($(ls "$script_dir"))

# Use Rofi to display the scripts
selected_script=$(printf "%s\n" "${scripts[@]}" | rofi -dmenu -p "Select a script:")

# Execute the selected script
if [ -n "$selected_script" ]; then
  bash "$script_dir/$selected_script"
fi
