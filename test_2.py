import sys

import math
import pygame

from board import Board
# from mainfile import srt_map,  w, h

pygame.init()

clock = pygame.time.Clock()
FPS = 200
pos_tank = [100, 100]
pos_tank2 = [200, 400]
color = pygame.Color('white')


def point(angle):
    angle = angle % 360
    angle = angle * math.pi / 180
    x = pos_tank[0] + 70 * math.cos(angle)
    y = pos_tank[1] - 75 * math.sin(angle)
    return int(x), int(y)
def point2(angle):
    angle = angle % 360
    angle = angle * math.pi / 180
    x = pos_tank2[0] + 70 * math.cos(angle)
    y = pos_tank2[1] - 75 * math.sin(angle)
    return int(x), int(y)

class Game_stage(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.speed = 0

    # затычка
    def on_click(self, cell_coords):
        pass

    # отрисовка
    def render(self, screen):
        pass
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

    def menu(self, angle=90):
        done = True
        while done:
            mp = pygame.mouse.get_pos()
            screen.fill((0, 0, 0))
            # pygame.draw.polygon(screen, color, [
            #     point(angle + 45), point(angle - 45), point(angle - 135), point(angle + 135)
            # ])
            # pygame.draw.polygon(screen, color, [
            #     point2(angle + 45), point2(angle - 45), point2(angle - 135), point2(angle + 135)
            # ])
            pygame.draw.rect(screen, (255, 255, 255), (point(angle - 15), point(angle + 15)))
            pygame.display.flip()
            angle += self.speed / FPS
            for b in pygame.event.get():
                if b.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            abuttons = pygame.key.get_pressed()
            if abuttons[pygame.K_UP]:
                pos_tank[1] -= 1
            if abuttons[pygame.K_DOWN]:
                pos_tank[1] += 1
            if abuttons[pygame.K_RIGHT]:
                angle += 1
            if abuttons[pygame.K_LEFT]:
                angle -= 1
            clock.tick(FPS)
            pygame.event.pump()
            screen.blit(window, (0, 0))
            pygame.display.flip()



f = open('map_cod.txt', 'r')
w, h = list(map(int, f.readline().split()))
srt_map = f.read().strip().split(',')
size_for_main = width1, height1 = 1024, 600
size2 = width2, height2 = 600, 600
cell_size = width2 // w
cell_size2 = [int(width2 // w), int(height2 // h)]
size = width, height = cell_size2[0] * w,  cell_size2[1] * h
screen = pygame.display.set_mode(size_for_main)
window = pygame.display.set_mode(size)
game2 = Game_stage(w, h)
game2.menu()
