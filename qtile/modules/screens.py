from libqtile import bar
from libqtile.config import Screen

from .widgets import *


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26, margin=[4, 5, 0, 5], opacity=0.8)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26, margin=[4, 5, 0, 5], opacity=0.8))]
screens = init_screens()
