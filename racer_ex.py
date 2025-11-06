# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing 
pygame.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load and scale background to fill the screen
background = pygame.image.load("road.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        # scaling original image
        self.image = pygame.image.load("yellow_car.png").convert()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # red original ~900x737 -> scaled to 60x50 (wider-ish)
        self.image = pygame.image.load("red_car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # try to load coin image, fallback to a drawn circle surface
        try:
            self.image = pygame.image.load("gold.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (28, 28))
        except Exception:
            surf = pygame.Surface((28, 28), pygame.SRCALPHA)
            pygame.draw.circle(surf, (255, 215, 0), (14,14), 14)
            self.image = surf
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH-20), 0)

    def move(self):
        # coins fall slightly slower than enemies
        self.rect.move_ip(0, max(1, int(SPEED / 1.5)))
        if self.rect.top > SCREEN_HEIGHT:
            # respawn at top at a new x position
            self.rect.top = 0
            self.rect.center = (random.randint(20, SCREEN_WIDTH-20), 0)

# Setting up Sprites        
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Add an initial coin
initial_coin = Coin()
coins.add(initial_coin)
all_sprites.add(initial_coin)

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
# Event to spawn coins periodically
SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 3000)  # every 3 seconds

# Game Loop
while True:
       
    # Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == SPAWN_COIN:
            # spawn a new coin (limit count to avoid clutter)
            if len(coins) < 6:
                c = Coin()
                coins.add(c)
                all_sprites.add(c)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # draw background (now scaled to full screen)
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    # show coins collected
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        # only call move if sprite has move method
        if hasattr(entity, 'move'):
            entity.move()

    # check collision between player and coins
    collected = pygame.sprite.spritecollide(P1, coins, True)
    if collected:
        # play coin sound if present (coin_sound.mp3 or coin.wav)
        try:
            pygame.mixer.Sound('coin_sound.mp3').play()
        except Exception:
            pass
        COINS += len(collected)
        # spawn replacement coins immediately so gameplay continues
        for _ in collected:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          try:
              pygame.mixer.Sound('crash_sound.mp3').play()
          except Exception:
              pass
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)
