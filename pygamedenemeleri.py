import random
import time
import pygame

try:
    again += 1
except NameError:
    again = 1
from pygame.locals import (
    RLEACCEL,
    K_w,
    K_a,
    K_s,
    K_d,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    )


clock = pygame.time.Clock()
pygame.init()

# for animation
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
 
        self.images = []
        self.images.append(pygame.image.load('images/position_1.png'))
        self.images.append(pygame.image.load('images/position_2.png'))
        """
        self.images.append(pygame.image.load('images/walk3.png'))
        self.images.append(pygame.image.load('images/walk4.png'))
        self.images.append(pygame.image.load('images/walk5.png'))
        self.images.append(pygame.image.load('images/walk6.png'))
        self.images.append(pygame.image.load('images/walk7.png'))
        self.images.append(pygame.image.load('images/walk8.png'))
        self.images.append(pygame.image.load('images/walk9.png'))
        self.images.append(pygame.image.load('images/walk10.png'))
        """
 
        self.index = 0
 
        self.image = self.images[self.index]
 
        self.rect = pygame.Rect(5, 5, 150, 198)
 
    def update(self):
        self.index += 1
 
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        
        
# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((30,30))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # kullanıcının yön tuşlarını kullandığında olacak hareket davranışını oluşturdu
    def update(self, pressed_keys):
        
        if pressed_keys[K_UP] and self.rect.bottom == SCREEN_HEIGHT:
            # !!!!!!!!!!!!!!!!!!
            for each in range(16):
                self.rect.move_ip(0, -5)
                pygame.display.flip()
            
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            
        if pressed_keys[K_RIGHT]:
            
            print(again)
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right  > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom < SCREEN_HEIGHT:
            # zeminden yukarıda ise zıplamasını engellemek için jump bool değişkeni var
            self.rect.move_ip(0, 5)
            loop = 0

            


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

            
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(screen_size)

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

running = True

# oyun döngüsü
while running:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:

            running = False

        # add e new enemy?
        elif event.type == ADDENEMY:
            # create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
            
    # Bu, her karenin başında basılan tuşları içeren bir sözlük döndürür
    pressed_keys = pygame.key.get_pressed()

    # kullanıcı tuşlara bastığında oyunucunun konumunu günceller
    player.update(pressed_keys)
    enemies.update()
    
    screen.fill((255, 0, 0))

    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    # if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        # player.kill()
        # running = False
    
    # oyuncuyu ekrana çiziyor
    screen.blit(player.surf, player.rect)
    
    # pygame.draw.circle(screen, (123, 123, 123), (123, 123), 75)
    # time.sleep(0.01)
    pygame.display.flip()
    clock.tick(50)
    
pygame.quit()
