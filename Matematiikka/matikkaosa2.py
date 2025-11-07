from matplotlib import pyplot as plt, patches
import numpy as np

fig = plt.figure()
ax = fig.subplots()

# Draw the unit circle
ymp = patches.Circle((0, 0), radius=1, fill=False)
ax.add_patch(ymp)

# Center axes
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.axis('equal')

plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

# Angles in radians
pii = np.pi
pist_xy = np.array([pii/6, pii/4, pii/3, pii/2, 2*pii/3, 5*pii/6, pii, 3*pii/2])
nim = np.ones_like(pist_xy)  # divide by 1 to get actual angles
varit = ['red', 'green', 'blue', 'orange', 'magenta', 'cyan', 'yellow', 'black']
text = [
    r'$\pi/6$', r'$\pi/4$', r'$\pi/3$', r'$\pi/2$', 
    r'$2\pi/3$', r'$5\pi/6$', r'$\pi$', r'$3\pi/2$'
]

x = np.cos(pist_xy / nim)
y = np.sin(pist_xy / nim)

plt.scatter(x, y, color=varit, marker='X', s=80)

for i in range(len(pist_xy)):
    plt.annotate(
        text[i],
        xy=(x[i], y[i]),
        xycoords='data',
        xytext=(+20, +5),
        textcoords='offset points',
        fontsize=12,
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")
    )

plt.show()
