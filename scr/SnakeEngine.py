from core import Engine


class SnakeEngine(Engine):

    def __init__(self, x_max, y_max):
        super().__init__(x_max, y_max)

        self.frame_view_creator = self.snake_logic

    def snake_logic(self, cls, *ignore, **ignoretoo):
        frame = ""
        for _ in range(0, cls.y_max):
            frame += "." * cls.x_max

        return frame
