# How to create an animation using the function animation() from matplotlib or not
# Two examples

# run --> %matplotlib qt
# in IPython before the code

#______________________________________________________________________________________________________
# ANIMATION WITH THE FUNCTION animation()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 2*np.pi
w = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 100

x = np.linspace(xmin, xmax, nbx)

fig = plt.figure() # initialise la figure
line, = plt.plot([],[]) 
plt.xlim(xmin, xmax)
plt.ylim(-1,1)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([],[])
    return line,

def animate(i): 
    t = i * dt
    y = np.cos(k*x - w*t)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, blit=True, interval=20, repeat=False)

plt.show()

#_____________________________________________________________________________________________________________________
#ANIMTAION WITHOUT THE FUNCTION animation()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 100)
k = 2*np.pi
w = 2*np.pi
dt = 0.01  

t = 0
for i in range(50):
    y = np.cos(k*x - w*t)
    if i == 0:
        line, = plt.plot(x, y)
    else:
        line.set_ydata(y)
    plt.pause(0.01) # pause avec duree en secondes
    t = t + dt
    
plt.show()
