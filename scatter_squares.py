import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Заданиие заголовка диаграммы и меток осей.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squae of Value", fontsize=14)

# Задание диапазона для каждой оси.
ax.axis([0, 1100, 0, 1_000_000])
ax.ticklabel_format(style='plain')

plt.show()