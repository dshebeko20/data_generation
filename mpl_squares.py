import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Задание заголовка диаграмы и меток осей.
ax.set_title("Square numbers", fontsize=40)
ax.set_xlabel("Value", fontsize=20)
ax.set_ylabel("Square of value", fontsize=20)

# Задание размера шрифта делений на осях.
ax.tick_params(labelsize=20)

plt.show()