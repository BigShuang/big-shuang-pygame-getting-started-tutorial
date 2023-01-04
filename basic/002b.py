import pygame

pygame.init()
win = pygame.display.set_mode((350,350))
clock = pygame.time.Clock()

lines = [
    "I've saved the summer",
    "And I give it all to you",
    "To hold on winter mornings",
    "When the snow is new",
    "",
    "I've saved some sunlight",
    "If you should ever need",
    "A place away from darkness",
    "Where your mind can feed",
]

font = pygame.font.SysFont("Arial", 24)
# 起始的横纵坐标
sx = 50  # 开头是对齐的，所以每行的横坐标都是这个
sy = 40  # 纵向是一行一行的，每行的纵坐标都要在这个基础上做计算
for i in range(len(lines)):  # 遍历索引，以知道是哪一行
    line = lines[i]  # 通过索引取到对用的行
    text = font.render(line, True, "white")
    yi = sy + i * 30  # 计算对应的纵坐标，索引即行号，30是行高
    win.blit(text, (sx, yi))

while True:
    clock.tick(60)
    pygame.display.update()