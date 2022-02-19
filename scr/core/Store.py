# -*- coding: utf-8 -*-

# Written by: SantaSpeen
# (c) SantaSpeen 2022

import builtins
import os
import threading


# noinspection PyShadowingBuiltins
class Store:

    debug = False
    threads = {}

    def __init__(self):
        pid = os.getpid()
        self.threads.update({"main": {"object": threading.main_thread(), "pid": pid}})
        self.items = dict()
        self.items.update({"pid": pid})

    def builtins_hook(self):
        builtins.Store = self
        return self

    def __getitem__(self, item: tuple or any):
        self.items.update(dict(item))
        return self
