# -*- coding: utf-8 -*-

# Written by: SantaSpeen
# (c) SantaSpeen 2022

import builtins
import os
import threading
import time
import colorama


# noinspection PyShadowingBuiltins
class Store:

    debug = True
    threads = {}

    def __init__(self):
        colorama.init()
        self.pid = os.getpid()
        self.start_time = time.time()
        self.threads.update({"main": {"object": threading.main_thread(), "pid": self.pid}})
        self.items = dict()
        self.items.update({"pid": self.pid})

        self.colors_reset = colorama.Style.RESET_ALL
        self.font_white = colorama.Fore.WHITE
        self.back_black = colorama.Back.BLACK

    def builtins_hook(self):
        builtins.Store = self
        return self

    def __getitem__(self, item: tuple or any):
        self.items.update(dict(item))
        return self
