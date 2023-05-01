import pygame
import numpy as np
import pendulum_class as pc

pygame.init()

FONT = pygame.font.SysFont("comicsans", 16)

WIDTH, HEIGHT = 1400,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Pendulum") 

pend = []
for i in range(30):
    pendulum = pc.Pendulum(30, 2 + 2 * i, 5, pc.FUCSIA)
    pend.append(pendulum)

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        WIN.fill(pc.WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for pendulum in pend:
            pendulum.update_position()
            pendulum.draw(WIN)
            #pendulum.draw_trajectory(WIN)

        pygame.display.update()

    pygame.quit()

main()
