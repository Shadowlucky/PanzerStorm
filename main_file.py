import pygame
from bourd import Board


class Life(Board):
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


cell_size = 60
pygame.init()
f = open('map_cod.txt', 'r')
w, h = map(int, f.readline().split())
srt_map = f.read().strip().split(',')
clock = pygame.time.Clock()
fps = 1
size = width, height = w * cell_size, h * cell_size
screen = pygame.display.set_mode(size)
board = Life(w, h)
board.set_view(0, 0, cell_size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    free_color = pygame.Color('gray')
    screen.fill(free_color)
    board.render(screen)
    pygame.display.flip()
    if board.playing:
        clock.tick(fps)
pygame.quit()
