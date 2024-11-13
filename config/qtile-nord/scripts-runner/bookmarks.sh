#!/usr/bin/sh

BROWSER="firefox"

declare -a options=(

"1 - (youtube)   								https://youtube.com"
"2 - (reddit) 									https://reddit.com"
"3 - (monkeytype) 								https://monkeytype.com"
"4 - (unixporn) 								https://reddit.com/r/unixporn"
"5 - (github) 									https://github.com"
"6 - (nerdfonts-cheat-sheet) 					https://www.nerdfonts.com/cheat-sheet"
"7 - (wallhaven) 								https://wallhaven.cc"
"8 - (how-to-create-a-shell-script-in-linux) 	https://www.geeksforgeeks.org/how-to-create-a-shell-script-in-linux/"
"9 - (wabsites-style) 							https://rms-support-letter.github.io/"
"10 -(Rofi-User-scripts) 						https://github.com/davatorium/rofi/wiki/User-scripts"



"quit"
)

choice=$(printf '%s\n' "${options[@]}" | rofi -dmenu -i -l 10 -p 'Bookmarks')


if [[ "$choice" == quit ]]; then
	echo "Program Terminated." && exit 1
elif [ "$choice" ]; then
	cfg=$(printf '%s\n' "${choice}" | awk '{print $NF}')
	$BROWSER "$cfg"
else
	echo "Program Terminated." && exit 1
fi





