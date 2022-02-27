import random

from core import Engine, EngineFPSLock


class SnakeEngine(Engine):

    def __init__(self, x_max, y_max):
        super().__init__(x_max, y_max)

        self.random_list = [".", "#", "-", "=", "+", "1", "2", "3", "4", "5", "/", "\\", "?", "<", ">", "_"]
        self.choice = random.choice
        self.str = str()

        self.frame_view_creator = self.snake_logic

        self.fps_lock = EngineFPSLock.FPS_20

    def snake_logic(self, cls, *ignore, **ignoretoo):

        frame = self.str.join([self.choice(self.random_list) for _ in range(0, cls.y_max * cls.x_max)])
        # frame = " " * cls.y_max * cls.x_max

        # frame = str()
        # self.game_score += random.randint(0, 50)
        # for _ in range(0, cls.y_max):
        #     for _ in range(0, cls.x_max):
        #         frame += random.choice(self.random_list)

        return frame
