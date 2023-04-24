import pygame 
import sympy as sym
import math
import random
import numpy as np
import projectile_class as pclass

pygame.init()

FONT = pygame.font.SysFont("comicsans", 16)

WIDTH, HEIGHT = 1400,750
GND = 0
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Proiettile") 

def main():
    run = True
    clock = pygame.time.Clock()

    projectiles = []
    i = 0

    while run:
        clock.tick(60)
        WIN.fill(pclass.WHITE)
        pygame.draw.rect(WIN, pclass.BLACK, pygame.Rect(0, HEIGHT - GND, WIDTH, GND))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                i = i + 1
                color = pclass.FUCSIA
                a = pclass.Projectile(0, 0, 5, color = color)
                a.x_vel = 100
                a.y_vel = 10 * i - 10
                projectiles.append(a)
                print("Projectile n. ", i, "color = ", color, "x vel = ", a.x_vel, "y vel = ", a.y_vel)

        for projectile in projectiles:
            projectile.update_position()
            projectile.draw(WIN)
            #rojectile.draw_trajectory(WIN)

        pygame.display.update()

    pygame.quit()

main()

