# импорты
import os
import sys
import random

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
red_color = pygame.Color('red')


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


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(group_tank)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([0, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 0, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 0])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 0)


class WallHard(pygame.sprite.Sprite):
    def __init__(self, group_sprites, wall_x, wall_y):
        super().__init__(group_sprites)
        self.image = wall_hard_image
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


class Wall(pygame.sprite.Sprite):
    def __init__(self, group_sprites, wall_x, wall_y):
        super().__init__(group_sprites)
        self.image = wall_image
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.state = [4, None, None]


class Bullet2(pygame.sprite.Sprite):
    def __init__(self, group_sprites, tank_x, tank_y):
        super().__init__(group_sprites)
        x, y = info2[0]
        self.coord = info2[1]
        self.image = pygame.transform.rotate(bullet_image, info2[2])
        self.rect = self.image.get_rect()
        self.rect.x = tank_x + x
        self.rect.y = tank_y + y

    def update(self):
        self.rect.x += self.coord[0]
        self.rect.y += self.coord[1]
        if pygame.sprite.spritecollideany(self, horizontal_borders) or \
                pygame.sprite.spritecollideany(self, vertical_borders) or \
                pygame.sprite.spritecollideany(self, group_wall_hard):
            self.kill()
        if pygame.sprite.spritecollideany(self, group_wall):
            for wall in pygame.sprite.spritecollide(self, group_wall, False):
                if wall.state[0] == 4:
                    wall.state = [2, info2[3], opposite[info[3]]]
                    wall.image = load_image('2_' + info2[3] + '.png')
                    if info2[3] == 'top':
                        wall.rect = (wall.rect.x, wall.rect.y, 16, 8)
                    if info2[3] == 'bottom':
                        wall.rect = (wall.rect.x, wall.rect.y + 8, 16, 8)
                    if info2[3] == 'right':
                        wall.rect = (wall.rect.x + 8, wall.rect.y, 8, 16)
                    if info2[3] == 'left':
                        wall.rect = (wall.rect.x, wall.rect.y, 8, 16)
                elif wall.state[0] == 2:
                    if info2[3] in wall.state:
                        wall.kill()
                        continue
                    elif info2[3] == 'top':
                        if wall.state[1] == 'left':
                            wall.image = load_image('14.png')
                            wall.rect = (wall.rect[0], wall.rect[1], 8, 8)
                        elif wall.state[1] == 'right':
                            wall.image = load_image('23.png')
                            wall.rect = (wall.rect[0], wall.rect[1], 8, 8)
                    elif info2[3] == 'bottom':
                        if wall.state[1] == 'left':
                            wall.image = load_image('23.png')
                            wall.rect = (wall.rect[0], wall.rect[1] + 8, 8, 8)
                        elif wall.state[1] == 'right':
                            wall.image = load_image('14.png')
                            wall.rect = (wall.rect[0], wall.rect[1] + 8, 8, 8)
                    elif info2[3] == 'right':
                        if wall.state[1] == 'top':
                            wall.image = load_image('23.png')
                            wall.rect = (wall.rect[0] + 8, wall.rect[1], 8, 8)
                        elif wall.state[1] == 'bottom':
                            wall.image = load_image('14.png')
                            wall.rect = (wall.rect[0] + 8, wall.rect[1], 8, 8)
                    elif info2[3] == 'left':
                        if wall.state[1] == 'top':
                            wall.image = load_image('14.png')
                            wall.rect = (wall.rect[0], wall.rect[1], 8, 8)
                        elif wall.state[1] == 'bottom':
                            wall.image = load_image('23.png')
                            wall.rect = (wall.rect[0], wall.rect[1], 8, 8)
                    wall.state = [1, None, None]
                else:
                    wall.kill()
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, group_sprites, tank_x, tank_y):
        super().__init__(group_sprites)
        x, y = info[0]
        self.coord = info[1]
        self.image = pygame.transform.rotate(bullet_image, info[2])
        self.rect = self.image.get_rect()
        self.rect.x = tank_x + x
        self.rect.y = tank_y + y

    def update(self):
        self.rect.x += self.coord[0]
        self.rect.y += self.coord[1]
        if pygame.sprite.spritecollideany(self, horizontal_borders) or \
                pygame.sprite.spritecollideany(self, vertical_borders) or \
                pygame.sprite.spritecollideany(self, group_wall_hard):
            self.kill()
        if pygame.sprite.spritecollideany(self, group_wall):
            for wall in pygame.sprite.spritecollide(self, group_wall, False):
                if wall.state[0] == 4:
                    wall.state = [2, info[3], opposite[info[3]]]
                    wall.image = load_image('2_' + info[3] + '.png')
                    if info[3] == 'top':
                        wall.rect = (wall.rect.x, wall.rect.y, 16, 8)
                    if info[3] == 'bottom':
                        wall.rect = (wall.rect.x, wall.rect.y + 8, 16, 8)
                    if info[3] == 'right':
                        wall.rect = (wall.rect.x + 8, wall.rect.y, 8, 16)
                    if info[3] == 'left':
                        wall.rect = (wall.rect.x, wall.rect.y, 8, 16)
                elif wall.state[0] == 2:
                    if info[3] in wall.state:
                        wall.kill()
                        continue
                    elif info[3] == 'top':
                        if wall.state[1] == 'left':
                            wall.image = load_image('14.png')
                            wall.rect = (wall.rect[0], wall.rect[1], 8, 8)
                        elif wall.state[1] == 'right':
                            wall.image = load_image('23.png')
                            wall.rect = (wall.rect[0], wall.rect[1], 8, 8)
                    elif info[3] == 'bottom':
                        if wall.state[1] == 'left':
                            wall.image = load_image('23.png')
                            wall.rect = (wall.rect[0], wall.rect[1] + 8, 8, 8)
                        elif wall.state[1] == 'right':
                            wall.image = load_image('14.png')
                            wall.rect = (wall.rect[0], wall.rect[1] + 8, 8, 8)
                    elif info[3] == 'right':
                        if wall.state[1] == 'top':
                            wall.image = load_image('23.png')
                            wall.rect = (wall.rect[0] + 8, wall.rect[1], 8, 8)
                        elif wall.state[1] == 'bottom':
                            wall.image = load_image('14.png')
                            wall.rect = (wall.rect[0] + 8, wall.rect[1], 8, 8)
                    elif info[3] == 'left':
                        if wall.state[1] == 'top':
                            wall.image = load_image('14.png')
                            wall.rect = (wall.rect[0], wall.rect[1], 8, 8)
                        elif wall.state[1] == 'bottom':
                            wall.image = load_image('23.png')
                            wall.rect = (wall.rect[0], wall.rect[1], 8, 8)
                    wall.state = [1, None, None]
                else:
                    wall.kill()
            self.kill()


class Tank(pygame.sprite.Sprite):
    def __init__(self, group_sprites, tank_x, tank_y, image):
        super().__init__(group_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = tank_x
        self.rect.y = tank_y

    def move(self, move_x, move_y, angle, image):
        self.image = pygame.transform.rotate(image, angle)
        if self.check(move_x, move_y):
            self.rect.x += move_x
            self.rect.y += move_y

    def check(self, move_x, move_y):
        self.rect.x += move_x
        self.rect.y += move_y
        if pygame.sprite.spritecollideany(self, horizontal_borders) or \
                pygame.sprite.spritecollideany(self, vertical_borders) or \
                pygame.sprite.spritecollideany(self, group_wall) or \
                pygame.sprite.spritecollideany(self, group_wall_hard):
            self.rect.x -= move_x
            self.rect.y -= move_y
            return False
        self.rect.x -= move_x
        self.rect.y -= move_y
        return True

    def shoot(self, direct):
        pass

    def get_coord(self):
        return self.rect.x, self.rect.y


# загружаем pygame
pygame.init()
# работаем с файлом карты
with open('data/map_code.txt', 'r', encoding='utf-8') as file:
    size = width, height = [int(i[:2]) * 32 for i in file.readline().split(' ')]
    list_edit = file.readline().split(',')
    list_wall = [[int(list_edit[i]) for i in range(j * 20, (j + 1) * 20)]
                 for j in range(20)]
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


punkts_3 = [(center_r - 350, center_b, u'1 vs 1', red_color, (0, 0, 0), 1),
            (center_r + 50, center_b + 200, u'vs computer', red_color, (0, 0, 0), 0)
            ]
# вызываем
game = Menu_Stage(punkts)
game.menu()
load = Loading_stage(punkts2)
load.menu()
# chose = Chose_stage(punkts_3)
# chose.menu()
# настраиваем доску
window = pygame.display.set_mode(size)
board = Game_stage(w1, h1)
board.set_view(0, 0, cell_size)
# запускаем
all_sprites = pygame.sprite.Group()
font = pygame.font.SysFont('Times New Roman', 50)
direct_for_bullet = 11, 0
pos = 100, 150
info = [(10, 0), (0, -2), 0, 'top']
info2 = [(10, 0), (0, -2), 0, 'top']
opposite = {'left': 'right', 'right': 'left', 'top': 'bottom', 'bottom': 'top'}

tank_image = load_image('tank.png', -1)
tank_image2 = load_image('tank2.png', -1)
wall_image = load_image('wall2.png')
cust_image = load_image('cust.png', -1)
bullet_image = load_image('bullet.png', -1)
wall_hard_image = load_image('wall_hard.png')

group_bullet = pygame.sprite.Group()
group_bullet2 = pygame.sprite.Group()
group_tank = pygame.sprite.Group()
group_wall_hard = pygame.sprite.Group()
group_wall = pygame.sprite.Group()
for row in range(20):
    for col in range(20):
        if list_wall[col][row] == 1:
            Wall(group_wall, 16 * row, 16 * col)
        elif list_wall[col][row] == 2:
            tank2 = Tank(group_tank, 16 * row + 3, 16 * col + 3, tank_image2)
        elif list_wall[col][row] == 3:
            tank = Tank(group_tank, 16 * row + 3, 16 * col + 3, tank_image)

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
Border(0, 0, width, 0)
Border(0, height, width, height)
Border(0, 0, 0, height)
Border(width, 0, width, height)

radius = 3
move = 1
key_top, key_bottom, key_left, key_right = False, False, False, False
keys = [key_top, key_bottom, key_left, key_right]
key_top2, key_bottom2, key_left2, key_right2 = False, False, False, False
keys2 = [key_top2, key_bottom2, key_left2, key_right2]
values = {273: 'key_top', 274: 'key_bottom', 275: 'key_right', 276: 'key_left'}
values_key = {'key_top': 'y - move', 'key_bottom': 'y + move',
              'key_right': 'x + move', 'key_left': 'x - move'}
running = True
fps = 100
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        button_pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == 273:
                key_top, key_bottom, key_left, key_right = True, False, False, False
            elif event.key == 274:
                key_top, key_bottom, key_left, key_right = False, True, False, False
            elif event.key == 275:
                key_top, key_bottom, key_left, key_right = False, False, False, True
            elif event.key == 276:
                key_top, key_bottom, key_left, key_right = False, False, True, False
            elif event.key == 13:
                if not group_bullet:
                    Bullet(group_bullet, tank.get_coord()[0], tank.get_coord()[1])
            if event.key == 119:
                key_top2, key_bottom2, key_left2, key_right2 = True, False, False, False
            elif event.key == 115:
                key_top2, key_bottom2, key_left2, key_right2 = False, True, False, False
            elif event.key == 100:
                key_top2, key_bottom2, key_left2, key_right2 = False, False, False, True
            elif event.key == 97:
                key_top2, key_bottom2, key_left2, key_right2 = False, False, True, False
            elif event.key == 32:
                if not group_bullet2:
                    Bullet2(group_bullet2, tank2.get_coord()[0], tank2.get_coord()[1])
        if event.type == pygame.KEYUP:
            if event.key == 273:
                key_top = False
            elif event.key == 274:
                key_bottom = False
            elif event.key == 275:
                key_right = False
            elif event.key == 276:
                key_left = False
            if event.key == 119:
                key_top2 = False
            elif event.key == 115:
                key_bottom2 = False
            elif event.key == 100:
                key_right2 = False
            elif event.key == 97:
                key_left2 = False
    if key_top:
        info = [(10, 0), (0, -2), 0, 'top']
        tank.move(0, -move, 0, tank_image)
    if key_bottom:
        info = [(10, 26), (0, 2), 180, 'bottom']
        tank.move(0, move, 180, tank_image)
    if key_right:
        info = [(26, 10), (2, 0), -90, 'right']
        tank.move(move, 0, -90, tank_image)
    if key_left:
        info = [(0, 10), (-2, 0), 90, 'left']
        tank.move(-move, 0, 90, tank_image)
    if key_top2:
        info2 = [(10, 0), (0, -2), 0, 'top']
        tank2.move(0, -move, 0, tank_image2)
    if key_bottom2:
        info2 = [(10, 26), (0, 2), 180, 'bottom']
        tank2.move(0, move, 180, tank_image2)
    if key_right2:
        info2 = [(26, 10), (2, 0), -90, 'right']
        tank2.move(move, 0, -90, tank_image2)
    if key_left2:
        info2 = [(0, 10), (-2, 0), 90, 'left']
        tank2.move(-move, 0, 90, tank_image2)
    screen.fill(color_background)
    group_tank.draw(screen)
    group_wall.draw(screen)
    # group_cust.draw(screen)
    group_bullet.draw(screen)
    group_bullet.update()
    group_bullet2.draw(screen)
    group_bullet2.update()
    group_wall_hard.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
    keys = [key_top, key_bottom, key_left, key_right]
pygame.quit()
