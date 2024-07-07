import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def flower(radius, petal_count, t):
    theta = np.linspace(0, 2 * np.pi, 100)
    r = radius * (1 + 0.5 * np.sin(petal_count * theta + t))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

flower_patch, = ax.plot([], [], lw=2)
colors = plt.cm.viridis(np.linspace(0, 1, 128))

def init():
    flower_patch.set_data([], [])
    return flower_patch,

def update(t):
    x, y = flower(5, 6, t)
    flower_patch.set_data(x, y)
    flower_patch.set_color(colors[int(t / (2 * np.pi) * 127)])
    return flower_patch,

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 128),
                              init_func=init, blit=True)

plt.show()