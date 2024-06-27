#!/usr/bin/sh

BROWSER="firefox"

declare -a options=(

"1 - https://youtube.com"
"2 - https://reddit.com"
"3 - https://monkeytype.com"
"4 - https://reddit.com/r/unixporn"
"5 - https://github.com"
"6 - https://www.nerdfonts.com/cheat-sheet"
"7 - https://wallhaven.cc"
"8 - https://www.geeksforgeeks.org/how-to-create-a-shell-script-in-linux/"
"9 - https://rms-support-letter.github.io/"



"quit"
)

choice=$(printf '%s\n' "${options[@]}" | rofi -dmenu -i -l 9 -p 'Bookmarks')


if [[ "$choice" == quit ]]; then
	echo "Program Terminated." && exit 1
elif [ "$choice" ]; then
	cfg=$(printf '%s\n' "${choice}" | awk '{print $NF}')
	$BROWSER "$cfg"
else
	echo "Program Terminated." && exit 1
fi





