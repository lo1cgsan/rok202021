# Tutaj pisz swój kod, młody padawanie ;-)
import numpy as np
import matplotlib.pyplot as plt

x = [2, 8, 6, 2]
y = [11, 23, 14, 11]

plt.yticks(range(10, 25))
plt.grid()
plt.plot(x, y)

punkt = (5, 15)
plt.plot(punkt[0], punkt[1], "ro")
plt.text(punkt[0] + 0.2, punkt[1], f"P ({punkt[0]}, {punkt[1]})")
