import pygame
import sys

pygame.init()
win = pygame.display.set_mode((400,200))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)
# 1. 新建一个字符串变量
word = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # 2. 每按一个字母按键，将字母添加到字符串`word`中
            word += event.unicode
            # 3. 刷新屏幕，展示字符串`word`
            win.fill("black")
            text = font.render(word, True, "green")
            win.blit(text, (40, 20))

    clock.tick(60)
    pygame.display.update()