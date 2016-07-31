import pygame

### Safely moves a rectangle within the constraints of the screen,
### meaning it will refuse to move the object beyond the borders.
### Params:
### @scrSize: a constant 2-tuple containing the size of the screen, the borders
### @rectangle: a pygame.Rect object
### @movement: a 2-tuple containing (x,y) axis movement.
def safe_move(scrSize, rectangle, movement):
        local_rect = rectangle.move(movement)
        if local_rect.top < 0:
                local_rect.top = 0
        if local_rect.right > scrSize[0]:
                local_rect.right = scrSize[0]
        if local_rect.bottom > scrSize[1]:
                local_rect.bottom = scrSize[1]
        if local_rect.left < 0:
                local_rect.left = 0

        return local_rect
