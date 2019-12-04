import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.color = pygame.Color('white')

    # настройка внешнего вида
    def set_view(self, left=10, top=10, cell_size=30):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # Отрисовка клеточного поля на холсте
    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(
                    self.left + col * self.cell_size,
                    self.top + row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )

    # Реакция поля на события мыши
    # возвращает координаты клетки в виде кортежа
    def get_cell(self, mouse_pos):
        col = (mouse_pos[0] - self.left) // self.cell_size
        row = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= col < self.width and 0 <= row < self.height:
            return col, row

    # как-то изменяет поле, опираясь на полученные координаты клетки
    def on_click(self, cell_coords):
        pass

    def on_click2(self, cell_coords):
        pass

    # получает событие нажатия и вызывает первые два метода
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def get_click2(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click2(cell)
