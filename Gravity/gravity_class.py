import pygame 
import numpy as np
import math

WIDTH, HEIGHT = 1400,800

pygame.init()
FONT = pygame.font.SysFont("comicsans", 16)

WHITE = (255, 255, 255) 
FUCSIA = (200, 0, 200)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (50, 205, 50)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

class Body:
    AU = 149.6e9
    G = 6.67428e-1
    #mu = 1800 * 10**(-6) #air
    mu = 0
    TIMESTEP = 1
    SCALE = 1

    def __init__(self, x, y, mass, color):
        self.x = x
        self.y = y
        self.mass = mass
        self.color = color
        self.radius = self.mass

        self.trajectory = []
        self.velocity = []

        self.vel_x = 0
        self.vel_y = 0
        self.time = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def draw_trajectory(self, win):
        if len(self.trajectory) > 2:            
            trajectory_text_angle = FONT.render(f"angle = {round(self.trajectory[len(self.trajectory) - 1], 1)}", 1, BLACK)
            trajectory_text_velocity = FONT.render(f"velocity = {round(np.abs((self.velocity[len(self.velocity) - 1])/10), 1)}", 1, BLACK)
            win.blit(trajectory_text_angle, (7/8*WIDTH, HEIGHT/8))
            win.blit(trajectory_text_velocity, (7/8*WIDTH, HEIGHT/8 + 20))

    def gravity(self, other):
        distance_x = self.x - other.x
        distance_y = self.y - other.y
        distance2 = (distance_x)**2 + (distance_y)**2
        force = self.G * self.mass * other.mass / distance2
        angle = math.atan2(distance_y, distance_x)
        force_x, force_y = math.cos(angle) * force, math.sin(angle) * force
        return force_x, force_y
    
    def air_att(self):
        if self.mu == 0:
            f = 0
        else:
            f = -6 * np.pi * self.mu * self.radius * self.vel
        return f

    def update_position(self, bodies):
        total_fx, total_fy = 0, 0
        self.time += self.TIMESTEP
        for body in bodies:
            if self == body:
                continue
            f_x, f_y = self.gravity(body)
            total_fx += -f_x
            total_fy += -f_y
        self.vel_x += total_fx/self.mass * self.TIMESTEP
        self.vel_y += total_fy/self.mass * self.TIMESTEP
        self.x += self.vel_x * self.TIMESTEP
        self.y += self.vel_y * self.TIMESTEP
        self.trajectory.append((self.x, self.y))
        self.velocity.append((self.vel_x, self.vel_y))

