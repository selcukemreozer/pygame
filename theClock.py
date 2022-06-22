import pygame
import math
from time import sleep

sleep_sayac = 0.1
speedValue = 0.001
derece = 360
dereceDK = 360
dereceST = 360
sayac = 0

sayi = 12

beyaz=(255,255,255)
mavi=(0,0,255)
yesil=(34,139,34)
turuncu=(255,69,0)
kırmızı=(255,0,0)

pygame.init()
font = pygame.font.SysFont("ComicSansMs", 18)

def sayi(value):
    sayilar = font.render(str(int(value / 30)), 2, beyaz)
    return  sayilar

"""def CIRCLE_DRAWER(x1, y1, x2, y2):
    pass"""
screen = pygame.display.set_mode([500, 500])

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    # pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 4)
    xsaniye = -50 * round(math.sin(math.radians(derece)), 5) + 250
    ysaniye = -50 * round(math.cos(math.radians(derece)), 5) + 250

    """
    saniye  = -10 * round(math.sin(math.radians(derece)), 5) + 100
    saniye2 = -10 * round(math.cos(math.radians(derece)), 5) + 100
    saniye3 = 25 * round(math.sin(math.radians(derece)), 5) + 100
    saniye4 = 25 * round(math.cos(math.radians(derece)), 5) + 100
    """

    xdakika = -50 * round(math.sin(math.radians(dereceDK)), 5) + 250
    ydakika = -50 * round(math.cos(math.radians(dereceDK)), 5) + 250
    xsaat   = -40 * round(math.sin(math.radians(dereceST)), 5) + 250
    ysaat   = -40 * round(math.cos(math.radians(dereceST)), 5) + 250

    # pygame.draw.line(screen, (255, 255, 255), (saniye3, saniye4), (saniye, saniye2))
    # pygame.draw.line(screen, (255, 255, 255), (100, 100), (saniye3, saniye4))

    pygame.draw.line(screen, (255, 255, 255), (250, 250), (xsaniye, ysaniye))
    pygame.draw.line(screen, kırmızı, (250, 250), (xdakika, ydakika), 2)
    pygame.draw.line(screen, (0, 255, 255), (250, 250), (xsaat, ysaat), 3)

    derece-=6
    for each in range(360):

        if (each) % 30 == 0:
            xsayi = -50 * round(math.sin(math.radians(each)), 5) + 250
            ysayi = -50 * round(math.cos(math.radians(each)), 5) + 250
            screen.blit(sayi(each), (xsayi-5, ysayi-15))

    if derece == 0:
        derece=360
        dereceDK-=6 # her 60 saniyede yelkovan 6 derece ilerliyor. Her dakika 6 derece.
        sayac+=1

    if dereceDK == 0:
        dereceDK = 360

    if sayac == 6: # akrep her 6 saniyede 3 derece hareket ediyor. Her 1 saat 30 derece. 3 x 10 = 30 derece = 1saat
        dereceST -= 3
        sayac = 0

    if dereceST == 0:
        dereceST = 360

    # print(f"\ndegree:{derece}\nx1:{x1 - 100}\ny1:{y1 - 100}\nx2:{x2 - 100}\ny2:{y2 - 100}\n")
    sleep_sayac -= speedValue
    if sleep_sayac < 0.001:
        speedValue = -speedValue

    elif sleep_sayac > 0.1:
        speedValue = -speedValue

    print(f"sleep_sayac:{sleep_sayac}")
    sleep(sleep_sayac)



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
