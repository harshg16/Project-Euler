import math

for x in range(1,1000):
    for y in range (x,1000):
        z = x**2 + y**2
        if (z == ((int)(math.sqrt(z)))**2):
            if (x + y + math.sqrt(z) == 1000):
                print(x*y*math.sqrt(z),x,y,math.sqrt(z))
        