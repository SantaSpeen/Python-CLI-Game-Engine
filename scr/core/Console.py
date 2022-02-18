# -*- coding: utf-8 -*-

# Developed by Ahegao Devs
# Written by: SantaSpeen
# (c) ahegao.ovh 2022

import builtins
import logging
import sys
from typing import AnyStr

from core.exceptions import DeprecatedMethod


class ConsoleIO:

    # @staticmethod
    # def smart_write(*values: object,
    #                 sep: str or None = " ",
    #                 end: str or None = "\n",
    #                 file: str or None = sys.stdout,
    #                 flush: bool = False):
    #     print(*values, sep=sep, end=end, file=file, flush=flush)

    @staticmethod
    def write(s: AnyStr):
        sys.stdout.write(s)

    @staticmethod
    def write_err(s: AnyStr):
        sys.stderr.write(s)

    @staticmethod
    def read():
        return sys.stdin.readline().strip()


# noinspection PyUnusedLocal PyShadowingBuiltins
class Console:

    def __init__(self,
                 prompt_in: str = ">",
                 prompt_out: str = "]:",
                 not_found: str = "Command \"%s\" not found in alias.",
                 file: str or None = None,
                 debug: bool = False) -> None:
        """
            def __init__(self,
                 prompt_in: str = ">",
                 prompt_out: str = "]:",
                 not_found: str = "Command \"%s\" not found in alias.") -> None:
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

        self.__alias = {
            "help": self.__create_help_message,
        }

    def __debug(self, *x):
        if self.__is_debug:
            x = list(x)
            x.insert(0, "\r CONSOLE DEBUG:")
            self.__print(*x)

    def __getitem__(self, item):

        raise DeprecatedMethod("Method deprecated for this project")

    @staticmethod
    def __get_max_len(arg) -> int:
        arg = list(arg)
        i = 0
        for a in arg:
            l = len(a)
            if l > i:
                i = l
        return i

    def __create_help_message(self, x) -> AnyStr:
        """Print help message and alias of console commands"""
        self.__debug("creating help message")

        max_len = self.__get_max_len(self.__alias.keys())

        message = "Help message:\n"
        for k, v in self.__alias.items():
            doc = v.__doc__
            if doc is None:
                doc = "No help message found"
            message += f"\t* %-{max_len}s : %s\n" % (k, doc)

        return message

    def __create_message(self, text, r="\r"):
        self.__debug("create message to output")
        return r + self.__prompt_out + " " + text + "\n\r" + self.__prompt_in + " "

    @property
    def alias(self) -> dict:
        """
            def alias(self) -> dict:
        :return: dict of alias
        """
        return self.__alias.copy()

    def add(self, key: str, func) -> dict:
        """
            def add(self, key: str, func) -> dict:
        :param key:
        :param func:
        :return:
        """

        if not isinstance(key, str):
            raise TypeError("key must be string")
        self.__debug(f"added user command: key={key}; func={func}")
        self.__alias.update({key: func})
        return self.__alias.copy()

    def write(self, s: AnyStr, r="\r"):
        s = s.replace("\n\t", "\n" + self.__prompt_out + "   ").replace("\t", "   ")
        ConsoleIO.write(self.__create_message(s, r))

    def log(self, s: AnyStr, r='\r') -> None:
        self.write(s, r)

    def __lshift__(self, s: AnyStr) -> None:
        self.write(s)

    def __builtins_print(self,
                         *values: object,
                         sep: str or None = " ",
                         end: str or None = "\n",
                         file: str or None = None,
                         flush: bool = False,
                         loading: bool = False) -> None:
        val = list(values)
        if len(val) > 0:
            val.insert(0, "\r" + self.__prompt_out)
            if not loading:
                val.append("\r\n" + self.__prompt_in + " ")
            end = ""
        self.__print(*tuple(val), sep=sep, end=end, file=file, flush=flush)

    def logger_hook(self) -> None:

        self.__debug("used logger_hook")

        def emit(cls, record):
            try:
                msg = cls.format(record)
                ConsoleIO.write(self.__create_message(msg))
                cls.flush()
            except RecursionError:  # See issue 36272
                raise
            except Exception:
                cls.handleError(record)

        def debug(cls, msg, *args, **kwargs):
            if cls.isEnabledFor(logging.DEBUG):
                cls._log(logging.WARNING, "DEBUG: " + msg, args, **kwargs)

        logging.StreamHandler.emit = emit
        # logging._srcfile = False
        # logging.Logger.debug = debug

        # self.__log = logging.getLogger("PyConsole")

        # self.__log.info("self.__debug", "321")

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
                    self.log("\r" + self.__prompt_in + " ")
                else:
                    do = self.__alias.get(cmd)
                    if do:
                        x = cmd_in[len(cmd) + 1:]
                        self.log(do(x) + "\n")
                    else:
                        self.log(self.__not_found % cmd)
            except Exception as e:
                ConsoleIO.write_err("\r" + str(e))


if __name__ == '__main__':
    c = Console(debug=True)
    logging.basicConfig(level=10)
    log = logging.getLogger()

    c.logger_hook()
    c.builtins_hook()

    log.warning('warning log')
    log.debug('debug log')
    log.info("info log")
    c.log("c log")
    console.log("console.log")
    console << "lshift log"
    print(c.alias)
    print("print log")
    # console.log("console.log")
