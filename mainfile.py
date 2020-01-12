# импорты
import os
import sys

import math
import pygame

from board import Board


# Поворот танка
def blitRotate(surf, image, pos, originPos, angle):
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    pivot = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] -
              max_box[1] + pivot_move[1])
    rotated_image = pygame.transform.rotate(image, angle)
    surf.blit(rotated_image, origin)


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
                if self.time_for_map == w1 * h1:
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
color_background = pygame.Color('black')
color_triangle = pygame.Color('yellow')


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
        pygame.font.init()
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


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, num_sp):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 1
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.image = pygame.transform.scale(self.image, (cell_size - 1, cell_size - 1))
        self.num_image = self.frames[num_sp]
        self.num_image = pygame.transform.scale(self.num_image, (cell_size, cell_size))

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, posish):
        if self.cur_frame > 7:
            self.cur_frame = 1
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        if posish == 0:
            self.image = self.frames[self.cur_frame]
            self.image = pygame.transform.rotate(self.image, 0)
            self.image = pygame.transform.scale(self.image, (cell_size - 1, cell_size - 1))
        elif posish == 1:
            self.image = self.frames[self.cur_frame]
            self.image = pygame.transform.rotate(self.image, 180)
            self.image = pygame.transform.scale(self.image, (cell_size - 1, cell_size - 1))
        elif posish == 2:
            self.image = self.frames[self.cur_frame]
            self.image = pygame.transform.rotate(self.image, 90)
            self.image = pygame.transform.scale(self.image, (cell_size - 1, cell_size - 1))
        elif posish == 3:
            self.image = self.frames[self.cur_frame]
            self.image = pygame.transform.rotate(self.image, 270)
            self.image = pygame.transform.scale(self.image, (cell_size - 1, cell_size - 1))


# загружаем pygame
pygame.init()
# звук
boom_sound = pygame.mixer.Sound('data/boom.wav')
# sound2 = pygame.mixer.Sound('data/one.ogg')
# pygame.mixer.music.load('data/Test.mp3')
# pygame.mixer.music.play()
# работаем с файлом карты
f = open('data/map_code.txt', 'r')
w1, h1 = list(map(int, f.readline().split()))
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
cell_size = width2 // w1
cell_size2 = [int(width2 // w1), int(height2 // h1)]
size = width, height = cell_size2[0] * w1, cell_size2[1] * h1
free_color = pygame.Color('gray')
punkts = [(center_r - 450, center_b, u'Play', (250, 250, 250), (0, 0, 0), 2),
          (center_r - 450, center_b + 100, u'Settings', (250, 250, 250), (0, 0, 0), 1),
          (center_r - 450, center_b + 200, u'Exit', (250, 250, 250), (0, 0, 0), 0)
          ]
punkts2 = [(130, 150, u'PanzerStorm', (250, 250, 30), (250, 30, 250), 0)]
# создаём окна
screen = pygame.display.set_mode(size_for_main)
window = pygame.display.set_mode(size_for_main)

class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


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
# game = Menu_Stage(punkts)
# game.menu()
# load = Loading_stage(punkts2)
# load.menu()
# настраиваем доску
window = pygame.display.set_mode(size)
board = Game_stage(w1, h1)
board.set_view(0, 0, cell_size)
# запускаем
all_sprites = pygame.sprite.Group()
font = pygame.font.SysFont('Times New Roman', 50)

move = 1
key_top, key_bottom, key_left, key_right = False, False, False, False
keys = [key_top, key_bottom, key_left, key_right]
values = {273: 'key_top', 274: 'key_bottom', 275: 'key_right', 276: 'key_left'}
values_key = {'key_top': 'y - move', 'key_bottom': 'y + move',
              'key_right': 'x + move', 'key_left': 'x - move'}

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
Border(0, 0, width, 0)
Border(0, height, width, height)
Border(0, 0, 0, height)
Border(width, 0, width, height)

walls = pygame.sprite.Group()
wall = pygame.sprite.Sprite()
wall.image = AnimatedSprite(load_image("kadr_tank.png", -1), 8, 4, 84, 84, 0).num_image
wall.rect = wall.image.get_rect()
wall.rect.x = 50
wall.rect.y = 50
walls.add(wall)
wall = pygame.sprite.Sprite()
wall.image = AnimatedSprite(load_image("kadr_tank.png", -1), 8, 4, 84, 84, 0).num_image
wall.rect = wall.image.get_rect()
wall.rect.x = 82
wall.rect.y = 50
walls.add(wall)
wall = pygame.sprite.Sprite()
wall.image = AnimatedSprite(load_image("kadr_tank.png", -1), 8, 4, 84, 84, 0).num_image
wall.rect = wall.image.get_rect()
wall.rect.x = 114
wall.rect.y = 50
walls.add(wall)
wall = pygame.sprite.Sprite()
wall.image = AnimatedSprite(load_image("kadr_tank.png", -1), 8, 4, 84, 84, 0).num_image
wall.rect = wall.image.get_rect()
wall.rect.x = 176
wall.rect.y = 50
walls.add(wall)
wall = pygame.sprite.Sprite()
wall.image = AnimatedSprite(load_image("kadr_tank.png", -1), 8, 4, 84, 84, 0).num_image
wall.rect = wall.image.get_rect()
wall.rect.x = 208
wall.rect.y = 50
walls.add(wall)

done = False
fps = 30
count_frames = 2
rect = AnimatedSprite(load_image("kadr_tank.png", -1), 8, 4, 84, 84, 0).rect

while not done:
    clock.tick(60)
    screen.fill(0)
    board.render(screen)
    abuttons = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if abuttons[pygame.K_UP]:
        rect[1] += -1
        count_frames += 1
        if count_frames % 6 == 0:
            all_sprites.update(0)
    elif abuttons[pygame.K_DOWN]:
        rect[1] += 1
        count_frames -= 1
        if count_frames % 6 == 0:
            all_sprites.update(1)
    elif abuttons[pygame.K_LEFT]:
        rect[0] -= 1
        count_frames += 1
        if count_frames % 6 == 0:
            all_sprites.update(2)
    elif abuttons[pygame.K_RIGHT]:
        rect[0] += 1
        count_frames += 1
        if count_frames % 6 == 0:
            all_sprites.update(3)
    elif abuttons[pygame.KMOD_LSHIFT]:
        print(1)
        pass
    all_sprites.draw(screen)
    walls.draw(screen)
    pygame.display.flip()
    pygame.event.pump()

pygame.quit()
