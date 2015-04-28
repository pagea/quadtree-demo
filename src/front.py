import pygame
import sys
import model
import controller

# Color of non-colliding circles
blue = (138, 255, 255)
# Color of colliding circles
orange = (255, 170, 51)


def draw_circ(circle, color, screen)
    '''A nice wrapper for pygame's ugly-ass draw syntax. '''
    pygame.gfxdraw.filled_circle(screen, c.coord[0], c.coord[1], c.radius, color)

def update_frame(screen):
    '''Draw everything onto the screen.'''
    # Draw the background
    screen.fill((255, 255, 255))
    
    # Draw all of the circles
    for c in controller.world:
        #Are we colliding? If so, change the color
        if c.collide is False:
            draw_circ(c, blue, screen)
        else:
            draw_circ(c, orange, screen)

    # Update the screen
    pygame.display.update()
