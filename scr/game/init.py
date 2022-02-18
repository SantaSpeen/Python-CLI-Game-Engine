# -*- coding: utf-8 -*-

# Written by: SantaSpeen
# (c) SantaSpeen 2022

from .binder import get_listener


def start_game():
    listener = get_listener()
    print("Game started!")
    listener.start()


def init_game():
    Store.start_game = start_game
