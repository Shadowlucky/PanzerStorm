import pygame

FPS = 60
W = 700  # ширина экрана
H = 300  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
x = W // 2
y = H // 2
r = 50

while 1:
    sc.fill(WHITE)

    pygame.draw.circle(sc, BLUE, (x, y), r)

    pygame.display.update()
    abuttons = pygame.key.get_pressed()
    if abuttons[pygame.K_UP]:
        x -= 10
    if abuttons[pygame.K_DOWN]:
        x += 10
    if abuttons[pygame.K_LEFT]:
        y -= 10
    if abuttons[pygame.K_RIGHT]:
        y += 10
    clock.tick(FPS)
    pygame.event.pump()
