# -*- coding: utf-8 -*-

# Written by: SantaSpeen
# (c) SantaSpeen 2022
import time
from typing import Type


class Engine:

    def __init__(self, x_max, y_max):
        # self.snake = []
        # self.snake_len = 1

        self.minus_fix = 2
        if Store.debug:
            self.minus_fix += 5

        self.x_max = x_max
        self.y_max = y_max - self.minus_fix

        self.frame_view_creator = self.sharp_creator
        self.frame_view_pause = self.with_phrase_creator

        self.frame_all_counter = 0
        self.frame_all_start_time = Store.start_time

        self.frame_last_counter = 0
        self.frame_last_start_time = 0
        self.frame_last_game_status = None

        self.new_frame()

        Store.game_score = 0

        print(Store.colors_reset + Store.font_white + Store.back_black)

    @staticmethod
    def work_time(from_w, _cls: Type[int] or Type[float] = int) -> int or float:
        return _cls(time.time() - from_w)

    def new_frame(self):
        self.frame_last_counter = 0
        self.frame_last_start_time = time.time()
        self.frame_last_game_status = Store.game_status

    @staticmethod
    def sharp_creator(cls, *ignore, **ignore1):
        frame = ""
        for _ in range(0, cls.y_max):
            frame += "#" * cls.x_max

        return frame

    @staticmethod
    def with_phrase_creator(cls, *, phase='paused. Press Enter to play'):

        frame = phase + (" " * (cls.x_max - len(phase)))
        for _ in range(0, cls.y_max - 1):
            frame += " " * cls.x_max

        return frame

    def get_fixed_terminal_size(self):
        x, y = Store.terminal_size()
        return x, y - self.minus_fix

    def get_center(self, string):
        half_string = len(string) / 2
        half_x = self.x_max / 2
        phrase_center = half_x - half_string
        null_text = " " * int(phrase_center)
        phrase = null_text + string + null_text
        return phrase

    def frame_topbar(self):
        return self.get_center("Score: %5s;" % Store.game_score)

    def frame_footer(self):
        return self.get_center("Playing time: %9s sec" % self.work_time(self.frame_all_start_time))

    def frame_footer_debug(self):
        x, y = self.get_fixed_terminal_size()
        return (
                "FPS: %s\n"
                "Width: %s; Height: %s; \n"
                "Frames all: %-10s Frames last: %-s\n"
                "View      : %-10s game_fps   : %-s\n"
                "Time all  : %-10s Time last  : %-s" %
                (self.frame_all_counter / self.work_time(self.frame_last_start_time, float),
                 x, y,
                 self.frame_all_counter, self.frame_last_counter,
                 Store.game_status, Store.game_fps,
                 self.frame_all_start_time, self.frame_last_start_time)
        )

    def frame_create(self, view):
        top = self.frame_topbar()

        footer = self.frame_footer()
        if Store.debug:
            footer += self.frame_footer_debug()

        frame = top + view + footer

        return frame

    def frame(self):

        if Store.game_status.startswith("error"):
            Store.game_status = "game"
        if self.get_fixed_terminal_size() != (self.x_max, self.y_max):
            Store.game_status = "error-terminal"

        if Store.game_status == self.frame_last_game_status:
            self.new_frame()

        match Store.game_status:
            case "game":
                Store.game_fps = .09
                view = self.frame_view_creator(self)
                # view = self.with_phrase_creator(self, phase=f"{self.frame_last_counter} {self.frame_last_game_status}")
            case "pause":
                Store.game_fps = Store.game_fps_pause
                view = self.frame_view_pause(self, phase="paused. Press Enter to continue. CTRL + c to exit.")
            case "error-terminal":
                Store.game_fps = Store.game_fps_pause
                Store.clear()
                x, y = self.get_fixed_terminal_size()
                view = self.with_phrase_creator(
                    self,
                    phase=f"Error: terminal_size error -> Need: x: {self.x_max}px y: {self.y_max}px. You have: x: {x}px y: {y}px"
                )
            case _:
                Store.game_fps = Store.game_fps_pause
                view = self.with_phrase_creator(self, phase="A little error...")

        self.frame_last_counter += 1

        return self.frame_create(view)

    def frame_print(self):
        print("\r" + self.frame(), end="")
        self.frame_all_counter += 1
