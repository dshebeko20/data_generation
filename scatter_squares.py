import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Заданиие заголовка диаграммы и меток осей.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squae of Value", fontsize=14)

# Задание рамера шрита делений на сосях.
ax.tick_params(labelsize=14)

plt.show()