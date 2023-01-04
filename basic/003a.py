import pygame
import sys

pygame.init()
win = pygame.display.set_mode((400,200))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 判断当前事件是否为点击右上角退出键
            pygame.quit()
            sys.exit()  # 需要提前 import sys

        if event.type == pygame.KEYDOWN:
            win.fill("black")
            text = font.render(event.unicode, True, "green")
            win.blit(text, (40, 20))

    clock.tick(60)
    pygame.display.update()