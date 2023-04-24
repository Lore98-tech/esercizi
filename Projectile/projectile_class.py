import pygame
import random
import numpy as np

pygame.init()

WIDTH, HEIGHT = 1400,750 
GND = 0

FONT = pygame.font.SysFont("comicsans", 16)

WHITE = (255, 255, 255) 
FUCSIA = (200, 0, 200)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

class Projectile:
    SCALE = 1
    TIMESTEP = 1/60
    ATT_AN = 1
    WIND = 0 #*1/10 m/s
    #mu = 174 * 10**(-6) #aria
    mu = 0
    #g = 9.81
    g = 0
    def __init__(self, x, y, mass, color):
        self.x = x
        self.y = y
        self.mass = mass
        self.color = color

        self.trajectory = []
        self.x_vel = 0
        self.y_vel = 0
        self.radius = self.mass
        self.time = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def draw_trajectory(self, win):
        if len(self.trajectory) > 2:
            updated_points = []
            for point in self.trajectory:
                x, y = point
                x = x * self.SCALE + WIDTH/2
                y = y * self.SCALE + HEIGHT/2
                updated_points.append((x, y))
                if len(self.trajectory) > 100:
                    updated_points = updated_points[len(updated_points) - 100:]
                    
            pygame.draw.lines(win, BLACK, False, updated_points, 2)
            trajectory_text_x = FONT.render(f"x = {round(x/10 - WIDTH/20, 1)} m", 1, BLACK)
            trajectory_text_y = FONT.render(f"y = {round(-(y/10 - HEIGHT/10 + GND/10), 1)} m", 1, BLACK)
            win.blit(trajectory_text_x, (x, y))
            win.blit(trajectory_text_y, (x, y + 20))

    def gravity(self):
        force = self.mass * self.g
        return force
    
    def wind(self):
        if self.mu == 0:
            fx = 0
            fy = 0
        else:
            fx = -6 * np.pi * self.mu * self.radius * (self.x_vel + self.WIND)
            fy = -6 * np.pi * self.mu * self.radius * self.y_vel
        return fx, fy

    def update_position(self):
        total_fx = total_fy = 0
        self.time += self.TIMESTEP
        wx, wy = self.wind()
        fy = self.gravity() + wy
        fx = wx
        total_fx += fx
        total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        if self.y > HEIGHT/2 - GND:
            self.y_vel = - self.y_vel * self.ATT_AN
            self.y = HEIGHT/2 - GND
            self.x_vel = self.x_vel * self.ATT_AN
            #print(self.time)
            #print(self.x/10)
        if self.x < -WIDTH/2:
            self.x_vel = - self.x_vel * self.ATT_AN 
            self.x = -WIDTH/2
        if self.x > WIDTH/2:
            self.x_vel = - self.x_vel * self.ATT_AN 
            self.x = WIDTH/2
        if self.y < -HEIGHT/2:
            self.y_vel = - self.y_vel * self.ATT_AN
            self.y = -HEIGHT/2
            self.x_vel = self.x_vel * self.ATT_AN
        self.trajectory.append((self.x, self.y))