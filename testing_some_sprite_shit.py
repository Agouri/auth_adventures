import pygame
import time
from threading import Thread

class Pokemon(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, filename):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load(filename)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

pygame.init()

        
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

mySurface = pygame.Surface((800,600))
mySurface.fill((255,255,255))
mySurface.set_colorkey((255,0,255))
gameDisplay.blit(mySurface, (0,0))

#### NPC Sprite Group to blit at each tick ####
poke_sprites = pygame.sprite.Group()

#### Display variables ####
pygame.display.set_caption("Edw ston agwna")

white = (255,255,255)
black = (0,0,0)
red = (190,0,7)

hero = Pokemon("scyther.png")
poke_sprites.add(hero) #TODO: Change this functionality in the class'es __init__
enemy = Pokemon("beedrill.png")
poke_sprites.add(enemy)

FPS = 30
clock = pygame.time.Clock()

def message_to_screen(msg, color):
    textSurf, textRect = text_objects(msg,color)
    text.Rect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)

def enemyMove():
    location_x = 0
    location_y = 100
    
    while True:
        enemy.rect = enemy.rect.move(2,0)
        clock.tick(FPS/2)

##def blitHero():
##    heroRect.center = (display_width/2), 550
##    location_x = display_width/2
##    location_y = 550
##    gameDisplay.blit(hero,heroRect)

##def moveEnemy(speed):
##    location_x = 800
##    location_y = 100
##    while location_x <= 800 and location_x >=0:
##        gameDisplay.blit(enemy,[location_x,location_y])
##        location_x -= speed * 2
##        location_y += speed
    

##def moveHero(location_x,location_y):
##    if (location_x + 50 < 800 and location_x + 50 > 0) or (location_y + 50 < 600 and location_y + 50 > 0):
##        gameDisplay.blit(hero,[location_x,location_y])
##   
       
    
def gameLoop():

    gameRunning = True
    gameOver = False


    block_size = 10
    location_x = 0
    location_y = 0
    X = 400
    Y = 200
    speed = 5
    gameDisplay.fill(red)
    

    while gameRunning:

        while gameOver:

            gameDisplay.fill(white)
            message_to_screen("Game Over Press C To Play Again Or Q to Quit")
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameRunning = False
                    elif event.key == pygame.K_c:
                        gameLoop()
                elif event.type == pygame.QUIT:
                    gameOver = False
                    gameRunning = False
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if hero.rect.left - 50 >= 0:   
                        hero.rect = hero.rect.move((-50,0))
                        
                elif event.key == pygame.K_RIGHT:
                    if hero.rect.right + 50 < 800:
                        hero.rect = hero.rect.move((50,0))
                    
                elif event.key == pygame.K_UP:
                     if hero.rect.top - 50 >= 0:
                         hero.rect = hero.rect.move((0,-50))
                    
                elif event.key == pygame.K_DOWN:
                     if hero.rect.bottom + 50 < 600:
                         hero.rect = hero.rect.move((0,50))

        gameDisplay.blit(mySurface, (0,0))
        for this_sprite in poke_sprites:
            gameDisplay.blit(this_sprite.image, this_sprite.rect)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    quit()
beedrill1 = Thread(target = enemyMove)
beedrill1.daemon = True
beedrill1.start()

gameLoop()
    
            

            
            
            
