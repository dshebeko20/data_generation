import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Заданиие заголовка диаграммы и меток осей.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squae of Value", fontsize=14)

# Задание рамера шрита делений на сосях.
ax.tick_params(labelsize=14)

plt.show()