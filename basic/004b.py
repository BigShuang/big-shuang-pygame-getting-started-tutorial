import pygame
import sys

pygame.init()
win = pygame.display.set_mode((400,350))
clock = pygame.time.Clock()

win.fill("lavender")

# 绘制屋顶
points = [
    (200, 50),
    (60, 150),
    (340, 150),
]
pygame.draw.polygon(win, "black", points)

# 绘制房子主体（大矩形）
rect1 = pygame.Rect(100, 150, 200, 150)
pygame.draw.rect(win, "black", rect1, width=5)

# 绘制门（小矩形）
rect2 = pygame.Rect(180, 220, 40, 80)
pygame.draw.rect(win, "black", rect2)

# 绘制窗户
pygame.draw.circle(win, "black", (140, 200), 30, width=5)
pygame.draw.circle(win, "black", (260, 200), 30, width=5)

# 绘制地平线
start = (0, 300)
end = (400, 300)
pygame.draw.line(win, "black", start, end, width=5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    pygame.display.update()