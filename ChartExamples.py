# Примеры построения графиков

import tkinter as tk

# Импорт внешних файлов
import chart_1
import chart_2


# Функция закрытия программы
def do_close():
    window.destroy()


font_btn = ("Helvetica", 10, "bold")

# Создание главного окна
window = tk.Tk()
window.geometry("450x550")
window.title("Примеры построения графиков")
window.resizable(False, False)

# Добавление метки заголовка
lbl_title = tk.Label(
    text="Примеры построения графиков", font=("Helvetica", 16, "bold"), fg="#0000cc"
)
lbl_title.place(x=55, y=25)

# Добавление кнопки и метки для графика 1
btn_chart_1 = tk.Button(
    window, text="График 1", font=font_btn, command=chart_1.plot_chart
)
btn_chart_1.place(x=40, y=115, width=90, height=30)

lbl_chart_1 = tk.Label(text="График синуса matplotlib")
lbl_chart_1.place(x=170, y=122)

# Добавление кнопки и метки для графика 2
btn_chart_2 = tk.Button(
    window, text="График 2", font=font_btn, command=chart_2.plot_chart
)
btn_chart_2.place(x=40, y=165, width=90, height=30)

lbl_chart_2 = tk.Label(text="Нормальное распределение")
lbl_chart_2.place(x=170, y=172)

# Добавление кнопки и метки для графика 3
btn_chart_3 = tk.Button(
    window, text="График 3", font=font_btn, command=chart_2.plot_chart2
)
btn_chart_3.place(x=40, y=215, width=90, height=30)

lbl_chart_3 = tk.Label(text="Нормальное распределение - 3 графика")
lbl_chart_3.place(x=170, y=222)

# Добавление кнопки и метки для графика 4
btn_chart_4 = tk.Button(window, text="График 4", font=font_btn)
btn_chart_4.place(x=40, y=265, width=90, height=30)

lbl_chart_4 = tk.Label(text="Нормальное распределение")
lbl_chart_4.place(x=170, y=272)

# Добавление кнопки и метки для графика 5
btn_chart_5 = tk.Button(window, text="График 5", font=font_btn)
btn_chart_5.place(x=40, y=315, width=90, height=30)

lbl_chart_5 = tk.Label(text="Нормальное распределение")
lbl_chart_5.place(x=170, y=322)

# Добавление кнопки и метки для графика 6
btn_chart_6 = tk.Button(window, text="График 6", font=font_btn)
btn_chart_6.place(x=40, y=365, width=90, height=30)

lbl_chart_6 = tk.Label(text="Нормальное распределение")
lbl_chart_6.place(x=170, y=372)

# Добавление кнопки и метки для графика 7
btn_chart_7 = tk.Button(window, text="График 7", font=font_btn)
btn_chart_7.place(x=40, y=415, width=90, height=30)

lbl_chart_7 = tk.Label(text="Нормальное распределение")
lbl_chart_7.place(x=170, y=422)

# Добавление кнопки закрытия программы
btn_close = tk.Button(window, text="Закрыть", font=font_btn, command=do_close)
btn_close.place(x=330, y=500, width=90, height=30)


# Запуск цикла mainloop
window.mainloop()
