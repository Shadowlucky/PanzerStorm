import sys

import pygame
from board import Board


class Tanks(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.hg_color = pygame.Color('black')
        self.free_color = pygame.Color('gray')
        self.blue_tem = pygame.Color('blue')
        self.error_color = pygame.Color('red')
        self.playing = False
        self.time_for_map = 0

    def on_click(self, cell_coords):
        pass

    def render(self, screen):
        if self.playing:
            self.next_move()
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(
                    self.left + col * self.cell_size,
                    self.top + row * self.cell_size,
                    self.cell_size, self.cell_size
                )
                if self.time_for_map == 100:
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


punkts = [(130, 150, u'Играть', (250, 250, 30), (250, 30, 250), 0),
          (130, 250, u'Настройки', (250, 250, 30), (250, 30, 250), 2),
          (130, 350, u'Выход', (250, 250, 30), (250, 30, 250), 1)
          ]

color1 = pygame.Color('grey')
color2 = pygame.Color('black')


class Menu:
    def __init__(self, punkts=[120, 140, u'Punkt', color1, color2, 0]):
        self.punkts = punkts
        self.free_color = pygame.Color('gray')

    def render(self, surfase, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                surfase.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surfase.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        done = True
        font_menu = pygame.font.init()
        font_menu = pygame.font.SysFont('courier new', 66)
        punkt = 0
        while done:
            window.fill(self.free_color)
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if i[0] < mp[0] < i[0] + 155 and i[1] < mp[1] < i[1] + 50:
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
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()
            screen.blit(window, (0, 0))
            pygame.display.flip()


cell_size = 60
pygame.init()
f = open('map_cod.txt', 'r')
w, h = map(int, f.readline().split())
srt_map = f.read().strip().split(',')
clock = pygame.time.Clock()
fps = 1
size = width, height = w * cell_size, h * cell_size
size_for_main = width, height = 600, 600
screen = pygame.display.set_mode(size)
window = pygame.display.set_mode(size_for_main)
game = Menu(punkts)
game.menu()
board = Tanks(w, h)
board.set_view(0, 0, cell_size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.menu()
    free_color = pygame.Color('gray')
    screen.fill(free_color)
    board.render(screen)
    pygame.display.flip()
    if board.playing:
        clock.tick(fps)
pygame.quit()
