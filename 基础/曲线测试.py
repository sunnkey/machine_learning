import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 8 * np.pi + 0.1, 0.1)
sin_x = np.sin(x)
con_x = np.cos(x / 2) / 2

plt.figure(figsize=(5, 4), dpi=120)
plt.plot(x, sin_x, color="red", label="y=sin(x)")
plt.plot(x, con_x, color="blue", label="y=cos(x)")
plt.xlim(0, 27)
plt.ylim(-1.5, 2)
plt.xticks(range(0, 28, 2))
plt.grid(linestyle=":")
plt.xlabel("x")
plt.ylabel("y")
plt.fill_between(x, sin_x, con_x, sin_x > con_x, color="green")
plt.fill_between(x, sin_x, con_x, sin_x < con_x, color="red")

plt.legend()
plt.show()
