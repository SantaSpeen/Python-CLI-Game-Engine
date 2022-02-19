#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Written by: SantaSpeen
# (c) SantaSpeen 2022

import time

import core
import game

import click


@click.command()
@click.argument('command', required=1)
def main(command):
    """
    CLI Python Snake game. SantaSpeen's version!

    Use command "start" to launch the game.

    start       - NORMAL\n
    startd      - DEBUG\n
    cli         - CLI Mode (alpha)
    """

    game.init_game()

    match command:

        case "cli":
            Store.start_console()
            # noinspection PyStatementEffect
            console << "Started in CLI mode!"
        case "start":
            Store.debug = False
            Store.start_game()
        case "startd":
            Store.start_game()
        case _:
            print("Usage: main.py [OPTIONS] COMMAND\nTry 'main.py --help' for help.")

    Store.clear()


if __name__ == '__main__':
    core.init_core()
    main()
