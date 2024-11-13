
# ╔════════════════════════════════════════════════════════════════╗
# ║    ____  __  _ __        ______            _____               ║
# ║   / __ \/ /_(_) /__     / ____/___  ____  / __(_)___ _         ║
# ║  / / / / __/ / / _ \   / /   / __ \/ __ \/ /_/ / __ `/         ║
# ║ / /_/ / /_/ / /  __/  / /___/ /_/ / / / / __/ / /_/ /          ║
# ║ \___\_\__/_/_/\___/   \____/\____/_/ /_/_/ /_/\__, /           ║
# ║                                              /____/            ║
# ╚════════════════════════════════════════════════════════════════╝
# ╔════════════════════════════════════════════════════════════════╗
# ║ Author: xrito-o (github.com/xrito-o)                           ║
# ║ Link: https://github.com/xrito/qtile                           ║
# ║ Date: 13 June, 2024                                            ║
# ║ Last Modified: 10 November, 2024                               ║
# ╚════════════════════════════════════════════════════════════════╝



# ╔════════════════════════════════════════════════════════════════╗
# ║                     IMPORTS CONFIGURATION                      ║
# ╚════════════════════════════════════════════════════════════════╝

import os                           # Operating system interface
import re                           # Regular expression library
import socket                       # Networking library
import subprocess                   # Subprocess control

from typing import List             # Type hinting for list
from libqtile import bar, layout, qtile, widget, hook, extension  # Qtile essentials
from libqtile.config import Click, Drag, Group, ScratchPad, DropDown, Key, Match, Screen, Rule  # Qtile configuration
from libqtile.lazy import lazy      # Lazy loading functions
from libqtile.utils import guess_terminal  # Guess default terminal
from libqtile.layout.floating import Floating  # Floating window layout
from qtile_extras import widget      # Extra widgets for Qtile

from colors import nord_fox         # Nord Fox color scheme
from bar1 import bar                # Custom bar configuration


# ╔════════════════════════════════════════════════════════════════╗
# ║                        VARIABLES CONFIGURATION                 ║
# ╚════════════════════════════════════════════════════════════════╝

mod = "mod4" #mod4 or mod = super key
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

browser = "firefox"
terminal = "kitty"
fileManager = "thunar"

# ╔════════════════════════════════════════════════════════════════╗
# ║               OPTIONAL APPLICATION CONFIGURATION               ║
# ╚════════════════════════════════════════════════════════════════╝


#text_editor = "code"  # Example: Visual Studio Code
#media_player = "mpv"   # Example: MPV media player
#screenshot_tool = "flameshot"  # Example: Flameshot for screenshots
#email_client = "thunderbird"    # Example: Thunderbird for email
#chat_app = "slack"              # Example: Slack for chat

# ╔════════════════════════════════════════════════════════════════╗
# ║              ADDITIONAL UTILITIES CONFIGURATION                ║
# ╚════════════════════════════════════════════════════════════════╝

# Additional Utilities
#clipboard_manager = "clipmenu"  # Example: Clipmenu for clipboard management
#file_search_tool = "rofi"        # Example: Rofi for application launcher



# ╔════════════════════════════════════════════════════════════════╗
# ║                     KEYBINDINGS CONFIGURATION                  ║
# ╚════════════════════════════════════════════════════════════════╝


keys = [
    # The essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "v", lazy.spawn("rofi -show drun -theme ~/.config/rofi/matty.rasi"), desc="Launch Rofi"),
    Key([mod], "b", lazy.spawn(browser), desc='Web browser'),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod], "e", lazy.spawn(fileManager), desc="Launch Thunare"),
    Key([mod], "p", lazy.spawn("pavucontrol"), desc="Launch pavucontrol"),
    Key([mod, "shift"], "w", lazy.spawn("xvkbd"), desc="Launch xvkbd"),


    

    #Scripts
    Key([mod], "s", lazy.spawn("/home/xrito/.config/qtile/script-runner.sh"), desc="script-runner"),
    #Key([mod], "w", lazy.spawn("/home/xrito/.config/qtile/scripts/get_wm_class.sh")),

    # Switch between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),


    # Move windows between left/right columns or move up/down in current stack
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow/shrink windows left/right
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

    # Grow windows in specific directions
    Key([mod, "control"], "left", lazy.layout.grow_left(), lazy.layout.grow(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), lazy.layout.grow(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),

]

# Add key bindings to switch VTs in Wayland
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )



# ╔════════════════════════════════════════════════════════════════╗
# ║                           GROUPS CONFIGURATION                 ║
# ╚════════════════════════════════════════════════════════════════╝


groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


group_labels = ["", "" ,"", "", "", "", "", "", "", "'"]


group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

# Add group names, labels, and default layouts to the groups object.
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))



for i in groups:
    keys.extend([

        #CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])



# ╔════════════════════════════════════════════════════════════════╗
# ║                         SCRATCHPAD CONFIGURATION               ║
# ╚════════════════════════════════════════════════════════════════╝

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
                'fileManager',
                'thunar',
                width=0.6,
                height=0.6,
                x=0.2,
                y=0.1,
                opacity=1
            ),
        ]
    )
)
keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('mixer')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('fileManager')),

])


# ╔════════════════════════════════════════════════════════════════╗
# ║                       LAYOUT CONFIGURATION                     ║
# ╚════════════════════════════════════════════════════════════════╝

def init_layout_theme():
    return {
        "margin": 4,
        "border_width": 2,
        "border_focus": nord_fox['fg'],
        "border_normal": nord_fox['black'],
    }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['fg'],
        margin=8,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    layout.MonadWide(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['fg'],
        margin=8,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    layout.Matrix(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['fg'],
        margin=8,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    layout.Bsp(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['fg'],
        margin=8,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    layout.Floating(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['fg'],
        margin=8,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    layout.RatioTile(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['fg'],
        margin=8,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    layout.TreeTab(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['fg'],
        margin=8,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    layout.Max(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['fg'],
        margin=8,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    )
]

# ╔═══════════════════════════════════════════════════════════════╗
# ║                    WIDGET CONFIGURATION                       ║
# ╚═══════════════════════════════════════════════════════════════╝

widget_defaults = dict(
    # font='TerminessTTF Nerd Font',
    font='JetBrainsMono Nerd Font',
    fontsize=13,
    padding=10,
    background=nord_fox['bg'],
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=bar)
]


# ╔═══════════════════════════════════════════════════════════════╗
# ║                         MOUSE CONFIGURATION                   ║
# ╚═══════════════════════════════════════════════════════════════╝


# MOUSE CONFIGURATION
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list



# ╔═══════════════════════════════════════════════════════════════╗
# ║                      FLOATING WINDOW SETTINGS                 ║
# ╚═══════════════════════════════════════════════════════════════╝


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,

    Match(wm_class="confirmreset"),   # gitk
    Match(wm_class="dialog"),         # dialog boxes
    Match(wm_class="download"),       # downloads
    Match(wm_class="error"),          # error msgs
    Match(wm_class="file_progress"),  # file progress boxes
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pavucontrol'),    # pavucontrol
    Match(wm_class='nitrogen'),       # nitrogen
    Match(wm_class='stacer'),         # stacer
    Match(wm_class="makebranch"),     # gitk
    Match(wm_class="maketag"),        # gitk
    Match(wm_class="notification"),   # notifications
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
    Match(wm_class="ssh-askpass"),    # ssh-askpass
    Match(wm_class="toolbar"),        # toolbars
    Match(wm_class="Yad"),            # yad boxes
    Match(title="branchdialog"),      # gitk
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(title="pinentry"),          # GPG key password entry
    Match(title="tastycharts"),       # tastytrade pop-out charts
    Match(title="tastytrade"),        # tastytrade pop-out side gutter
    Match(title="tastytrade - Portfolio Report"), # tastytrade pop-out allocation
    Match(wm_class="tasty.javafx.launcher.LauncherFxApp"), # tastytrade settings
    Match(wm_class='confirm'),
    Match(wm_class='splash'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='archlinux-logout'),
    Match(wm_class='xvkbd'),



],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "qtile"

# ╔══════════════════════════════════╗
# ║          STARTUP_ONCE            ║
# ╚══════════════════════════════════╝


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('/home/xrito/.config/qtile/scripts/conky.sh')
    subprocess.Popen([home])



# ╔════════════════════════════════════════════╗
# ║          APPLICATION GROUP ASSIGNMENT      ║
# ╚════════════════════════════════════════════╝



@hook.subscribe.client_new
def assign_app_group(client):
    # Rules to assign specific applications to specific groups
    app_group = {
        "firefox": "3",         # Firefox to group 3
        "code-oss": "5",
        "virt-manager": "7",
        "Spotify": "9",         # Spotify to group 9
        "vesktop": "0"          # VSCodium (vesktop) to group 0

    }

    wm_class = client.window.get_wm_class()
    if wm_class:
        for app, group in app_group.items():
            if app in wm_class:
                client.togroup(group)

