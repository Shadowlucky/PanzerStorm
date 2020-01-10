# импорты
import os
import sys

import math
import pygame

from board import Board


def blitRotate(surf, image, pos, originPos, angle):
    # calcaulate the axis aligned bounding box of the rotated image
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

    # draw rectangle around the image


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


# цвета
grey_color = pygame.Color('grey')
black_color = pygame.Color('black')


class Menu_Stage:
    def __init__(self, punkts=None):
        # параметры
        if not punkts:
            punkts = [120, 140, u'Punkt', grey_color, black_color, 0]
        self.punkts = punkts
        self.free_color = pygame.Color('gray')
        self.image_bg = load_image('bg.png')
        window.blit(self.image_bg, (0, 0))

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
                if i[0] < mp[0] < i[0] + 360 and i[1] < mp[1] < i[1] + 85:
                    if punkt != i[5]:
                        punkt = i[5]
                        window.blit(self.image_bg, (0, 0))

                        # boom_sound.play()
                    # pygame.draw.circle(window, color1, (i[0] + 300, i[1] + 20), 10)

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
                        # pygame.time.wait(500)
                        done = False
                        # sound2.play()
                    elif punkt == 1:
                        pass
                        # sound2.play()
                    elif punkt == 0:
                        sys.exit()
            screen.blit(window, (0, 0))
            pygame.display.flip()


def point(angle):
    angle = angle % 360
    angle = angle * math.pi / 180
    x = center[0] + 60 * math.cos(angle)
    y = center[1] - 60 * math.sin(angle)
    return int(x), int(y)


class Loading_stage:
    def __init__(self, punkts2):
        # параметры
        self.punkts = punkts2
        self.free_color = pygame.Color('gray')
        self.time = 0
        self.color = pygame.Color('white')
        self.angle = 90
        self.speed = 1000
        self.bg_imm = load_image('bg_for_loading.jpg')

    # отрисовка
    def render(self, surfase, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                surfase.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surfase.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
        window.blit(self.bg_imm, (0, 0))
        pygame.draw.circle(window, grey_color, point(self.angle - 15), 10)
        pygame.draw.circle(window, grey_color, point(self.angle - 15 + 120), 10)
        pygame.draw.circle(window, grey_color, point(self.angle - 15 + 240), 10)
        pygame.draw.circle(window, grey_color, point(self.angle - 15 - 40), 9)
        pygame.draw.circle(window, grey_color, point(self.angle - 15 + 80), 9)
        pygame.draw.circle(window, grey_color, point(self.angle - 15 + 200), 9)
        pygame.display.flip()
        self.angle += self.speed / FPS

    # функция меню
    def menu(self):
        done = True
        pygame.font.init()
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
# звук
boom_sound = pygame.mixer.Sound('data/boom.wav')
# sound2 = pygame.mixer.Sound('data/one.ogg')
# pygame.mixer.music.load('data/Test.mp3')
# pygame.mixer.music.play()
# работаем с файлом карты
f = open('data/map_code.txt', 'r')
w, h = list(map(int, f.readline().split()))
srt_map = f.read().strip().split(',')
# работа с фпс
clock = pygame.time.Clock()
FPS = 30
# размеры и параметры
size_for_main = width1, height1 = 1024, 600
center = (width1 // 1 - 95 + 1, height1 // 1 - 75 + 1)
center_r = width1 // 2
center_b = height1 // 2
size2 = width2, height2 = 600, 600
cell_size = width2 // w
cell_size2 = [int(width2 // w), int(height2 // h)]
size = width, height = cell_size2[0] * w, cell_size2[1] * h
free_color = pygame.Color('gray')
punkts = [(center_r - 450, center_b, u'Play', (250, 250, 250), (0, 0, 0), 2),
          (center_r - 450, center_b + 100, u'Settings', (250, 250, 250), (0, 0, 0), 1),
          (center_r - 450, center_b + 200, u'Exit', (250, 250, 250), (0, 0, 0), 0)
          ]
punkts2 = [(130, 150, u'PanzerStorm', (250, 250, 30), (250, 30, 250), 0)]
# создаём окна
screen = pygame.display.set_mode(size_for_main)
window = pygame.display.set_mode(size_for_main)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey((255, 255, 255))
    else:
        image = image.convert_alpha()
    return image


# вызываем
game = Menu_Stage(punkts)
game.menu()
load = Loading_stage(punkts2)
load.menu()
# настраиваем доску
window = pygame.display.set_mode(size)
board = Game_stage(w, h)
board.set_view(0, 0, cell_size)
# запускаем
font = pygame.font.SysFont('Times New Roman', 50)
image = load_image('object.png', -1)
image2 = load_image('Caterpillar.png', -1)

SPEED = 1

image2.blit(image2, (1, 1))
image.blit(image, (1, 1))
w, h = image.get_size()

angle = 0
done = False
pos = [screen.get_width() / 2, screen.get_height() / 2]
while not done:
    clock.tick(60)
    screen.fill(0)
    blitRotate(screen, image2, pos, (w / 2 + 100, h / 2 + 30), angle)
    blitRotate(screen, image, pos, (w / 2, h / 2), angle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    abuttons = pygame.key.get_pressed()
    if abuttons[pygame.K_UP]:
        pos[1] -= math.cos((angle * math.pi) / 180)
        pos[0] -= math.sin((angle * math.pi) / 180)
    if abuttons[pygame.K_DOWN]:
        pos[1] += math.cos((angle * math.pi) / 180)
        pos[0] += math.sin((angle * math.pi) / 180)
    if abuttons[pygame.K_LEFT]:
        angle += 1
    if abuttons[pygame.K_RIGHT]:
        angle += -1

    pygame.display.flip()
    pygame.event.pump()

pygame.quit()
