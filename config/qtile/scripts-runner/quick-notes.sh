#!/bin/bash

# Create a new note with a timestamp
note_file="$HOME/notes/$(date +%Y-%m-%d_%H-%M-%S).txt"

# Open the new note in Mousepad
mousepad "$note_file" &
