import os, socket
from libqtile import qtile, widget
from libqtile.widget import Spacer
from libqtile.command import lazy

from .colors import *
from .layouts import *

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
               widget.GroupBox(font="FontAwesome",
                        fontsize = 16,
                        margin_y = -1,
                        margin_x = 0,
                        padding_y = 6,
                        padding_x = 5,
                        borderwidth = 0,
                        disable_drag = True,
                        active = colors[9],
                        inactive = colors[5],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[8],
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.CurrentLayout(
                        font = "Noto Sans Bold",
                        foreground = colors[5],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.WindowName(font="Noto Sans",
                        fontsize = 12,
                        foreground = colors[5],
                        background = colors[1],
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[3],
                        background=colors[1],
                        padding = 0,
                        fontsize=16
                        ),
               widget.Clock(
                        foreground = colors[5],
                        background = colors[1],
                        fontsize = 12,
                        format="%d-%m-%Y %H:%M"
                        ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               widget.Systray(
                        background=colors[1],
                        icon_size=20,
                        padding = 4
                        ),
              ]
    return widgets_list

widgets_list = init_widgets_list()