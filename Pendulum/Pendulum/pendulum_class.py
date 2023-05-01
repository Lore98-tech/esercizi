import pygame 
import numpy as np

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

class Pendulum:
    SCALE = 1
    TIMESTEP = 1/60
    X_TOP, Y_TOP = WIDTH/2, HEIGHT/10
    #mu = 1800 * 10**(-6) #air
    mu = 0
    g = 98.1
    def __init__(self, angle, l, mass, color):
        self.angle = angle
        self.l = l * 10
        self.mass = mass
        self.color = color

        self.trajectory = []
        self.velocity = []
        self.vel = 0
        self.radius = self.mass
        self.time = 0
        self.w = np.sqrt(self.g/self.l)

    def draw(self, win):
        x = np.sin(np.radians(self.angle)) * self.l * self.SCALE + self.X_TOP
        y = np.cos(np.radians(self.angle)) * self.l * self.SCALE + self.Y_TOP
        #pygame.draw.lines(win, BLACK, False, [(self.X_TOP, self.Y_TOP), (x, y)], 1)
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def draw_trajectory(self, win):
        if len(self.trajectory) > 2:            
            trajectory_text_angle = FONT.render(f"angle = {round(self.trajectory[len(self.trajectory) - 1], 1)}", 1, BLACK)
            trajectory_text_velocity = FONT.render(f"velocity = {round(np.abs((self.velocity[len(self.velocity) - 1])/10), 1)}", 1, BLACK)
            win.blit(trajectory_text_angle, (7/8*WIDTH, HEIGHT/8))
            win.blit(trajectory_text_velocity, (7/8*WIDTH, HEIGHT/8 + 20))

    def gravity(self):
        force = self.mass * self.g
        return force
    
    def air_att(self):
        if self.mu == 0:
            f = 0
        else:
            f = -6 * np.pi * self.mu * self.radius * self.vel
        return f

    def update_position(self):
        self.time += self.TIMESTEP
        att = self.air_att()
        self.vel += (-self.g * np.sin(np.radians(self.angle)) + att) * self.TIMESTEP
        self.angle += np.degrees(self.vel/self.l * self.TIMESTEP)
        self.trajectory.append(self.angle)
        self.velocity.append(self.vel)
