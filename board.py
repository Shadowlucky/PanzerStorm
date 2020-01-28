import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 32
        self.top = 32
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

    # возвращает координаты клетки в виде кортежа
    def get_cell(self, mouse_pos):
        col = (mouse_pos[0] - self.left) // self.cell_size
        row = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= col < self.width and 0 <= row < self.height:
            return col, row
