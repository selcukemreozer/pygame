import pygame
import math
from time import sleep

donus_x = False
donus_y = False
derece = 360
dereceDK = 360
dereceST = 360
sayac = 0

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
    xsaniye = -50 * round(math.sin(math.radians(derece)), 5) + 250
    ysaniye = -50 * round(math.cos(math.radians(derece)), 5) + 250
    xdakika = -50 * round(math.sin(math.radians(dereceDK)), 5) + 250
    ydakika = -50 * round(math.cos(math.radians(dereceDK)), 5) + 250
    xsaat   = -50 * round(math.sin(math.radians(dereceST)), 5) + 250
    ysaat = -50 * round(math.cos(math.radians(dereceST)), 5) + 250
    pygame.draw.line(screen, (255, 255, 255), (250, 250), (xsaniye, ysaniye))
    pygame.draw.line(screen, (0, 0, 255), (250, 250), (xdakika, ydakika), 3)
    pygame.draw.line(screen, (0, 255, 255), (250, 250), (xsaat, ysaat), 3)

    derece-=6
    if derece == 0:
        derece=360
        dereceDK-=6
        sayac+=1

    if dereceDK == 0:
        dereceDK = 360

    if sayac == 6:
        dereceST -= 3
        sayac = 0

    if dereceST == 0:
        dereceST = 360

    # print(f"\ndegree:{derece}\nx1:{x1 - 100}\ny1:{y1 - 100}\nx2:{x2 - 100}\ny2:{y2 - 100}\n")
    sleep(0.0001)
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

y1 = round(math.sin(math.radians(derece)), 2)
x1 = round(math.cos(math.radians(derece)), 2)
