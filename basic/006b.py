import pygame
import sys

pygame.init()
win = pygame.display.set_mode((500,240))
clock = pygame.time.Clock()


# 用变量去记录数据，方便动态的计算，防止全部写数字混乱，且不好辨识与理解意义
size = 100

x1, x2, x3 = 50, 200, 350
y = 50
rect1 = pygame.Rect(x1, y, size, size)
rect2 = pygame.Rect(x2, y, size, size)
rect3 = pygame.Rect(x3, y, size, size)

c1 = 0
c2 = 0
c3 = 0
font = pygame.font.SysFont(None, 30)

while True:
    win.fill("black")

    pygame.draw.rect(win, "purple", rect1)
    pygame.draw.rect(win, "green", rect2)
    pygame.draw.rect(win, "yellow", rect3)
    t1 = font.render(str(c1), True, "purple")
    t2 = font.render(str(c2), True, "green")
    t3 = font.render(str(c3), True, "yellow")

    win.blit(t1, (x1, y + size + 30))
    win.blit(t2, (x2, y + size + 30))
    win.blit(t3, (x3, y + size + 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 判断当前事件是否为点击右上角退出键
            pygame.quit()
            sys.exit()  # 需要提前 import sys

        if event.type == pygame.MOUSEBUTTONDOWN:
            px, py = event.pos
            if x1 <= px < x1 + size and y <= py <= y +size:
                c1  += 1

            if x2 <= px < x2 + size and y <= py <= y + size:
                c2 += 1

            if x3 <= px < x3 + size and y <= py <= y +size:
                c3  += 1

    clock.tick(60)
    pygame.display.update()