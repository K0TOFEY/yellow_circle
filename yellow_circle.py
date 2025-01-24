import pygame
import random as rd

if __name__ == '__main__':
    pygame.init()

    pygame.display.set_caption('Жёлтый круг')
    size = width, height = rd.randint(200, 800), rd.randint(200, 600)
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    fl = False
    pixels_sec = 10
    running = True
    while running:
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                fl = True
                r = 0
        if fl:
            pygame.draw.circle(screen, (255, 255, 0), (x, y), int(r), 0)
            r += pixels_sec * clock.tick()/1000
        pygame.display.flip()
    pygame.quit()
