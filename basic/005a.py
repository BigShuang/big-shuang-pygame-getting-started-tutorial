import pygame
import sys

pygame.init()
win = pygame.display.set_mode((400,300))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    clock.tick(60)
    pygame.display.update()