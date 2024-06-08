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
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

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

"""
--------
|Colors|
--------
"""

def init_colors():
    return[["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#2bc0ad", "#2bc0ad"],
          ["#a9a1e1", "#a9a1e1"],
          ["#66b2b2", "#66b2b2"]]


colors = init_colors()


"""
--------------
|Key Bindings|
--------------
"""


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),


    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),


    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),



    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "v", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
    #Key([mod], "v", lazy.spawn("wofi --show drun"), desc="Launch Wofi"),
    Key([mod], "e", lazy.spawn(fileManager), desc="Launch Thunare"),


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


groups = [Group(i) for i in "123456789"]

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
---------
|Layouts|
---------
"""



def init_layout_theme():
    return {"margin":10,
            "border_width":1,
            "border_focus": colors[6],
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
                font="sans",
                fontsize=14,
                padding=4,
                background=colors[1])

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
                    filename="~/.config/qtile/icons/.face",
                    scale="False",
                    margin=5,
                    foreground=colors[2],
                    background=colors[0],
                    mouse_callbacks={'Button1': lazy.spawn('dmenu_run')},
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[2],
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
                    active=colors[8],
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
                    foreground=colors[8],
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
                widget.WindowName(
                    foreground=colors[8],
                    background=colors[0],
                    padding=0,
                ),
                #####
                widget.TextBox(
                    text='🖧',
                    background=colors[1],
                    foreground=colors[8],
                    padding=0,
                    fontsize=20,
                ),
                widget.Net(
                    foreground=colors[8],
                    background=colors[1],
                    format = ' {down:.0f}{down_suffix}    {up:.0f}{up_suffix}',

                ),
                #####
                widget.TextBox(
                    text='',
                    background=colors[1],
                    foreground=colors[8],
                    padding=0,
                    fontsize=40,
                ),
                widget.Sep(
                    linewidth=0,
                    padding=12,
                    background=colors[1]
                ),
                widget.Systray(
                    foreground=colors[7],
                    background=colors[1],
                    padding=12,
                    icon_size=17,
                ),
                widget.TextBox(
                    text='🔉',
                    background=colors[1],
                    foreground=colors[8],
                    padding=0,
                    fontsize=20,
                ),
                widget.Volume(
                    foreground=colors[8],
                    background=colors[1],
                    fmt='{}',
                    padding=6,
                    fontsize=12,
                ),
                widget.Sep(
                    linewidth=0,
                    padding=12,
                    background=colors[1]
                ),
                #####
                widget.TextBox(
                    text='',
                    background=colors[1],
                    foreground=colors[8],
                    padding=4,
                    fontsize=40,
                ),
                widget.ThermalSensor(
                    foreground=colors[1],
                    background=colors[8],
                    format = '  {temp:.1f}{unit} ',
                ),
                widget.Sep(
                    linewidth=0,
                    padding=12,
                    background=colors[8]
                ),
                #widget.Sep(
                 #   linewidth=0,
                  ## background=colors[8]
                #),
                #####
                widget.TextBox(
                    text='',
                    background=colors[8],
                    foreground=colors[1],
                    padding=4,
                    fontsize=40,
                ),
                widget.Clock(
                    foreground=colors[8],
                    background=colors[1],
                    format="    %d %b, %a %I:%M %p",
                    fontsize=15
                ),

                widget.TextBox(
                    text=' ⏻ ',
                    background=colors[8],
                    foreground=colors[0],
                    padding=0,
                    fontsize=15,
                ),
                widget.QuickExit(
                    foreground=colors[0],
                    background=colors[8],
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
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=30, opacity=0.85))
            #Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), size=50, opacity=0.9))
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
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Arcolinux-welcome-app.py'),
    Match(wm_class='Arcolinux-calamares-tool.py'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='archlinux-logout'),
],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/conky/qtile/01/start.sh')
    subprocess.Popen([home])

