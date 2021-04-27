import matplotlib.pyplot as plt

# A=(-1;-2), B=(7;2), C=(2;4)
x = [-1, 7, 2, -1]
y = [-2, 2, 4, -2]

plt.title("Trójkąt")
plt.text(-1.3, -1.8, "A (-1,-2)", size="14")
plt.text(6.5, 2.3, "B (7,2)", size="14")
plt.text(1.5, 4.3, "C (2,4)", size="14")
plt.grid()
plt.plot(x, y, "go:")
plt.plot(0, 0, "ro")
plt.show()


