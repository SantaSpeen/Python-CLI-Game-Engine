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
    """

    match command:

        case "cli":
            Store.start_console()
            console << "Started in CLI mode!"
        case "start":
            Store.start_game()
            while True:
                time.sleep(.5)
        case _:
            print("Usage: main.py [OPTIONS] COMMAND\nTry 'main.py --help' for help.")


if __name__ == '__main__':
    core.init_core()
    game.init_game()
    main()
