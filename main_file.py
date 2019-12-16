# импорты
import math
import sys

import pygame
from board import Board


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


class Menu_Stage:
    def __init__(self, punkts=[120, 140, u'Punkt', color1, color2, 0]):
        # параметры
        self.punkts = punkts
        self.free_color = pygame.Color('gray')
        bg_imm = pygame.image.load('bg.jpg')
        window.blit(bg_imm, (0, 0))

    # отрисовка
    def render(self, surfase, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                surfase.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surfase.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    # функция меню
    def menu(self):
        done = True
        font_menu = pygame.font.init()
        font_menu = pygame.font.SysFont('Metal Gear', 50)
        punkt = 0
        while done:
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 360 and mp[1] > i[1] and mp[1] < i[1] + 85:
                    punkt = i[5]
            self.render(window, font_menu, punkt)
            for b in pygame.event.get():
                if b.type == pygame.QUIT:
                    sys.exit()
                if b.type == pygame.KEYDOWN:
                    if b.key == pygame.K_UP:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                    if b.key == pygame.K_DOWN:
                        if punkt > 0:
                            punkt -= 1
                if b.type == pygame.MOUSEBUTTONDOWN and b.button == 1:
                    if punkt == 2:
                        done = False
                    elif punkt == 1:
                        pass
                    elif punkt == 0:
                        sys.exit()
            screen.blit(window, (0, 0))
            pygame.display.flip()


def point(angle):
    angle = angle % 360
    angle = angle * math.pi / 180
    x = center[0] + 70 * math.cos(angle)
    y = center[1] - 70 * math.sin(angle)
    return int(x), int(y)


def point2(angle):
    angle = angle % 360
    angle = angle * math.pi / 180
    x = center[0] + 60 * math.cos(angle)
    y = center[1] - 60 * math.sin(angle)
    return int(x), int(y)


class Loading_stage:
    def __init__(self, punkts=[120, 140, u'Punkt', color1, color2, 0]):
        # параметры
        self.punkts = punkts2
        self.free_color = pygame.Color('gray')
        self.time = 0
        self.color = pygame.Color('white')
        self.angle = 90
        self.speed = 1000
        self.bg_imm = pygame.image.load('bg_for_loading.jpg')

    # отрисовка
    def render(self, surfase, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                surfase.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surfase.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
        # for i in range(2):
        # pygame.draw.rect(window, (0, 0, 0), (150 + self.time, 500, 49, 49))
        # self.time += 50
        # if self.time == 500:
        #     self.time = 0
        for i in range(1):
            window.blit(self.bg_imm, (0, 0))
            pygame.draw.polygon(screen, (34, 0, 0), [
                center, point(self.angle + 15), point(self.angle - 15)
            ])
            pygame.draw.polygon(screen, (34, 0, 0), [
                center, point(self.angle + 15 + 120), point(self.angle - 15 + 120)
            ])
            pygame.draw.polygon(screen, (34, 0, 0), [
                center, point(self.angle + 15 + 240), point(self.angle - 15 + 240)
            ])
            pygame.draw.circle(window, color1, point2(self.angle - 15), 10)
            pygame.draw.circle(window, color1, point2(self.angle - 15 + 120), 10)
            pygame.draw.circle(window, color1, point2(self.angle - 15 + 240), 10)
            pygame.draw.circle(window, color1, point2(self.angle - 15 - 40), 9)
            pygame.draw.circle(window, color1, point2(self.angle - 15 + 80), 9)
            pygame.draw.circle(window, color1, point2(self.angle - 15 + 200), 9)
            pygame.display.flip()
            self.angle += self.speed / FPS
        # Идея: за место загрузки реализовать вентилятор

    # функция меню
    def menu(self):
        done = True
        font_menu = pygame.font.init()
        font_menu = pygame.font.SysFont('Metal Gear', 50)
        punkt = 0
        a = 0
        while done:
            self.render(window, font_menu, punkt)
            pygame.time.wait(20)
            for b in pygame.event.get():
                if b.type == pygame.QUIT:
                    sys.exit()
            screen.blit(window, (0, 0))
            pygame.display.flip()
            a += 1
            if a == 200:
                done = False


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
load = Loading_stage(punkts2)
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
