import pygame
import time
from threading import Thread
pygame.init()


    

        
display_width = 800
display_height = 600

mySurface = pygame.Surface((800,600))


gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Edw ston agwna")

white = (255,255,255)
black = (0,0,0)
red = (190,0,7)

hero = pygame.image.load("scyther.png")
enemy = pygame.image.load("beedrill.png")
heroRect = hero.get_rect()

FPS = 15
clock = pygame.time.Clock()

def message_to_screen(msg, color):
    textSurf, textRect = text_objects(msg,color)
    text.Rect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)

def enemyMove():
    location_x = 0
    location_y = 100
    enemyRect = enemy.get_rect()

    #gameDisplay.blit(enemy,location_x, location_y)
    while True:

        gameDisplay.fill(white)
        enemyRect = enemyRect.move(10,0)
        gameDisplay.blit(enemy,enemyRect)
        pygame.display.update()
        clock.tick(5)

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
                    if location_x - 50 >= 0:
                         location_x -= 50
                        
                elif event.key == pygame.K_RIGHT:
                    if location_x + 50 < 800:
                           location_x += 50
                    
                elif event.key == pygame.K_UP:
                     if location_y - 50 >= 0:
                            location_y -= 50
                    
                elif event.key == pygame.K_DOWN:
                     if location_y + 50 < 600:
                          location_y += 50
                    
            gameDisplay.fill(white)
            gameDisplay.blit(hero,[location_x,location_y])
            pygame.display.update()
            
        
        
        clock.tick(5)

    pygame.quit()
    quit()
beedrill1 = Thread(target = enemyMove)
beedrill1.daemon = True
beedrill1.start()

gameLoop()
    
            

            
            
            
