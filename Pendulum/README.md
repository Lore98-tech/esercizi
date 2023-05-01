This code simulates the motion of one or multiple pendulums. 
X_TOP, Y_TOP are the coordinates of the point where the rope is attached. 
The units of measurement are considered as [1/10 m].
The position of the pendulum is defined through the angle between a vertical line and the rope.
Medium friction can be added by changing 'mu' to a non-zero value, that is the viscosity coefficient. 

draw_trajectory works for a single pendulum. 
pygame.draw.lines(win, BLACK, False, [(self.X_TOP, self.Y_TOP), (x, y)], 1) is for drawing the rope.

Examples:
*for i in range(100):
    pendulum = pc.Pendulum(0, 35, 5, pc.FUCSIA)
    pendulum.vel = 8 * i
    pend.append(pendulum)

*for i in range(30):
    pendulum = pc.Pendulum(30, 2 + 2 * i, 5, pc.FUCSIA)
    pend.append(pendulum)

*pendulum = pc.Pendulum(5, 60, 10, pc.FUCSIA)
pend.append(pendulum)