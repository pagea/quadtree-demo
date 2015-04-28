import sys
import pygame
import front
import model
import collision

WIN_SIZE = (1366, 768)

def run_sim(arg1, arg2):
    detector = None
    if arg1 is 0:
        print("No collision detection enabled.")
    if arg1 is 1:
        print("Using brute force collision detection.")
        detector = collision.BasicDetector()
    if arg1 is 2:
        print("Using Quadtree collision detection.")
        detector = collision.QuadtreeDetector()

    pygame.init()
    clock = pygame.time.Clock()
    world = model.World(WIN_SIZE[0], WIN_SIZE[1], arg2)
    screen = pygame.display.set_mode((WIN_SIZE), pygame.FULLSCREEN)
    # Main loop
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        world.step(detector)
        front.draw_quad(screen, detector)
        front.update_frame(world, screen)
