# -*- coding: utf-8 -*-

# Written by: SantaSpeen
# (c) SantaSpeen 2022
import sys
import time
from enum import Enum
from typing import Type, Tuple


# noinspection PyUnusedLocal
def sharp_creator(cls, *ignore, **ignoretoo) -> str:
    frame = ""
    for _ in range(0, cls.y_max):
        frame += "#" * cls.x_max

    return frame


# noinspection PyUnusedLocal
def with_phrase_creator(cls, *, phase: str = 'paused. Press Enter to play', **ignoretoo):
    frame = phase + (" " * (cls.x_max - len(phase)))
    for _ in range(0, cls.y_max - 1):
        frame += " " * cls.x_max

    return frame


def work_time(from_w, _cls: Type[int] | Type[float] = int) -> int | float:
    w = _cls(time.time() - from_w)
    if w == 0:
        w = 1
    return w


class EngineFPSLock(Enum):
    NOLOCK = 0x0
    FPS_05 = 0x1
    FPS_10 = 0x2
    FPS_15 = 0x3
    FPS_20 = 0x4
    FPS_25 = 0x5
    FPS_30 = 0x6


class Engine:

    def __init__(self, x_max: int, y_max: int):

        self.frame_delay: int = int()
        self.play_delay: int = int()

        self.y_fix: int = 2
        if Store.debug:
            self.y_fix += 5

        self.x_max: int = x_max
        self.y_max: int = y_max - self.y_fix

        self.frame_view_creator = sharp_creator
        self.frame_view_pause = with_phrase_creator

        self.frame_all_counter: int = int()
        self.frame_all_start_time: float = Store.start_time

        self.frame_last_counter: int = int()
        self.frame_last_start_time: int = int()
        self.frame_last_game_status: str = str()

        self.new_frame()

        self.game_score = 0

        self.fps_lock = EngineFPSLock.NOLOCK
        self.fps_lock_pause = .3955

        print(Store.colors_reset + Store.font_white + Store.back_black)

    def new_frame(self) -> None:
        self.frame_last_counter = int()
        self.frame_last_start_time = time.time()
        self.frame_last_game_status = Store.game_status

    def get_fixed_terminal_size(self) -> Tuple[int, int]:
        x, y = Store.terminal_size()
        return x, y - self.y_fix

    def get_center(self, string: str) -> str:
        half_string = len(string) / 2
        half_x = self.x_max / 2
        phrase_center = half_x - half_string
        null_text = " " * int(phrase_center)
        phrase = null_text + string
        return phrase

    def frame_footer_debug(self) -> str:
        x, y = self.get_fixed_terminal_size()
        return (
                "\nframe_delay: %-10s FPS        : %-10s\n"
                "Width      : %-10s Height     : %-10s Valid: %-10s Width lock: %-10s Height lock: %-10s \n"
                "Frames all : %-10s Frames last: %-10s\n"
                "View       : %-10s View last  : %-10s Valid: %-s\n"
                "Time all   : %-30s Time last: %-s" %
                (self.frame_delay, self.frame_last_counter / work_time(self.frame_last_start_time, float),
                 x, y, (x, y) == (self.x_max, self.y_max), self.x_max, self.y_max,
                 self.frame_all_counter, self.frame_last_counter,
                 Store.game_status, self.frame_last_game_status, Store.game_status == self.frame_last_game_status,
                 self.frame_all_start_time, self.frame_last_start_time)
        )

    def frame_topbar(self) -> str:
        return self.get_center("Score: %6s;\n" % self.game_score)

    def frame_footer(self) -> str:
        return self.get_center("Playing time: %10s sec" % work_time(self.frame_all_start_time))

    def frame_create(self, view: str) -> str:
        top = self.frame_topbar()

        footer = self.frame_footer()
        if Store.debug:
            footer += self.frame_footer_debug()

        frame = top + view + footer

        return frame

    def frame(self) -> str:

        if Store.game_status.startswith("error"):
            Store.game_status = "game"

        if self.get_fixed_terminal_size() != (self.x_max, self.y_max):
            Store.game_status = "error-terminal"

        if Store.game_status != self.frame_last_game_status:
            self.new_frame()

        match Store.game_status:
            case "game":
                self.frame_delay = self.play_delay
                view = self.frame_view_creator(self)
                # view = self.with_phrase_creator(self, phase=f"{self.frame_last_counter} {self.frame_last_game_status}")
            case "pause":
                self.frame_delay = self.fps_lock_pause
                view = self.frame_view_pause(self, phase="paused. Press Enter to continue. CTRL + c to exit.")
            case "error-terminal":
                self.frame_delay = self.fps_lock_pause
                # Store.clear()
                x, y = self.get_fixed_terminal_size()
                view = with_phrase_creator(
                    self,
                    phase=f"Error: terminal_size error -> Need: x: {self.x_max}px y: {self.y_max}px. You have: x: {x}px y: {y}px"
                )
            case _:
                self.play_delay = Store.game_fps_pause
                view = with_phrase_creator(self, phase="A little error...")

        self.frame_last_counter += 1
        return self.frame_create(view)

    def frame_print(self) -> None:
        sys.stdout.write("\n\r" + self.frame())
        self.frame_all_counter += 1

    def run(self, fps_lock: EngineFPSLock | None = None) -> None:
        """
                def run(self, fps_lock: EngineFPSLock = None) -> None:
        :param fps_lock: A ver from enum EngineFPSLock; If none used self.fps_lock. By default, self.fps_lock = EngineFPSLock.NOLOCK
        :return: None
        """
        
        if fps_lock is not None:
            self.fps_lock = fps_lock

        match self.fps_lock:
            case EngineFPSLock.NOLOCK:
                self.play_delay = 0
            case EngineFPSLock.FPS_05:
                self.play_delay = .19
            case EngineFPSLock.FPS_10:
                self.play_delay = .092
            case EngineFPSLock.FPS_15:
                self.play_delay = .059
            case EngineFPSLock.FPS_20:
                self.play_delay = .0424
            case EngineFPSLock.FPS_25:
                self.play_delay = .033
            case EngineFPSLock.FPS_30:
                self.play_delay = .0267

        self.frame_delay = self.play_delay

        while True:

            time.sleep(self.frame_delay)

            match Store.last_key:
                case 4:
                    Store.game_status = "pause"
                case 5:
                    Store.game_status = "game"

            self.frame_print()
