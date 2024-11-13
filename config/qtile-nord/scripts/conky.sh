#!/bin/bash

# This command will close all active conky
killall conky
sleep 2s
		
# Only the config listed below will be avtivated
# if you want to combine with another theme, write the command here
#conky -c /home/xrito/.config/conky/qtile/01/DoomOne.conf &> /dev/null &
conky -c /home/xrito/.config/conky/qtile/01/Nord.conf &> /dev/null &
exit
