# 3.3.3

class ModelWindow:
    title: str
    point_left_up: list
    horizontal: int
    vertical: int
    color_window: str
    transparency: bool
    presence_frame: bool

    def __init__(self, title: str, point_left_up: list, horizontal: int, vertical: int, color_window: str,
                 transparency: bool, presence_frame: bool):
        self.title = title
        self.point_left_up = point_left_up
        self.horizontal = horizontal
        self.vertical = vertical
        self.color_window = color_window
        self.transparency = transparency
        self.presence_frame = presence_frame


    def __str__(self):
        return (f'Заголовок окна: {self.title};'
                f'Координаты левого верхнего угла: {self.point_left_up};'
                f'Размер по горизонтали: {self.horizontal};'
                f'Размер по вертикали: {self.vertical};'
                f'Цвет окна: {self.color_window};'
                f'Прозрачность окна: {self.transparency};'
                f'Наличие рамки: {self.presence_frame};')



    