# -*- coding: utf-8 -*-

# Written by: SantaSpeen
# (c) SantaSpeen 2022

from _typeshed import SupportsWrite
from builtins import function
import logging
from typing import AnyStr


class Console(object):

    def __init__(self,
                 prompt_in: str = ">",
                 prompt_out: str = "]:",
                 not_found: str = "Command \"%s\" not found in alias.",
                 file: SupportsWrite[str] or None = Console,
                 debug: bool = False) -> None:

        self.__log: logging = None
        self.__prompt_out: str = None

    def __getitem__(self, item): ...
    @property
    def alias(self) -> dict: ...
    def add(self, key: str, func: function) -> dict: ...
    def log(self, s: AnyStr, r='\r') -> None: ...
    def write(self, s: AnyStr, r='\r') -> None: ...
    def logger_hook(self) -> None: ...
    def builtins_hook(self) -> None: ...
    def run(self) -> None: ...
    def run_while(self, whl) -> None:...
