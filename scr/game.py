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


def get_listener() -> keyboard.Listener:
    Store.last_key = None
    return keyboard.Listener(on_press=on_press)


def start_game():
    listener = get_listener()
    listener.start()
    Store.clear()
    Store.game_fps = Store.game_fps_play
    print("Game started!")
    width, height = Store.terminal_size()
    engine = SnakeEngine(width, height)  # x_max, y_max
    Store.clear()
    while True:

        match Store.last_key:
            case 4: Store.game_status = "pause"
            case 5: Store.game_status = "game"

        time.sleep(Store.game_fps)
        engine.frame_print()


def init_game():
    Store.game_fps_play = .03955  # 20.295007664166093
    Store.game_fps_pause = .3955  # 2.5
    Store.game_status = "game"
    Store.start_game = start_game
