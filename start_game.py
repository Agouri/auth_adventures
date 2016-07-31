import sys, pygame, os

#position = (0, 0)
#os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
os.environ['SDL_VIDEO_CENTERED'] = '1' #Centers the opened window to the middle of the screen

init_results = pygame.init() #Returns a 2-tuple (numpass, numfail), numpass is how many modules initiated succesfully, numfail is how many failed to initialize
if init_results[1] != 0:
        print("Failed to initialize ", init_results[1], " modules!")

scr_size = width, height = 640, 320
speed = [1, 1]
black = (0, 0, 0)

screen = pygame.display.set_mode(scr_size)

ball = pygame.image.load("assets/ball.gif")
ballrect = ball.get_rect()
hero = pygame.image.load("assets/hero.png")
heroRect = hero.get_rect()

running = True
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:          
                        running = False #Be IDLE friendly :)
            
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
                speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
                speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        screen.blit(hero, heroRect)
        pygame.display.flip()
        print("POS - Top:", ballrect.top, " Right:", ballrect.right, " Bottom:", ballrect.bottom, " Left:", ballrect.left)
        pygame.time.delay(200)

pygame.quit()
