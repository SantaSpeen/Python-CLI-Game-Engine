# -*- coding: utf-8 -*-

# Developed by Ahegao Devs
# Written by: SantaSpeen
# Version 1.1
# Licence: MIT
# (c) ahegao.ovh 2022

import builtins
import logging
import sys
import traceback
from builtins import RecursionError
from typing import AnyStr


class ConsoleIO:

    @staticmethod
    def write(s: AnyStr):
        sys.stdout.write(s)

    @staticmethod
    def write_err(s: AnyStr):
        sys.stderr.write(s)

    @staticmethod
    def read():
        return sys.stdin.readline().strip()


# noinspection PyUnusedLocal, PyShadowingBuiltins, PyUnresolvedReferences
class Console:

    def __init__(self,
                 prompt_in: str = ">",
                 prompt_out: str = "]:",
                 not_found: str = "Command \"%s\" not found in alias.",
                 file: str or None = ConsoleIO,
                 debug: bool = False) -> None:
        """
            def __init__(self,
                 prompt_in: str = ">",
                 prompt_out: str = "]:",
                 not_found: str = 'Command "%s" not found in alias.'
                 ) -> None:
        :param prompt_in:
        :param prompt_out:
        :param not_found:
        """
        self.__prompt_in = prompt_in
        self.__prompt_out = prompt_out
        self.__not_found = not_found + "\n"
        self.__is_debug = debug

        self.__print = print

        self.__file = file

        self.__alias = dict()
        self.__man = dict()

        self.add("man", self.__create_man_message, True, "man [COMMAND]")
        self.add("help", self.__create_help_message, True, "List of all available commands\n"
                                                           "--raw : View raw")

        self.is_run = False

        self.get_IO = ConsoleIO

    def __debug(self, *x):
        if self.__is_debug:
            x = list(x)
            x.insert(0, "\r CONSOLE DEBUG:")
            self.__print(*x)

    def __getitem__(self, item):

        print(item)

    def __get_max_len(self, arg) -> int:
        i = 0
        arg = list(arg)
        for a in arg:
            l = len(str(a))
            if l > i:
                i = l
        return i

    def __create_man_message(self, argv: list) -> AnyStr:
        x = argv[0]
        if x in ['']:
            return "man [COMMAND]"
        man_message = self.__man.get(x)
        if man_message:
            return man_message
        return f'man: command "{x}" not found'

    # noinspection PyStringFormat
    def __create_help_message(self, argv: list) -> AnyStr:
        """ Print help message and alias of console commands"""
        self.__debug("creating help message")
        raw = False
        if "--raw" in argv:
            max_len_v = self.__get_max_len(self.__alias.values())
            print()
            raw = True

        message = str()
        max_len = self.__get_max_len(self.__alias.keys())
        if max_len < 7:
            max_len = 7

        if not raw:
            message += f"%{max_len}s : Help message\n" % "Command"
        else:
            message += f"%-{max_len - len(self.__prompt_out)-1}s; %-{max_len_v}s; __doc__\n" % ("Key", "Object")

        for k, v in self.__alias.items():
            doc = v['f'].__doc__

            if raw:

                message += f"%-{max_len}s; %-{max_len_v}s; %s\n"  % (k, v, doc)

            else:

                if doc is None:
                    doc = " No help message found"
                message += f"   %{max_len}s :%s\n" % (k, doc)

        return message

    def __create_message(self, text, r="\r"):
        self.__debug(f"create message to output, is_run: {self.is_run}")
        text += "\n"
        if self.is_run:
            text += "\r" + self.__prompt_in + " "
        return r + self.__prompt_out + " " + text

    @property
    def alias(self) -> dict:
        """
            @property
            def alias(self) -> dict:
        :return: Copy of commands alias
        """
        return self.__alias.copy()

    def add(self, key: str, func, argv=False, man="No have manual message") -> dict:
        """
            add(key: str, func, echo=False) -> dict
        :param key: Command name. This name added to alias of commands
        :param func: Function or lambda function to run, when called key
        :param argv: If you need echo from command set as True
        :param man: Man message
        :return: Copy of commands alias
        """

        key = key.format(" ", "-")

        if not isinstance(key, str):
            raise TypeError("key must be string")
        self.__debug(f"added user command: key={key}; func={func}; echo={argv}")
        self.__alias.update({key: {"f": func, "e": argv}})
        self.__man.update({key: f'Manual for command "{key}"\n\n' + man + "\n\n"})
        return self.__alias.copy()

    def write(self, s: AnyStr, r="\r"):
        self.__file.write(self.__create_message(s, r))

    def log(self, s: AnyStr, r='\r') -> None:
        self.write(s, r)

    def __lshift__(self, s: AnyStr) -> None:
        self.write(s)

    def __builtins_print(self,
                         *values: object,
                         sep: str or None = " ",
                         end: str or None = None,
                         file: str or None = None,
                         flush: bool = False,
                         loading: bool = False) -> None:
        self.__debug(f"Used __builtins_print; is_run: {self.is_run}")
        val = list(values)
        if len(val) > 0:
            val.insert(0, "\r" + self.__prompt_out)
            if not loading:
                if self.is_run:
                    val.append("\r\n" + self.__prompt_in + " ")
                    end = "" if end is None else end
                else:
                    if end is None:
                        end = "\n"
        self.__print(*tuple(val), sep=sep, end=end, file=file, flush=flush)

    def logger_hook(self) -> None:
        """
            def logger_hook(self) -> None:
        :return: None
        """

        self.__debug("used logger_hook")

        def emit(cls, record):
            try:
                msg = cls.format(record)
                ConsoleIO.write(self.__create_message(msg))
                cls.flush()
            except RecursionError:
                raise
            except Exception:
                cls.handleError(record)

        logging.StreamHandler.emit = emit

    def builtins_hook(self) -> None:
        """
            def builtins_hook(self) -> None:
        :return: None
        """
        self.__debug("used builtins_hook")

        builtins.Console = Console
        builtins.console = self

        builtins.print = self.__builtins_print

    def run(self) -> None:
        """
            def run(self) -> None:
        :return: None
        """
        self.is_run = True
        self.run_while(True)

    def run_while(self, whl) -> None:
        """
            def run_while(self, whl) -> None:
        :param whl: run while what?
        :return: None
        """
        self.__debug(f"run while {whl}")
        while whl:
            try:
                ConsoleIO.write("\r" + self.__prompt_in + " ")
                cmd_in = ConsoleIO.read()
                cmd = cmd_in.split(" ")[0]
                if cmd == "":
                    pass
                else:
                    command_object = self.__alias.get(cmd)
                    if command_object:
                        command = command_object['f']
                        if command_object['e']:
                            argv = cmd_in[len(cmd) + 1:].split(" ")
                            output = command(argv)
                        else:
                            output = command()
                        self.log(str(output))

                    else:
                        self.log(self.__not_found % cmd)
            except Exception as e:
                ConsoleIO.write_err("\rDuring the execution of the command, an error occurred:\n\n" +
                                    str(traceback.format_exc()) +
                                    "\nType Enter to continue.")
