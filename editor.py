import os

import pygame

from board import Board


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def get_cord():
    return


class Editor(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(
                    self.left + col * self.cell_size,
                    self.top + row * self.cell_size,
                    self.cell_size, self.cell_size
                )
                if self.board[row][col] == 0:
                    pygame.draw.rect(screen, self.color, rect)
                if self.board[row][col] == 1:
                    screen.blit(image, rect)
                if self.board[row][col] == 2:
                    pygame.draw.rect(screen, base_color, rect)
                if self.board[row][col] == 3:
                    pygame.draw.rect(screen, base_tem2_color, rect)
        super().render(screen)

    def on_click(self, cell_coords):
        col, row = cell_coords
        if self.board[row][col] == 0:
            self.board[row][col] = 1

    def clear_field(self, cell_coords):
        col, row = cell_coords
        if self.board[row][col] == 0:
            self.board[row][col] = 1

    def on_click2(self, cell_coords):
        col, row = cell_coords
        if self.board[row][col] == 0:
            self.board[row][col] = 2
        elif self.board[row][col] == 2:
            self.board[row][col] = 3
        elif self.board[row][col] == 3:
            self.board[row][col] = 2

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def get_click2(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click2(cell)

    def get_click3(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.board[cell[1]][cell[0]] = 0


pygame.init()
# w, h = map(int, input().split())
# file = input()
w = h = 20  # Размер карты(всегда квадрат)
file = 'data/map_code2.txt'
size = width, height = w * 20, h * 20
screen = pygame.display.set_mode(size)
back_color = pygame.Color('black')
base_color = pygame.Color('blue')
base_tem2_color = pygame.Color('red')
image = load_image('wall.png')
x, y = -16, -16
running = True
editor = Editor(w, h)
editor.set_view(0, 0, 20)
moving = True
key = False
key2 = False
while running:
    screen.blit(image, (x, y, 100, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            key = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            key2 = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            editor.get_click2(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            if moving:
                x += event.rel[0]
                y += event.rel[1]
        if event.type == pygame.KEYDOWN and event.key == 32:
            with open(file, 'w') as f:
                print(w, h, file=f)
                arr = []
                for row in editor.board:
                    arr += row
                print(*arr, sep=',', file=f, end='')
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            key = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            key2 = False
    if key:
        editor.get_click(pygame.mouse.get_pos())
    if key2:
        editor.get_click3(pygame.mouse.get_pos())
    screen.fill(back_color)
    editor.render(screen)


pygame.quit()
