import pygame
import os


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


def check(direct):
    if direct == 'key_top':
        sprite.rect.y -= move
        if pygame.sprite.spritecollideany(sprite, horizontal_borders):
            sprite.rect.y += move
            return False
        if pygame.sprite.spritecollideany(sprite, walls):
            sprite.rect.y += move
            return False
        return True
    elif direct == 'key_bottom':
        sprite.rect.y += move
        if pygame.sprite.spritecollideany(sprite, horizontal_borders):
            sprite.rect.y -= move
            return False
        if pygame.sprite.spritecollideany(sprite, walls):
            sprite.rect.y -= move
            return False
        return True
    elif direct == 'key_right':
        sprite.rect.x += move
        if pygame.sprite.spritecollideany(sprite, vertical_borders):
            sprite.rect.x -= move
            return False
        if pygame.sprite.spritecollideany(sprite, walls):
            sprite.rect.x -= move
            return False
        return True
    elif direct == 'key_left':
        sprite.rect.x -= move
        if pygame.sprite.spritecollideany(sprite, vertical_borders):
            sprite.rect.x += move
            return False
        if pygame.sprite.spritecollideany(sprite, walls):
            sprite.rect.x += move
            return False
        return True


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


pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
running = True
color_background = pygame.Color('black')
color_triangle = pygame.Color('yellow')
pos = 100, 250

tank_image = load_image('tank.png')
wall_image = load_image('wall.png')

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = tank_image
sprite.rect = sprite.image.get_rect()
sprite.rect.x = pos[0]
sprite.rect.y = pos[1]
all_sprites.add(sprite)

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
Border(0, 0, width, 0)
Border(0, height, width, height)
Border(0, 0, 0, height)
Border(width, 0, width, height)

walls = pygame.sprite.Group()
wall = pygame.sprite.Sprite()
wall.image = wall_image
wall.rect = wall.image.get_rect()
wall.rect.x = 50
wall.rect.y = 50
walls.add(wall)
wall = pygame.sprite.Sprite()
wall.image = wall_image
wall.rect = wall.image.get_rect()
wall.rect.x = 82
wall.rect.y = 50
walls.add(wall)
wall = pygame.sprite.Sprite()
wall.image = wall_image
wall.rect = wall.image.get_rect()
wall.rect.x = 114
wall.rect.y = 50
walls.add(wall)
wall = pygame.sprite.Sprite()
wall.image = wall_image
wall.rect = wall.image.get_rect()
wall.rect.x = 176
wall.rect.y = 50
walls.add(wall)
wall = pygame.sprite.Sprite()
wall.image = wall_image
wall.rect = wall.image.get_rect()
wall.rect.x = 208
wall.rect.y = 50
walls.add(wall)

radius = 3
move = 1
key_top, key_bottom, key_left, key_right = False, False, False, False
keys = [key_top, key_bottom, key_left, key_right]
values = {273: 'key_top', 274: 'key_bottom', 275: 'key_right', 276: 'key_left'}
values_key = {'key_top': 'y - move', 'key_bottom': 'y + move',
              'key_right': 'x + move', 'key_left': 'x - move'}
# coordinates, pos = [(100, 250), (100 + 25, 250), (100 + 25 / 2, 250 - 468.75 ** 0.5)], (100, 250)
# # / 25 = сторона тр. \ (x, y), (x + 25, y), (x + 25 / 2, y - (25 * 25 - 25/2 * 25/2) ** 0.5)

fps = 30
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
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
        if event.type == pygame.KEYUP:
            if event.key == 273:
                key_top = False
            elif event.key == 274:
                key_bottom = False
            elif event.key == 275:
                key_right = False
            elif event.key == 276:
                key_left = False
    x, y = pos
    if key_top and check('key_top'):
        sprite.rect.y -= move
        sprite.image = pygame.transform.rotate(tank_image, 0)
    if key_bottom and check('key_bottom'):
        sprite.rect.y += move
        sprite.image = pygame.transform.rotate(tank_image, 180)
    if key_right and check('key_right'):
        sprite.rect.x += move
        sprite.image = pygame.transform.rotate(tank_image, -90)
    if key_left and check('key_left'):
        sprite.rect.x -= move
        sprite.image = pygame.transform.rotate(tank_image, 90)
    pos = x, y
    screen.fill(color_background)
    all_sprites.draw(screen)
    walls.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
    keys = [key_top, key_bottom, key_left, key_right]
pygame.quit()
