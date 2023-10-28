import matplotlib.pyplot as plt
import numpy as np


def plot_chart():
    # Данные для графика
    mean = 0
    sigma = 1
    x = np.arange(-5, 5, 0.01)
    f = np.exp(-np.square((x - mean) / sigma) / 2) / (np.sqrt(2 * np.pi) * sigma)

    fig, ax = plt.subplots()
    ax.plot(x, f)

    ax.set(xlabel="X", ylabel="Y", title="Нормальное распределение")
    ax.grid()

    plt.show()


def plot_chart2():
    # Данные для графика
    mean = 1.5
    sigma = 0.7
    mean_2 = -1
    sigma_2 = 1.2
    mean_3 = 3
    sigma_3 = 0.9
    x = np.arange(-7, 7, 0.01)
    f = np.exp(-np.square((x - mean) / sigma) / 2) / (np.sqrt(2 * np.pi) * sigma)
    f_2 = np.exp(-np.square((x - mean_2) / sigma_2) / 2) / (
        np.sqrt(2 * np.pi) * sigma_2
    )
    f_3 = np.exp(-np.square((x - mean_3) / sigma_3) / 2) / (
        np.sqrt(2 * np.pi) * sigma_3
    )

    fig, ax = plt.subplots()
    ax.plot(x, f)
    ax.plot(x, f_2)
    ax.plot(x, f_3)

    ax.set(xlabel="X", ylabel="Y", title="Нормальное распределение")
    ax.grid()

    plt.show()
