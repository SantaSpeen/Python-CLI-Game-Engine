import random

from core import Engine


class SnakeEngine(Engine):

    def __init__(self, x_max, y_max):
        super().__init__(x_max, y_max)

        self.random_list = [".", "#", "-", "=", "+", "1", "2", "3", "4", "5", "/", "\\", "?", "<", ">", "_"]

        self.frame_view_creator = self.snake_logic

    def snake_logic(self, cls, *ignore, **ignoretoo):
        frame = str()
        self.game_score += random.randint(0, 50)
        for _ in range(0, cls.y_max):
            for _ in range(0, cls.x_max):
                frame += random.choice(self.random_list)

        return frame
