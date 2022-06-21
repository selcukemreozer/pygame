import pygame
import math
from time import sleep

donus_x = False
donus_y = False
degree = 0


pygame.init()

"""def CIRCLE_DRAWER(x1, y1, x2, y2):
    pass"""
screen = pygame.display.set_mode([500, 500])

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 0, 0))

    # pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 4)
    x1 = 25 * round(math.cos(math.radians(degree)), 5)+100 +25*(1-degree/360)
    y1 = 25 * round(math.sin(math.radians(degree)), 5)+100 +25*(1-degree/360)
    x2 = 50 * round(math.sin(math.radians(degree)), 5)+100
    y2 = 50 * round(math.cos(math.radians(degree)), 5)+100
    pygame.draw.line(screen, (255, 255, 255), (100, 100), (x2, y2))

    degree+=1
    if degree == 360:
        degree=6
    print(f"\ndegree:{degree}\nx1:{x1-100}\ny1:{y1-100}\nx2:{x2-100}\ny2:{y2-100}\n")
    sleep(1)
    """
    if y1 == 200:
        donus_y = True

    elif y1 == 300:
        donus_y = False

    if donus_y:
        y1+=1
        y2-=1

    else:
        y1-=1
        y2+=1

    if x1 == 150:
        donus_x = True
        print(f"x1:{x1}\nx2:{x2}\ny1:{y1}\ny2:{y2}\n")

    elif x1 == 250:
        donus_x = False

    if donus_x:
        x1+=1
        x2-=1

    else:
        x1-=1
        x2+=1
        """
    pygame.display.flip()
pygame.quit()

y1 = round(math.sin(math.radians(degree)), 2)
x1 = round(math.cos(math.radians(degree)), 2)
