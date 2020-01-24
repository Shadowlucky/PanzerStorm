# импорты
import os
import sys

import math
import pygame


# цвета
grey_color = pygame.Color('grey')
black_color = pygame.Color('black')
color_background = pygame.Color('black')
color_triangle = pygame.Color('yellow')
red_color = pygame.Color('red')
tank_you = None
tank_friend = None


class Menu_Stage:
    def __init__(self, punkts=None):
        # параметры
        if not punkts:
            punkts = [120, 140, u'point', grey_color, black_color, 0]
        self.points = punkts
        self.free_color = pygame.Color('gray')
        self.image_bg = load_image('bg.png')
        self.tank = load_image('tank.png')
        self.tank = pygame.transform.rotate(self.tank, 90)
        window.blit(self.image_bg, (0, 0))

    # отрисовка
    def render(self, surfase, render_font, num_point):
        for i in self.points:
            if num_point == i[5]:
                surfase.blit(render_font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surfase.blit(render_font.render(i[2], 1, i[3]), (i[0], i[1]))

    # функция меню
    def menu(self):
        done = True
        pygame.font.init()
        font_menu = pygame.font.SysFont(None, 30)
        punkt = 0
        while done:
            mp = pygame.mouse.get_pos()
            for i in self.points:
                if i[0] < mp[0] < i[0] + 360 and i[1] < mp[1] < i[1] + 85:
                    if punkt != i[5]:
                        punkt = i[5]
                        window.blit(self.image_bg, (0, 0))
                    window.blit(self.tank, (i[0] + 150, i[1]))

            self.render(window, font_menu, punkt)
            for b in pygame.event.get():
                if b.type == pygame.QUIT:
                    sys.exit()
                if b.type == pygame.KEYDOWN:
                    if b.key == pygame.K_UP:
                        if punkt < len(self.points) - 1:
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
    x = center[0] + 60 * math.cos(angle)
    y = center[1] - 60 * math.sin(angle)
    return int(x), int(y)


class Loading_stage:
    def __init__(self, punkts2):
        # параметры
        self.points = punkts2
        self.free_color = pygame.Color('gray')
        self.time = 0
        self.color = pygame.Color('white')
        self.angle = 90
        self.speed = 1000

    # отрисовка
    def render(self, surfase, render_font, num_point):
        for i in self.points:
            if num_point == i[5]:
                surfase.blit(render_font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surfase.blit(render_font.render(i[2], 1, i[3]), (i[0], i[1]))
        window.fill((0, 0, 0))
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
        super().__init__(group_borders)
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


class Bullet(pygame.sprite.Sprite):
    translate = {0: [(10, 0), 'top', (0, -2)], 180: [(10, 26), 'bottom', (0, 2)],
                 90: [(0, 10), 'left', (-2, 0)], -90: [(26, 10), 'right', (2, 0)]}

    def __init__(self, group_sprites, coord, tank_player):
        super().__init__(group_sprites)
        x, y = Bullet.translate[tank_player.angle][0]
        self.coord = Bullet.translate[tank_player.angle][2]
        self.image = pygame.transform.rotate(bullet_image, tank_player.angle)
        self.rect = self.image.get_rect()
        self.rect.x = coord[0] + x
        self.rect.y = coord[1] + y
        self.info = Bullet.translate[tank_player.angle][1]
        self.tank = tank_player

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
                    wall.state = [2, self.info, opposite[self.info]]
                    wall.image = load_image('2_' + self.info + '.png')
                    if self.info == 'top':
                        wall.rect = wall.rect.x, wall.rect.y, 16, 8
                    if self.info == 'bottom':
                        wall.rect = wall.rect.x, wall.rect.y + 8, 16, 8
                    if self.info == 'right':
                        wall.rect = wall.rect.x + 8, wall.rect.y, 8, 16
                    if self.info == 'left':
                        wall.rect = wall.rect.x, wall.rect.y, 8, 16
                elif wall.state[0] == 2:
                    if self.info in wall.state:
                        wall.kill()
                        continue
                    elif self.info == 'top':
                        if wall.state[1] == 'left':
                            wall.image = load_image('14.png')
                            wall.rect = (wall.rect[0], wall.rect[1], 8, 8)
                        elif wall.state[1] == 'right':
                            wall.image = load_image('23.png')
                            wall.rect = (wall.rect[0], wall.rect[1], 8, 8)
                    elif self.info == 'bottom':
                        if wall.state[1] == 'left':
                            wall.image = load_image('23.png')
                            wall.rect = (wall.rect[0], wall.rect[1] + 8, 8, 8)
                        elif wall.state[1] == 'right':
                            wall.image = load_image('14.png')
                            wall.rect = (wall.rect[0], wall.rect[1] + 8, 8, 8)
                    elif self.info == 'right':
                        if wall.state[1] == 'top':
                            wall.image = load_image('23.png')
                            wall.rect = (wall.rect[0] + 8, wall.rect[1], 8, 8)
                        elif wall.state[1] == 'bottom':
                            wall.image = load_image('14.png')
                            wall.rect = (wall.rect[0] + 8, wall.rect[1], 8, 8)
                    elif self.info == 'left':
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
        if pygame.sprite.spritecollideany(self, group_tank):
            for sprite in pygame.sprite.spritecollide(self, group_tank, False):
                if sprite is not self.tank:
                    sprite.kill()
                    self.kill()


class Tank(pygame.sprite.Sprite):
    def __init__(self, group_sprites, coord, image, player):
        super().__init__(group_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]
        self.angle = 0
        self.player = player

    def move(self, move_x, move_y, angle, image):
        self.image = pygame.transform.rotate(image, angle)
        self.angle = angle
        if self.check(move_x, move_y):
            self.rect.x += move_x
            self.rect.y += move_y

    def check(self, move_x, move_y):
        self.rect.x += move_x
        self.rect.y += move_y
        if pygame.sprite.spritecollideany(self, horizontal_borders) or \
                pygame.sprite.spritecollideany(self, vertical_borders) or \
                pygame.sprite.spritecollideany(self, group_wall) or \
                pygame.sprite.spritecollideany(self, group_wall_hard) or \
                len(pygame.sprite.spritecollide(self, group_tank, False)) > 1:
            self.rect.x -= move_x
            self.rect.y -= move_y
            return False
        self.rect.x -= move_x
        self.rect.y -= move_y
        return True

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
size_for_main = width1, height1 = 600, 600
center = (300, 300)
center_r = width1 // 2
center_b = height1 // 2
size2 = width2, height2 = 600, 600
cell_size = width2 // w1
cell_size2 = [int(width2 // w1), int(height2 // h1)]
free_color = pygame.Color('gray')
points = [(200, center_b, u'Играть', (250, 250, 250), red_color, 2),
          (200, center_b + 50, u'Выбор карты', (250, 250, 250), red_color, 1),
          (200, center_b + 100, u'Выход', (250, 250, 250), red_color, 0)
          ]
points2 = [(130, 150, u'', (250, 250, 30), (250, 30, 250), 0)]
# создаём окна
screen = pygame.display.set_mode(size_for_main)
window = pygame.display.set_mode(size_for_main)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        image.set_colorkey((255, 255, 255))
    else:
        image = image.convert_alpha()
    return image


# вызываем
game = Menu_Stage(points)
game.menu()
load = Loading_stage(points2)
load.menu()
# настраиваем доску
pygame.display.set_mode((320, 320))
# запускаем
all_sprites = pygame.sprite.Group()
font = pygame.font.SysFont('Times New Roman', 50)
direct_for_bullet = 11, 0
pos = 100, 150
info = [(10, 0), (0, -2), 0, 'top']
info2 = [(10, 0), (0, -2), 0, 'top']
opposite = {'left': 'right', 'right': 'left', 'top': 'bottom', 'bottom': 'top'}
start_position = [(None, None), (None, None)]

tank_image_you = load_image('tank.png', -1)
tank_image_friend = load_image('tank2.png', -1)
wall_image = load_image('wall2.png')
bullet_image = load_image('bullet.png', -1)
wall_hard_image = load_image('wall_hard.png')

group_bullet = pygame.sprite.Group()
group_bullet2 = pygame.sprite.Group()
group_tank = pygame.sprite.Group()
group_borders = pygame.sprite.Group()
group_wall_hard = pygame.sprite.Group()
group_wall = pygame.sprite.Group()
for row in range(20):
    for col in range(20):
        if list_wall[col][row] == 1:
            Wall(group_wall, 16 * row, 16 * col)
        elif list_wall[col][row] == 2:
            tank_friend = Tank(group_tank, (16 * row + 3, 16 * col + 3), tank_image_friend, 2)
            start_position[1] = (16 * row + 3, 16 * col + 3)
        elif list_wall[col][row] == 3:
            tank_you = Tank(group_tank, (16 * row + 3, 16 * col + 3), tank_image_you, 1)
            start_position[0] = (16 * row + 3, 16 * col + 3)
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
    button_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN and event.key == 13:
            if not group_bullet:
                Bullet(group_bullet, tank_you.get_coord(), tank_you)
        if event.type == pygame.KEYDOWN and event.key == 32:
            if not group_bullet2:
                Bullet(group_bullet2, tank_friend.get_coord(), tank_friend)
    if button_pressed[pygame.K_UP]:
        tank_you.move(0, -move, 0, tank_image_you)
    elif button_pressed[pygame.K_DOWN]:
        tank_you.move(0, move, 180, tank_image_you)
    elif button_pressed[pygame.K_RIGHT]:
        tank_you.move(move, 0, -90, tank_image_you)
    elif button_pressed[pygame.K_LEFT]:
        tank_you.move(-move, 0, 90, tank_image_you)
    if button_pressed[pygame.K_w]:
        tank_friend.move(0, -move, 0, tank_image_friend)
    elif button_pressed[pygame.K_s]:
        tank_friend.move(0, move, 180, tank_image_friend)
    elif button_pressed[pygame.K_d]:
        tank_friend.move(move, 0, -90, tank_image_friend)
    elif button_pressed[pygame.K_a]:
        tank_friend.move(-move, 0, 90, tank_image_friend)
    if running:
        screen.fill(pygame.color.Color('black'))
        group_tank.draw(screen)
        group_wall.draw(screen)
        group_bullet.draw(screen)
        group_bullet.update()
        group_bullet2.draw(screen)
        group_bullet2.update()
        group_wall_hard.draw(screen)
        pygame.display.flip()
    clock.tick(fps)
    if len(group_tank) < 2:
        for tank in group_tank:
            if tank.player == 1:
                tank_friend = Tank(group_tank, start_position[1], tank_image_friend, 2)
            elif tank.player == 2:
                tank_you = Tank(group_tank, start_position[0], tank_image_you, 1)
    if len(group_tank) == 0:
        tank_you = Tank(group_tank, start_position[0], tank_image_you, 1)
        tank_friend = Tank(group_tank, start_position[1], tank_image_friend, 2)
pygame.quit()
