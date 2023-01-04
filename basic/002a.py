import pygame

pygame.init()
win = pygame.display.set_mode((400,200))
clock = pygame.time.Clock()

# 新建字体对象，SysFont的第一个参数是字体名，设置为None会使用默认字体，
# 第二个参数是字体大小（尺寸size）
font = pygame.font.SysFont(None, 24)
# 用刚新建的字体对象，创建文本对象，
# render的第一个参数是文本(字符串类型），
# 第二个参数为是否设置光滑边缘，一般设置为True就好
# 第三个参数为文本颜色
text = font.render('hello world', True, "green")
# 将文本展示在指定位置，blit的第一个参数是文本对象，
# 第二个参数是坐标（左上角的横坐标，纵坐标）
win.blit(text, (40, 20))

text2 = font.render('hello world', True, "yellow")
text3 = font.render('hello world', True, "white")

win.blit(text2, (200, 20))
win.blit(text3, (40, 100))

while True:
    clock.tick(60)
    pygame.display.update()