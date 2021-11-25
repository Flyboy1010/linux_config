# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane

    ([mod], "Tab", lazy.layout.next()),

    # Change window sizes (MonadTall)

    ([mod], "plus", lazy.layout.grow()),
    ([mod], "minus", lazy.layout.shrink()),

    # Toggle floating

    ([mod], "f", lazy.window.toggle_floating()),
    ([mod, "shift"], "f", lazy.window.toggle_fullscreen()),

    # Move windows up or down in current stack

    ([mod, "shift"], "k", lazy.layout.shuffle_down()),
    ([mod, "shift"], "j", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    # ([mod], "Tab", lazy.next_layout()),
    # ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window

    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    # ([mod], "period", lazy.next_screen()),
    # ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile

    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu

    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav

    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser

    ([mod], "b", lazy.spawn("brave")),

    # File Explorer

    ([mod], "e", lazy.spawn("alacritty -e ranger")),

    # Terminal

    ([mod], "Return", lazy.spawn("alacritty")),

    # Screenshot
    # ([mod], "s", lazy.spawn("scrot")),
    # ([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
