import sys, pygame, os
from safe_movement import safe_move
from classes.hero import Hero

#position = (0, 0)
#os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
os.environ['SDL_VIDEO_CENTERED'] = '1' #Centers the opened window to the middle of the screen

init_results = pygame.init() #Returns a 2-tuple (numpass, numfail), numpass is how many modules initiated succesfully, numfail is how many failed to initialize
if init_results[1] != 0:
        print("Failed to initialize ", init_results[1], " modules!")

SCR_SIZE = width, height = 800, 600
speed = [1, 1]
black = (0, 0, 0)
#### SPEED CONSTANTS ####
LOW_SPEED = 2
MED_SPEED = 5
HIGH_SPEED = 10
MY_SPEED = MED_SPEED

#### Game clock ####
clock = pygame.time.Clock()

screen = pygame.display.set_mode(SCR_SIZE)

#Testing Hero class
protagonist = Hero()
heroRect = protagonist.rect
heroRect.move_ip(width/2 - 32 , height/2 - 32)

#hero = pygame.image.load("assets/hero_64x64.png")
#heroRect = hero.get_rect()
#heroRect.move_ip(width/2 - 32 , height/2 - 32)

running = True
while running:
        pressedKeys = pygame.key.get_pressed() #Returns a boolean index of all keys currently being held down
        if pressedKeys[pygame.K_LEFT]:
                protagonist.changeDirection(3)
                heroRect = safe_move(SCR_SIZE, heroRect, [-MY_SPEED,0])
        if pressedKeys[pygame.K_RIGHT]:
                protagonist.changeDirection(1)
                heroRect = safe_move(SCR_SIZE, heroRect, [MY_SPEED,0])
        if pressedKeys[pygame.K_DOWN]:
                protagonist.changeDirection(2)
                heroRect = safe_move(SCR_SIZE, heroRect, [0, MY_SPEED])
        if pressedKeys[pygame.K_UP]:
                protagonist.changeDirection(0)
                heroRect = safe_move(SCR_SIZE, heroRect, [0, -MY_SPEED])
        #Handle events! These, for now, can be KEYPRESS EVENTS or a single QUIT event
        #TODO: Handle situations where the user is pressing and keeping a key down, continuously
        for event in pygame.event.get():
                if event.type == pygame.QUIT:          
                        running = False #Be IDLE friendly :)

        screen.fill(black)
        screen.blit(protagonist.current_image, heroRect)
        pygame.display.flip()
        print("POS - Top:", heroRect.top, " Right:", heroRect.right, " Bottom:", heroRect.bottom, " Left:", heroRect.left)
        clock.tick(120)

pygame.quit()

