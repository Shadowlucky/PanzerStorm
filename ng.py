import os

import pygame
import pygame.font
import math

pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


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
