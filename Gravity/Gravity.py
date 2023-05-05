import pygame
import numpy as np
import gravity_class as gc

pygame.init()

FONT = pygame.font.SysFont("comicsans", 16)

WIDTH, HEIGHT = 1400,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Pendulum") 

body1 = gc.Body(0, 0, 6, gc.BLACK)
body1.vel_x = 0.1
body2 = gc.Body(100, 100, 6, gc.RED)
planets = [body1, body2]

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        WIN.fill(gc.WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
            #planet.draw_trajectory(WIN)

        pygame.display.update()

    pygame.quit()

main()

