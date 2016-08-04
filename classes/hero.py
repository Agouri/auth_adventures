import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self, gs=None):
        pygame.sprite.Sprite.__init__(self)
        #Stores all directional images of the current hero
        # [0] == Top
        # [1] = Right
        # [2] = Bottom
        # [3] = Left
        self.images = [pygame.image.load("assets/hero_top.png"),
                       pygame.image.load("assets/hero_right.png"),
                       pygame.image.load("assets/hero_bottom_sack.png"),
                       pygame.image.load("assets/hero_left.png")]
        self.current_image = self.images[2]
        self.rect = self.current_image.get_rect()
    def changeDirection(self, d):
        #TODO: Safety check
        self.current_image = self.images[d]
        self.rect = self.current_image.get_rect()
        
