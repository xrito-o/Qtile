#!/bin/bash

# Store clipboard history in a file
cliphistory=$(xclip -o -selection clipboard 2>/dev/null)
if [ -n "$cliphistory" ]; then
  echo "$cliphistory" >> ~/.local/share/cliphistory.txt
fi

# Show clipboard history
choice=$(tac ~/.local/share/cliphistory.txt | yad --width=500 --height=300 --list --column="Clipboard History" --text="Select to copy:" --title="Clipboard Manager")

# Copy selected item to clipboard
if [ -n "$choice" ]; then
  echo -n "$choice" | xclip -selection clipboard
fi
