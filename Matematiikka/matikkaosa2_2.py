import numpy as np
import matplotlib.pyplot as plt


X = np.linspace(-3*np.pi, 3*np.pi, 1000)


C, S = np.cos(X), np.sin(X)


plt.figure(figsize=(19.2, 14.4))  


plt.plot(X, C, color='royalblue', linestyle='-.', label='cos(x)')
plt.plot(X, S, color='darkorange', linestyle='--', label='sin(x)')


xticks = np.linspace(-3*np.pi, 3.5*np.pi, 13)
xtick_labels = [
    r'$-3\pi$', r'$-\frac{5\pi}{2}$', r'$-2\pi$', r'$-\frac{3\pi}{2}$',
    r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$',
    r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$', r'$\frac{5\pi}{2}$', r'$3\pi$'
]
plt.xticks(xticks, xtick_labels)

# Y-akselin merkit
plt.yticks([-1, -0.5, 0, 0.5, 1])



plt.legend()

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()