#Dylan Wattles
#Collisions and digits of pi
from visual import *

#large mass must be small.mass*100^n for pi collisions
ground=box(pos=vector(0,0,0),length=40,height=1,width=1)
wall=box(pos=(-9.5,2,0),length=1,height=4,width=1)
small=box(pos=(-4,1,0),length=1,height=1,width=1,
          mass=1,velocity=vector(0,0,0),color=color.red)
large=box(pos=(0,1.5,0),length=2,height=2,width=1,
          mass=1,velocity=vector(0,0,0),color=color.cyan)

# repeats demonstration with multiples of 100 of large mass
for i in range(0,6):
    time=0
    dt=.00001
    collisions=0
    small.velocity.x=0
    large.velocity.x=-1
    small.pos.x=-4
    large.pos.x=0

    # loop to continuously update positions
    while ((small.velocity.x<0) or (small.velocity.x>=large.velocity.x)):
        rate(100000)

        # x = x +vt, update positions 
        large.pos.x=large.pos.x+large.velocity.x*dt
        small.pos.x=small.pos.x+small.velocity.x*dt

        # large collides with small
        if ((large.pos.x-1)-(small.pos.x+.5))<.0000001:
            temp=large.velocity.x
            large.velocity.x=(2*small.mass*small.velocity.x+large.velocity.x
                              *(large.mass-small.mass))/(large.mass+small.mass)
            small.velocity.x=(2*large.mass*temp+small.velocity.x
                              *(small.mass-large.mass))/(large.mass+small.mass)
            collisions=collisions+1

        # small collides with wall    
        if ((small.pos.x-small.length/2)-(wall.pos.x+wall.length/2))<.0000001:
            small.velocity.x=-small.velocity.x
            collisions=collisions+1

        time=time+dt

    print('mass ratio',large.mass/small.mass,'collisions',collisions)
    large.mass=large.mass*100
