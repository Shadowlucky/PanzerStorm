class Menu_Stage:
    def __init__(self, punkts=[120, 140, u'Punkt', color1, color2, 0]):
        # параметры
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
        font_menu = pygame.font.init()
        font_menu = pygame.font.SysFont('Metal Gear', 50)
        punkt = 0
        while done:
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 360 and mp[1] > i[1] and mp[1] < i[1] + 85:
                    punkt = i[5]
                    window.blit(self.image_bg, (0, 0))
                    pygame.draw.circle(window, color1, (i[0] + 300, i[1] + 20), 10)

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
                        pygame.draw.circle(window, color1, (punkts[0][0] + 150, punkts[0][1] + 20), 20)
                    elif punkt == 1:
                        pass
                        pygame.draw.circle(window, color1, (punkts[1][0] + 150, punkts[1][1] + 20), 20)
                    elif punkt == 0:
                        pygame.draw.circle(window, color1, (punkts[2][0] + 150, punkts[2][1] + 20), 20)
                        sys.exit()
            screen.blit(window, (0, 0))
            pygame.display.flip()