import matplotlib.pyplot as plt
import numpy as np

apple_sales = [23, 34, 23, 23, 21, 14]
orange_sales = [25, 12, 22, 28, 31, 25]
x = np.arange(1, 7)

plt.figure(figsize=(5, 3), dpi=80)
plt.bar(
    x - 0.2,
    apple_sales,
    0.4,
    color="green",
    label="apples sales situation",
)
plt.bar(
    x + 0.2,
    orange_sales,
    0.4,
    color="gold",
    label="oranges sales situation",
)
plt.ylim(0, 45)

plt.legend()
plt.show()
