# -*- coding: utf-8 -*-

# Written by: SantaSpeen
# (c) SantaSpeen 2022
import time

from SnakeEngine import SnakeEngine
from pynput import keyboard


def on_press(key):

    Key = keyboard.Key

    match key:
        case Key.up:
            Store.last_key = 0
        case Key.down:
            Store.last_key = 1
        case Key.left:
            Store.last_key = 2
        case Key.right:
            Store.last_key = 3
        case Key.esc:
            Store.last_key = 4
        case Key.enter:
            Store.last_key = 5
        case _:
            Store.last_key = -1


def get_listener() -> keyboard.Listener:
    Store.last_key = None
    return keyboard.Listener(on_press=on_press)


def start_game():
    listener = get_listener()
    listener.start()
    Store.clear()
    print("Game started!")
    width, height = Store.terminal_size()
    Store.clear()
    SnakeEngine(width, height).run()  # x_max, y_max


def init_game():
    # Store.game_fps_pause = .3955  # 2.6
    Store.game_status = "game"
    Store.start_game = start_game
