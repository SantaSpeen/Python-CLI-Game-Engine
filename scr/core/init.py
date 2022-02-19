# -*- coding: utf-8 -*-

# Written by: SantaSpeen
# (c) SantaSpeen 2022

from threading import Thread

from .Console import Console
from .Store import Store
from . import tools

c: Console = None
s: Store = None


def start_console():
    global c, s
    c.builtins_hook()
    c.logger_hook()
    th = Thread(target=c.run)
    th.start()
    s.threads.update({"console": {"object": th, "pid": th.native_id}})


def init_core():
    global c, s
    c = Console(prompt_out="<:")
    s = Store().builtins_hook()
    s.builtins_hook()

    s.start_console = start_console
    s.terminal_size = tools.get_terminal_size

    return s
