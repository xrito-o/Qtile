import os
import subprocess



from libqtile import hook
from libqtile.layout.columns import Columns
from libqtile.layout.verticaltile import VerticalTile
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating
from libqtile.config import (
    Click,
    Drag,
    DropDown,
    Group,
    Key,
    Match,
    ScratchPad,
    Screen
)
from libqtile.lazy import lazy

from colors import nord_fox
from colors import gruvbox


from bar1 import bar

mod = "mod4" #mod4 or mod = super key
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

browser = "firefox"
terminal = "kitty"
fileManager = "thunar"

#  _  _________   ______ ___ _   _ ____  ____
# | |/ / ____\ \ / / __ )_ _| \ | |  _ \/ ___|
# | ' /|  _|  \ V /|  _ \| ||  \| | | | \___ \
# | . \| |___  | | | |_) | || |\  | |_| |___) |
# |_|\_\_____| |_| |____/___|_| \_|____/|____/

keys = [
    # The essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "v", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
    Key([mod], "b", lazy.spawn(browser), desc='Web browser'),
    #Key([mod], "v", lazy.spawn("wofi --show drun"), desc="Launch Wofi"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "e", lazy.spawn(fileManager), desc="Launch Thunare"),
    Key([mod], "p", lazy.spawn("pavucontrol"), desc="Launch pavucontrol"),

    #Scripts
    Key([mod], "s", lazy.spawn("/home/xrito/.config/qtile/script-runner.sh"), desc="script-runner"),



    # Switch between windows
    # Some layouts like 'monadtall' only need to use j/k to move
    # through the stack, but other layouts like 'columns' will
    # require all four directions h/j/k/l to move around

    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),


    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow/shrink windows left/right.
    # This is mainly for the 'monadtall' and 'monadwide' layouts
    # although it does also work in the 'bsp' and 'columns' layouts.
    Key([mod], "equal",
        lazy.layout.grow_left().when(layout=["bsp", "columns"]),
        lazy.layout.grow().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left"
    ),
    Key([mod], "minus",
        lazy.layout.grow_right().when(layout=["bsp", "columns"]),
        lazy.layout.shrink().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left"
    ),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "left", lazy.layout.grow_left(), lazy.layout.grow(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), lazy.layout.grow(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    # Toggle between different layouts as defined below

    #Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),


]

#   ____ ____   ___  _   _ ____  ____
#  / ___|  _ \ / _ \| | | |  _ \/ ___|
# | |  _| |_) | | | | | | | |_) \___ \
# | |_| |  _ <| |_| | |_| |  __/ ___) |
#  \____|_| \_\\___/ \___/|_|   |____/

groups = [
    Group(
        '1',
        label="一",
        matches=[
            Match(wm_class='firefox'),
            Match(wm_class='brave'),
            Match(wm_class='qutebrowser')
        ],
        layout="monadtall"
    ),
    Group('2', label="二", layout="monadtall"),
    Group('3', label="三", layout="monadtall"),
    Group(
        '4',
        label="四",
        matches=[
            Match(wm_class="whatsdesk")
        ],
        layout="monadtall"
    ),
    Group(
        '5',
        label="五",
        layout="monadtall"
    ),
    Group('6', label="六", matches=[
          Match(wm_class="thunderbird")], layout="monadtall"),
    Group('7', label="七", layout="monadtall"),
    Group('8', label="八", layout="monadtall"),
    Group('9', label="九", layout="monadtall"),
]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])
# """
# --------
# |Groups|
# --------
# """
#
# groups = []
#
# group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#
# #group_labels = ["󰖟", "", "", "", "", "", "", "", "ﭮ", "", "", "﨣", "F1", "F2", "F3", "F4", "F5"]
# group_labels = ["", "" ,"", "", "", "", "", "", "", "'"]
#
# #group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
#
# group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]
#
# # Add group names, labels, and default layouts to the groups object.
# for i in range(len(group_names)):
#     groups.append(
#         Group(
#             name=group_names[i],
#             layout=group_layouts[i].lower(),
#             label=group_labels[i],
#         ))
#
#
#
# for i in groups:
#     keys.extend([
#
#         #CHANGE WORKSPACES
#         Key([mod], i.name, lazy.group[i.name].toscreen()),
#         Key([mod], "Tab", lazy.screen.next_group()),
#         Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
#         Key(["mod1"], "Tab", lazy.screen.next_group()),
#         Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
#
#         # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
#         #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
#
#         # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
#     ])

#  ____   ____ ____      _  _____ ____ _   _ ____   _    ____  ____
# / ___| / ___|  _ \    / \|_   _/ ___| | | |  _ \ / \  |  _ \/ ___|
# \___ \| |   | |_) |  / _ \ | || |   | |_| | |_) / _ \ | | | \___ \
#  ___) | |___|  _ <  / ___ \| || |___|  _  |  __/ ___ \| |_| |___) |
# |____/ \____|_| \_\/_/   \_\_| \____|_| |_|_| /_/   \_\____/|____/


groups.append(
    ScratchPad(
        'scratchpad',
        [
            DropDown(
                'term',
                'kitty',
                width=0.4,
                height=0.5,
                x=0.3,
                y=0.1,
                opacity=1
            ),
            DropDown(
                'mixer',
                'pavucontrol',
                width=0.4,
                height=0.6,
                x=0.3,
                y=0.1,
                opacity=1
            ),
            DropDown(
                'pomodoro',
                'pomatez',
                width=0.05,
                height=0.6,
                x=0.35,
                y=0.1,
                opacity=1
            ),
            DropDown(
                'blueman',
                'blueman-manager',
                width=0.05,
                height=0.6,
                x=0.35,
                y=0.1,
                opacity=1
            ),
        ]
    )
)

keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('mixer')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('pomodoro')),
    Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('blueman')),
])

#  _        _ __   _____  _   _ _____ ____
# | |      / \\ \ / / _ \| | | |_   _/ ___|
# | |     / _ \\ V / | | | | | | | | \___ \
# | |___ / ___ \| || |_| | |_| | | |  ___) |
# |_____/_/   \_\_| \___/ \___/  |_| |____/

layouts = [
    Stack(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['cyan'],
        border_width=2,
        num_stacks=1,
        margin=10,
    ),
    MonadTall(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['cyan'],
        margin=10,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    Columns(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['cyan'],
        border_width=2,
        border_normal_stack=nord_fox['black'],
        border_focus_stack=nord_fox['cyan'],
        border_on_single=2,
        margin=8,
        margin_on_single=10,
    ),
    VerticalTile(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['cyan'],
        border_width=2,
        border_on_single=2,
        margin=8,
        margin_on_single=10,
    ),
]

floating_layout = Floating(
    border_normal=nord_fox['bg'],
    border_focus=nord_fox['cyan'],
    border_width=2,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry

        # Match(wm_class="protonvpn"),
        Match(title="AICOMS"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="zoom "),
        Match(wm_class="bitwarden"),
        Match(wm_class="nemo"),
        Match(wm_class="xarchiver"),
    ])

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

widget_defaults = dict(
    # font='TerminessTTF Nerd Font',
    font='JetBrainsMono Nerd Font',
    fontsize=13,
    padding=10,
    bacgkround=nord_fox['bg'],
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=bar)
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = ''
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "focus" # or smart
reconfigure_screens = True
auto_minimize = True




wmname = "LG3D"


@ hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
