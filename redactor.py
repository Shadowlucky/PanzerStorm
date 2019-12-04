import pygame
from bourd import Board

def get_cord():
    return

class Redactor(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(
                    self.left + col * self.cell_size,
                    self.top + row * self.cell_size,
                    self.cell_size, self.cell_size
                )
                if self.board[row][col] == 0:
                    pygame.draw.rect(screen, self.color, rect)
                if self.board[row][col] == 2:
                    pygame.draw.rect(screen, base_color, rect)
                if self.board[row][col] == 3:
                    pygame.draw.rect(screen, base_tem2_color, rect)


        super().render(screen)

    def on_click(self, cell_coords):
        col, row = cell_coords
        self.board[row][col] = 1 - self.board[row][col]

    def on_click2(self, cell_coords):
        col, row = cell_coords
        if self.board[row][col] == 0:
            self.board[row][col] = 2
        elif self.board[row][col] == 2:
            self.board[row][col] = 3
        elif self.board[row][col] == 3:
            self.board[row][col] = 0
        elif self.board[row][col] == 2:
            self.board[row][col] = 0



pygame.init()
# w, h = map(int, input().split())
# file = input()
w, h = 10, 10
file = 'map_cod.txt'
size = width, height = w * 20, h * 20
screen = pygame.display.set_mode(size)
back_color = pygame.Color('black')
base_color = pygame.Color('blue')
base_tem2_color = pygame.Color('red')
running = True
redactor = Redactor(w, h)
redactor.set_view(0, 0, 20)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            redactor.get_click(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            redactor.get_click2(event.pos)
        if event.type == pygame.KEYDOWN and event.key == 32:
            with open(file, 'w') as f:
                print(w, h, file=f)
                arr = []
                for row in redactor.board:
                    arr += row
                print(*arr, sep=',', file=f, end='')
        screen.fill(back_color)
        redactor.render(screen)
        pygame.display.flip()
pygame.quit()
