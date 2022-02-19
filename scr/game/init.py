# -*- coding: utf-8 -*-

# Written by: SantaSpeen
# (c) SantaSpeen 2022
import sys
import time

from .binder import get_listener


def start_game():
    listener = get_listener()
    listener.start()
    print("Game started!")
    time.time()
    while True:
        if Store.last_key == 4:
            exit(0)
        time.sleep(.3)
        width, height = Store.terminal_size()
        background = width * height
        sys.stdout.write("\r")
        sys.stdout.write("#" * background)


def init_game():
    Store.start_game = start_game
