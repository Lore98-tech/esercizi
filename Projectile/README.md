This game simulate the projectile motion. Projectiles bump against the floor and the window's edges. 
The windows is 1400*800 pixels. It can be considered to represent 140*80 m*m or 14*8 m*m, etc..
Several parameters can be set:
mu : the dynamic viscosity of the medium [*1/10 m/s];
g : the gravity acceleration;
WIND : the wind's velocity;
ATT_AN : the coefficient of inelastic friction that modulates the projectile's velocity when it bumps.

for i in range(200):
   a = Projectile(-599 + 5*i, -100, 3, FUCSIA)
   a.x_vel = np.sin(np.pi/10*i)*i*2
   a.y_vel = -np.cos(np.pi/10*i)*i*2
   projectiles.append(a)

for i in range(10):
   a = Projectile(random.randint(-599, 599), random.randint(-300, 400), random.randint(1, 20), color = random_color())
   a.x_vel = random.randint(100, 500) * random.choice((-1, 1))
   a.y_vel = random.randint(100, 500) * random.choice((-1, 1))

for event in pygame.event.get():
     if event.type == pygame.QUIT:
          run = False
     if event.type == pygame.MOUSEBUTTONDOWN:
         i = i + 1
         color = pclass.random_color()
          a = pclass.Projectile(random.randint(-599, 599), random.randint(-300, 400), random.randint(1, 20), color = color)
          a.x_vel = random.randint(100, 500) * random.choice((-1, 1))
          a.y_vel = random.randint(100, 500) * random.choice((-1, 1))
          projectiles.append(a)
          print("Projectile n. ", i, "color = ", color)

                color = pclass.FUCSIA
                a = pclass.Projectile(0, 0, 5, color = color)
                a.x_vel = 0
                a.y_vel = 0
                projectiles.append(a)
                print("Projectile n. ", i, "color = ", color)


