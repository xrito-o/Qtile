#!/bin/bash

# Define the directory to save screenshots
screenshot_dir="/home/xrito/screenshot/"

# Create the directory if it doesn't exist
mkdir -p "$screenshot_dir"

# Take a screenshot with a 2-second delay
scrot -d 1 "$screenshot_dir/screenshot_$(date +%Y-%m-%d_%H-%M-%S).png"

# Notify user that the screenshot has been taken
notify-send "Screenshot Taken" "Screenshot saved to $screenshot_dir"
