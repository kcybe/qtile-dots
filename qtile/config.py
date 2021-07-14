from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess
from libqtile import hook

## Auto Start ##
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('/home/kcybe/.config/qtile/autostart.sh')
    subprocess.call([home])

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), 
        desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "slash", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    ## Programs ##
    Key([mod, "shift"], "Print", lazy.spawn('gnome-screenshot -i')), # Opens screenshot tool
    Key([mod], "f", lazy.spawn('nautilus')), # Opens file manager
    Key([mod], "i", lazy.spawn('firefox')), # Opens browser
    
    ## Audio ##
    #  Using pacmd to change output device (audio)
    KeyChord([mod], "a", [
            Key([], "o", lazy.spawn("pacmd set-default-sink alsa_output.usb-Solid_State_System_Co._Ltd._USB_PnP_Audio_Device_000000000000-00.analog-stereo")), # Headphones
            Key([], "p", lazy.spawn("pacmd set-default-sink alsa_output.pci-0000_00_1f.3.analog-stereo")), # Speakers
    ]),

    ## Power ##
    KeyChord([mod], "p", [
            Key([], "l", lazy.spawn("kill -9 -1")), # Logout
            Key([], "s", lazy.spawn("shutdown -h 0")), # Shutdown
            Key([], "r", lazy.spawn("shutdown -r 0")), # Restart
    ]),

    ## Shortcuts ##
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."), # Change keyboard layout
]

## Colors ##
COLORS = ["fffcf9", # White Color
          "0c0f0a", # Bar Background
          "f72585", # Active
          "7209b7", # Inactive
          "3a0ca3",
          "4361ee",
          "4cc9f0",
          ]

#groups = [Group(i) for i in "123456789"]

#for i in groups:
#    keys.extend([
#        # mod1 + letter of group = switch to group
#        Key([mod], i.name, lazy.group[i.name].toscreen(),
#             desc="Switch to group {}".format(i.name)),
#
#        # mod1 + shift + letter of group = switch to & move focused window to group
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#            desc="Switch to & move focused window to group {}".format(i.name)),
#        # Or, use below if you prefer not to switch to that group.
#        # # mod1 + shift + letter of group = move focused window to group
#        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#        #     desc="move focused window to group {}".format(i.name)),
#    ])

groups = []

workspaces = [
        {"name": "١", "key": "1", "matches": [], "lay": "bsp"},
        {"name": "٢", "key": "2", "matches": [], "lay": "bsp"},
        {"name": "٣", "key": "3", "matches": [], "lay": "bsp"},
        {"name": "٤", "key": "4", "matches": [], "lay": "bsp"},
        {"name": "٥", "key": "5", "matches": [], "lay": "bsp"},
        {"name": "٦", "key": "6", "matches": [], "lay": "bsp"},
        {"name": "٧", "key": "7", "matches": [], "lay": "bsp"},
        {"name": "٨", "key": "8", "matches": [], "lay": "bsp"},
        {"name": "٩", "key": "9", "matches": [], "lay": "bsp"},
        {"name": "١٠", "key": "0", "matches": [], "lay": "bsp"},
]

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout = workspace["lay"]))
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], workspace["key"], lazy.group[workspace["name"]].toscreen(),
             desc="Switch to group {}".format(workspace["name"])),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], workspace["key"], lazy.window.togroup(workspace["name"], switch_group=True),
            desc="Switch to & move focused window to group {}".format(workspace["name"])),
])

layouts = [
    layout.Bsp(
	border_focus = COLORS[6],
        border_normal = COLORS[2],
        border_width = 2,
        margin = 25
	),
]

widget_defaults = dict(
    font='SF Pro Display',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Icons from https://fontawesome.com/v5/cheatsheet
# Install the fonts and use the icons
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 8
                    ),
                widget.GroupBox(
                    active = COLORS[6],
                    inactive = COLORS[2],
                    margin_y = None,
                    margin_x = None,
                    padding_y = 2,
                    padding_x = 5,
                    borderwidth = 2,
                    invert_mouse_wheel = True,
                    this_current_screen_border = COLORS[0],
                    highlight_method = "text"
                    ),
                widget.Prompt(foreground = COLORS[6]),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Spacer(),
                widget.WindowName(
                    width = bar.CALCULATED
                    ),
                widget.Spacer(),
                widget.Sep(
                    linewidth = 0,
                    padding = 8
                    ),
                widget.TextBox(
                    font = "Font Awesome 5 Free",
                    foreground = COLORS[2],
                    text = " "
                    ),
                widget.Mpris2(
                    name='spotify',
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_chars=None,
                    stop_pause_text='',
                    foreground = COLORS[0]
                    ),
                widget.Sep(
                    foreground = COLORS[0],
                    linewidth = 2,
                    padding = 25
                    ),
                widget.WidgetBox(
                    font = "Font Awesome 5 Free",
                    widgets=[
                                widget.Systray()
                    ],
                    text_closed = "",
                    text_open = ""
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 5
                    ),
                widget.KeyboardLayout(
                    configured_keyboards = ['us', 'il']
                    ),
                widget.Sep(
                    foreground = COLORS[0],
                    linewidth = 2,
                    padding = 25
                    ),
                widget.TextBox(
                    font = "Font Awesome 5 Free",
                    foreground = COLORS[6],
                    text = " "
                    ),
                widget.Volume(
                    foreground = COLORS[0],
                    get_volume_command = "amixer -D pulse get Master".split(),
                    volume_up_command = "amixer -q -D pulse sset Master 5%+",
                    volume_down_command = "amixer -q -D pulse sset Master 5%-",
                    mute_command = "amixer -D pulse set Master 1+ toggle"
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 8
                    ),
                widget.TextBox(
                    font = "Font Awesome 5 Free",
                    foreground = COLORS[2],
                    text = " "
                    ),
                widget.CPU(
                    format = "CPU {load_percent}%",
                    foreground = COLORS[0]
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 8
                    ),
                widget.TextBox(
                    font = "Font Awesome 5 Free",
                    foreground = COLORS[6],
                    text = " "
                    ),
                widget.Memory(
                    foreground = COLORS[0]
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 8
                    ),
                widget.TextBox(
                    font = "Font Awesome 5 Free",
                    foreground = COLORS[2],
                    text = " "
                    ),
                widget.Clock(
                    foreground = COLORS[0],
                    fontsize = 14,
                    format='%A, %B %d - %H:%M'
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 8
                    ),
            ],
            30,
            background = COLORS[1],
            margin = [12, 12, -12, 12],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
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
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
