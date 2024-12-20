
#######################################################
#    ____  __  _ __        ______            _____
#   / __ \/ /_(_) /__     / ____/___  ____  / __(_)___ _
#  / / / / __/ / / _ \   / /   / __ \/ __ \/ /_/ / __ `/
# / /_/ / /_/ / /  __/  / /___/ /_/ / / / / __/ / /_/ /
# \___\_\__/_/_/\___/   \____/\____/_/ /_/_/ /_/\__, /
#                                              /____/
#######################################################
# Author: xrito-o (github.com/xrito-o)
# Link: https://github.com/xrito/qtile
# Date: 13 June, 2024
# Last Modified: 13 June, 2024
#######################################################



"""
---------
│Imports|
---------
"""
import os
import re
import socket
import subprocess

from typing import List  # noqa: F401
from libqtile import bar, layout, qtile, widget, hook, extension
from libqtile.config import Click, Drag, Group, ScratchPad, DropDown, Key, Match, Screen, Rule
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.layout.floating import Floating
from qtile_extras import widget

"""
-----------
|Variables|
-----------
"""

mod = "mod4" #mod4 or mod = super key
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

browser = "firefox"
terminal = "kitty"
fileManager = "thunar"

#text_editor = "code"  # Example: Visual Studio Code
#media_player = "mpv"   # Example: MPV media player
#screenshot_tool = "flameshot"  # Example: Flameshot for screenshots
#email_client = "thunderbird"    # Example: Thunderbird for email
#chat_app = "slack"              # Example: Slack for chat
#
# Additional Utilities
#clipboard_manager = "clipmenu"  # Example: Clipmenu for clipboard management
#file_search_tool = "rofi"        # Example: Rofi for application launcher

"""
--------
|Colors|
--------
"""

def init_colors():
    return [
        ["#242831", "#242831"],  # 0: Dark background
        ["#1c1f24", "#1c1f24"],  # 1: Darker shade
        ["#dfdfdf", "#dfdfdf"],  # 2: Light gray
        ["#ff6c6b", "#ff6c6b"],  # 3: Red accent
        ["#98be65", "#98be65"],  # 4: Green accent
        ["#da8548", "#da8548"],  # 5: Orange accent
        ["#51afef", "#51afef"],  # 6: Blue accent
        ["#c678dd", "#c678dd"],  # 7: Magenta accent
        ["#ebcb8b", "#ebcb8b"],  # 8: Yellow accent
        ["#a9a1e1", "#a9a1e1"],  # 9: Light purple
        ["#66b2b2", "#66b2b2"],  # 10: Cyan
        ["#2e3440", "#2e3440"],  # 11: Background color
        ["#d8dee9", "#d8dee9"],  # 12: Foreground color
        ["#3b4252", "#3b4252"],  # 13: Lighter background
        ["#bf616a", "#bf616a"],  # 14: Red
        ["#a3be8c", "#a3be8c"],  # 15: Green
        ["#ebcb8b", "#ebcb8b"],  # 16: Yellow
        ["#81a1c1", "#81a1c1"],  # 17: Blue
        ["#b48ead", "#b48ead"],  # 18: Magenta
        ["#88c0d0", "#88c0d0"],  # 19: Cyan
        ["#e5e9f0", "#e5e9f0"],  # 20: White
        ["#4c566a", "#4c566a"],  # 21: Grey
        ["#d08770", "#d08770"],  # 22: Orange
        ["#8fbcbb", "#8fbcbb"],  # 23: Light cyan
        ["#5e81ac", "#5e81ac"],  # 24: Light blue
        ["#242831", "#242831"],  # 25: Dark background
        ["#ebcb8b", "#ebcb8b"],  # 26: Extra yellow
    ]

colors = init_colors()



"""
--------------
|Key Bindings|
--------------
"""


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

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )



"""
--------
|Groups|
--------
"""

groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

#group_labels = ["󰖟", "", "", "", "", "", "", "", "ﭮ", "", "", "﨣", "F1", "F2", "F3", "F4", "F5"]
group_labels = ["", "" ,"", "", "", "", "", "", "", "'"]

#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

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


"""
------------
|ScratchPad|
------------
"""

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
                width=0.4,
                height=0.6,
                x=0.3,
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



"""
---------
|Layouts|
---------
"""



def init_layout_theme():
    return {"margin":4,
            "border_width":2,
            "border_focus": colors[9],
            "border_normal": "#384149"
            }

layout_theme = init_layout_theme()


layouts = [
    #layout.MonadTall(margin=8, border_width=3, border_focus="#384149", border_normal="#1f252a"),
    layout.MonadTall(**layout_theme),
    #layout.MonadWide(margin=8, border_width=3, border_focus="#384149", border_normal="#1f252a"),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(**layout_theme),
    #layout.Max(**layout_theme)
]

"""
---------
|Widgets|
---------
"""

# WIDGETS FOR THE BAR
def init_widgets_defaults():
    return dict(
                font="JetBrainsMono Nerd Font",
                fontsize=14,
                padding=2,
                background=colors[0])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    widgets_list = [
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[2],
                    background=colors[0],
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/face",
                    scale="False",
                    margin=5,
                    foreground=colors[2],
                    background=colors[0],
                    mouse_callbacks={
                        'Button1': lazy.spawn('rofi -show drun'),
                        'Button3': lambda: qtile.cmd_spawn('/home/xrito/.config/qtile/scripts/config.sh')
                        },

                ),
                widget.Sep(
                    linewidth=1,
                    padding=10,
                    foreground=colors[1],
                    background=colors[0]
                ),
                widget.GroupBox(
                    font="Ubuntu Bold",
                    fontsize=14,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=10,
                    borderwidth=3,
                    active=colors[26],
                    inactive=colors[2],
                    rounded=True,
                    highlight_color=colors[1],
                    highlight_method="line",
                    this_current_screen_border=colors[6],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[6],
                    other_screen_border=colors[4],
                    foreground=colors[2],
                    background=colors[0]
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground=colors[1],
                    padding=0,
                    fontsize=50
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser(
                        "~/.config/qtile/icons")],
                    foreground=colors[9],
                    background=colors[0],
                    padding=0,
                    scale=0.45,
                ),
                widget.CurrentLayout(
                    foreground=colors[26],
                    background=colors[0],
                    padding=5,
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground=colors[1],
                    padding=2,
                    fontsize=50
                ),
                # widget.Sep(
                #     linewidth=1,
                #     padding=10,
                #     foreground=colors[1],
                #     background=colors[0]
                # ),
                widget.TaskList(
                    icon_size = 13,
                    font = "JetBrainsMono Nerd Font",
                    fontsize= 13,
                    foreground = colors[0],
                    background = colors[0],
                    borderwidth = 0,
                    border = colors[26],
                    margin_y = -3,
                    margin = 0,
                    padding = 8,
                    highlight_method = "block",
                    title_width_method = "uniform",
                    urgent_alert_method = "border",
                    urgent_border = colors[0],
                    rounded = False,
                    txt_floating = "🗗 ",
                    txt_maximized = "🗖 ",
                    txt_minimized = "🗕 ",
        ),
#                 widget.WindowName(
#                     foreground=colors[8],
#                     background=colors[0],
#                     padding=0,
#                     max_chars = 40,
#                     empty_group_string = '---',
#                     fontsize=15,
#
#                 ),
#                 ####

                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground=colors[1],
                    padding=0,
                    fontsize=60
                ),


                widget.Systray(
                    icon_size=15,
                    padding=2,
                    background=colors[0],
                    foreground=colors[26],

                    ),
                 widget.TextBox(
                    text='  ',
                    background=colors[0],
                    foreground=colors[26],
                    padding=2,
                    fontsize=15,
                    mouse_callbacks={'Button1': lazy.spawn('de.shorsh.discord-screenaudio')},
                ),
                 widget.TextBox(
                    text='   ',
                    background=colors[0],
                    foreground=colors[26],
                    padding=2,
                    fontsize=15,
                    mouse_callbacks={'Button1': lazy.spawn('com.github.KRTirtho.Spotube')},
                ),
                 widget.TextBox(
                    text='  ',
                    background=colors[0],
                    foreground=colors[26],
                    padding=2,
                    fontsize=15,
                    mouse_callbacks={'Button1': lazy.spawn("/home/xrito/.config/qtile/scripts/keyboard.sh")},
                ),

                widget.TextBox(
                    text='  ',
                    background=colors[0],
                    foreground=colors[26],
                    padding=2,
                    fontsize=15,
                    mouse_callbacks={'Button1': lazy.spawn('stacer')},
                ),

                widget.TextBox(
                    text='󰋫 ',
                    background=colors[0],
                    foreground=colors[26],
                    padding=2,
                    fontsize=20,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('nitrogen')},
                ),
                # widget.TextBox(
                #     text='|',
                #     font="Ubuntu Mono",
                #     background=colors[0],
                #     foreground=colors[1],
                #     padding=0,
                #     fontsize=60
                # ),
                # widget.TextBox(
                #     text = " ",
                #     fontsize = 14,
                #     font = "JetBrainsMono Nerd Font",
                #     foreground=colors[8],
                # ),
                #
                # widget.CPU(
                #     font = "JetBrainsMono Nerd Font",
                #     update_interval = 1.0,
                #     format = '{load_percent}%',
                #     foreground=colors[8],
                #     padding = 5
                # ),
                #  widget.Sep(
                #     linewidth = 0,
                #     padding = 10
                # ),
                # widget.TextBox(
                #     text = "",
                #     fontsize = 14,
                #     font = "JetBrainsMono Nerd Font",
                #     foreground=colors[8],
                # ),
                # widget.Memory(
                #     font = "JetBrainsMonoNerdFont",
                #     foreground=colors[8],
                #     format = '{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}',
                #     measure_mem='G',
                #     padding = 5,
                # ),
                # widget.Sep(
                #     linewidth = 0,
                #     padding = 10
                # ),


                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground=colors[1],
                    padding=0,
                    fontsize=60
                ),
                widget.TextBox(
                    text='󰓃',
                    background=colors[0],
                    foreground=colors[26],
                    padding=3,
                    fontsize=20,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")},
                ),
                widget.Volume(
                    foreground=colors[26],
                    background=colors[0],
                    fmt='{}',
                    padding=3,
                    fontsize=14,
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground=colors[1],
                    padding=0,
                    fontsize=60
                ),


                widget.TextBox(
                    text='󰈀 ',
                    background=colors[0],
                    foreground=colors[26],
                    padding=0,
                    fontsize=20,
                ),
                widget.Net(
                    foreground=colors[26],
                    background=colors[0],
                    format = ' {down:.0f}{down_suffix}    {up:.0f}{up_suffix}',
                    prefix='M'


                ),
                widget.Sep(
                    linewidth=0,
                    padding=0,
                    background=colors[0]
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground=colors[1],
                    padding=0,
                    fontsize=60
                ),

                widget.Clock(
                    foreground=colors[26],
                    background=colors[0],
                    format='%d/%m/%y %I:%M%p',
                    padding=0,
                    fontsize=14,
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    background=colors[0],
                    foreground=colors[1],
                    padding=-8,
                    fontsize=60
                ),

                widget.TextBox(
                    text='⏻ ',
                    background=colors[0],
                    foreground=colors[26],
                    padding=5,
                    fontsize=17,
                    mouse_callbacks={'Button1': lazy.spawn('/home/xrito/.config/qtile/scripts/powermenu.sh')},
                ),


            ]
    return widgets_list

widgets_list = init_widgets_list()

"""
---------
|Screens|
---------
"""
def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=27, opacity=1))
            #Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), size=25, opacity=0.95))
        ]
screens = init_screens()


"""
---------
|Screens|
---------
"""
# MOUSE CONFIGURATION
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list



"""
-----------------
|Floating Layout|
-----------------
"""

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

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"

"""
--------------
|Startup_once|
--------------
"""

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('/home/xrito/.config/qtile/scripts/conky.sh')
    subprocess.Popen([home])

# In your Qtile config.py


#@hook.subscribe.startup_once
#def autostart(qtile):
#    # Function to spawn Firefox in a specific workspace
#    def spawn_firefox_in_workspace(qtile, workspace):
#        qtile.spawn("firefox")
#        qtile.group["3"].toscreen()  # Move Firefox to workspace 3
#
#    # Example: Start Firefox in workspace 3
#    #spawn_firefox_in_workspace(qtile, 3)
#
#    # You can add more applications or configurations here
#
#
#@hook.subscribe.startup_once
#def autostart(qtile):
#    # Function to spawn Firefox in a specific workspace
#    def spawn_firefox_in_workspace(qtile, workspace):
#        qtile.spawn("dev.vencord.Vesktop")
#        qtile.group["9"].toscreen()  # Move Firefox to workspace 3
#
#    # Example: Start Firefox in workspace 3
#    #spawn_dev.vencord.Vesktop_in_workspace(qtile, 9)
#
#   # You can add more applications or configurations here
#
#
#@hook.subscribe.startup_once
#def autostart(qtile):
#    # Function to spawn Firefox in a specific workspace
#    def spawn_firefox_in_workspace(qtile, workspace):
#        qtile.spawn("kitty")
#        qtile.group["1"].toscreen()  # Move Firefox to workspace 3
#
#    # Example: Start Firefox in workspace 3
#    #spawn_kitty_in_workspace(qtile, 2)
#
#    # You can add more applications or configurations here
#
