from libqtile.bar import Bar
from libqtile.lazy import lazy
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.tasklist import TaskList
from libqtile.widget.battery import Battery
from libqtile.widget.textbox import TextBox
from libqtile.widget.volume import Volume



from unicodes import left_half_circle, right_arrow, left_arrow, right_half_circle

from colors import nord_fox

BAR_HEIGHT = 30

bar = Bar([
    GroupBox(
        disable_drag=True,
        active=nord_fox['magenta'],
        inactive=nord_fox['black'],
        #highlight_method='block',
        #block_highlight_text_color=nord_fox['fg_gutter'],
        block_highlight_text_color=nord_fox['cyan'],
        borderwidth=0,
        #highlight_color=nord_fox['cyan'],
        rounded=True,
        background=nord_fox['bg'],
        spacing=2,
        use_mouse_wheel=False,
        toggle=False
    ),
    left_half_circle(nord_fox['red'], nord_fox['bg']),
    CurrentLayout(
        background=nord_fox['red'],
        foreground=nord_fox['white'],
        margin=10,
    ),

    right_arrow(nord_fox['fg_gutter'], nord_fox['red']),
    WindowCount(
        text_format='缾 {num}',
        background=nord_fox['fg_gutter'],
        foreground=nord_fox['white'],
        show_zero=True,
    ),
    right_half_circle(nord_fox['fg_gutter'], nord_fox['bg']),

     TaskList(
        icon_size = 13,
        font = "JetBrainsMono Nerd Font",
        fontsize= 13,
        foreground = nord_fox['cyan'],
        background = nord_fox['bg'],
        borderwidth = 0,
        border = nord_fox['bg'],
        margin_y = -3,
        margin = 0,
        padding = 8,
        highlight_method = "block",
        title_width_method = "uniform",
        urgent_alert_method = "border",
        urgent_border = nord_fox['bg'],
        rounded = True,
        txt_floating = "🗗 ",
        txt_maximized = "🗖 ",
        txt_minimized = "🗕 ",
    ),
    # WindowName(
    #     background=nord_fox['bg'],
    #     foreground=nord_fox['fg']
    # ),

    left_half_circle(nord_fox['black'], nord_fox['bg']),
    CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=nord_fox['black'],
        foreground=nord_fox['pink']
    ),

    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=nord_fox['black'],
        foreground=nord_fox['cyan']
    ),

    Net(
        background=nord_fox['black'],
        foreground=nord_fox['green']
    ),
    # Battery(
    #     background=nord_fox['fg_gutter'],
    #     format='{char} {percent:2.0%} {hour:d}:{min:02d}'
    # ),

    left_half_circle(nord_fox['fg_gutter'], nord_fox['black']),
    Systray(
        background=nord_fox['fg_gutter'], foreground=nord_fox['black']
    ),
    right_half_circle(nord_fox['fg_gutter'], nord_fox['black']),

    Clock(
        background=nord_fox['black'],
        foreground=nord_fox['white'],
        format='  %Y-%m-%d %a %I:%M %p'
    ),
    TextBox(
        text='⏻ ',
        background=nord_fox['black'],
        foreground=nord_fox['cyan'],
        padding=5,
        fontsize=17,
        mouse_callbacks={'Button1': lazy.spawn('/home/xrito/.config/qtile/scripts/powermenu.sh')},
    ),



],
    # background=nord_fox['bg'],
    size=BAR_HEIGHT,
    margin=8,
)
