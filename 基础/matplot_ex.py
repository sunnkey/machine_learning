import numpy as np
import matplotlib.pyplot as plt
import math

# x = np.arange(0, 2 * np.pi, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# plt.plot(x, y1, ls=":", lw=4, c="gold", alpha=0.5)
# plt.plot(x, y2, ls="--")
#
# plt.show()

# x = np.arange(1, 20)
# y = x * 1.2 + 1
# plt.xticks(range(0, 20))
# plt.yticks(range(0, 100))
#
# plt.plot(x, y, linestyle=":", linewidth=3, color="#060606", label="x")
# plt.legend(loc=1)
# plt.show()

# 绘制二次函数图像  x=-5:5  y=x**2
x = np.arange(-5, 5.1, 0.1)
y = x ** 2
ax = plt.gca()
ax_left = ax.spines["left"]
ax_left.set_position(("data", 0))
ax_bottom = ax.spines["bottom"]
ax_bottom.set_position(("data", 0))
ax.spines["right"].set_color("None")
ax.spines["top"].set_color("None")

x_ticks = np.array([-2, 1, 4])
y_ticks = x_ticks ** 2
plt.plot(x, y)
plt.scatter(x_ticks, y_ticks, marker="o", s=15, edgecolors="red", facecolor="blue")
plt.show()
