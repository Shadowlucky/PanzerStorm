import sys

import pygame

from настоящее.PanzarStorm_off.main_file import punkts2, color1, color2, window, screen, center, point, FPS


class Loading_Stage:
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
            pygame.draw.circle(window, color1, point(self.angle - 15), 10)
            pygame.draw.circle(window, color1, point(self.angle - 15 + 120), 10)
            pygame.draw.circle(window, color1, point(self.angle - 15 + 240), 10)
            pygame.draw.circle(window, color1, point(self.angle - 15 - 40), 9)
            pygame.draw.circle(window, color1, point(self.angle - 15 + 80), 9)
            pygame.draw.circle(window, color1, point(self.angle - 15 + 200), 9)
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
