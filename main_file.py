# импорты
import math

import pygame
from board import Board

from main_menu import Menu_Stage
from loading_stage import Loading_Stage


# класс игры
class Game_stage(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        # параметры
        self.hg_color = pygame.Color('black')
        self.free_color = pygame.Color('gray')
        self.blue_tem = pygame.Color('blue')
        self.error_color = pygame.Color('red')
        self.playing = False
        self.time_for_map = 0

    # затычка
    def on_click(self, cell_coords):
        pass

    # отрисовка
    def render(self, screen):
        if self.playing:
            self.next_move()
        # по клеткам поля
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(
                    self.left + col * self.cell_size,
                    self.top + row * self.cell_size,
                    self.cell_size, self.cell_size
                )
                if self.time_for_map == w * h:
                    self.time_for_map = 0
                if srt_map[self.time_for_map] == '0':
                    pygame.draw.rect(screen, self.free_color, rect, 1)
                    self.time_for_map += 1
                elif srt_map[self.time_for_map] == '1':
                    pygame.draw.rect(screen, self.hg_color, rect)
                    self.time_for_map += 1
                elif srt_map[self.time_for_map] == '3':
                    pygame.draw.rect(screen, self.error_color, rect)
                    self.time_for_map += 1
                elif srt_map[self.time_for_map] == '2':
                    pygame.draw.rect(screen, self.blue_tem, rect)
                    self.time_for_map += 1
                else:
                    pygame.draw.rect(screen, self.error_color, rect)


# пункты
punkts = [(30, 300, u'Play', (250, 250, 250), (0, 0, 0), 2),
          (30, 400, u'Settings', (250, 250, 250), (0, 0, 0), 1),
          (30, 500, u'Exit', (250, 250, 250), (0, 0, 0), 0)
          ]
punkts2 = [(130, 150, u'PanzarStorm', (250, 250, 30), (250, 30, 250), 0)]

# цвета
color1 = pygame.Color('grey')
color2 = pygame.Color('black')


def point(angle):
    angle = angle % 360
    angle = angle * math.pi / 180
    x = center[0] + 70 * math.cos(angle)
    y = center[1] - 70 * math.sin(angle)
    return int(x), int(y)


# загружаем pygame
pygame.init()
# работаем с файлом карты
f = open('map_cod.txt', 'r')
w, h = list(map(int, f.readline().split()))
srt_map = f.read().strip().split(',')
# работа с фпс
clock = pygame.time.Clock()
FPS = 30
# размеры и параметры
size_for_main = width1, height1 = 1024, 600
center = (width1 // 1 - 95 + 1, height1 // 1 - 75 + 1)
size2 = width2, height2 = 600, 600
cell_size = [int(width2 / w), int(height2 / h)]
size = width, height = w * cell_size[0], h * cell_size[1]
free_color = pygame.Color('gray')
# создаём окна
screen = pygame.display.set_mode(size)
window = pygame.display.set_mode(size_for_main)
# вызываем
game = Menu_Stage(punkts)
game.menu()
load = Loading_Stage(punkts2)
load.menu()
# настраиваем доску
board = Game_stage(w, h)
board.set_view(0, 0, cell_size)
# запускаем
running = True
# основной цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = Menu_Stage(punkts)
                game.menu()
                # ToDO!!!!
                # сделать прототивное меню понял?
    # отрисовка
    screen.fill(color1)
    board.render(screen)
    pygame.display.flip()
    # работа с фпс 2
    if board.playing:
        clock.tick(FPS)
# не забываем закрыть
pygame.quit()
