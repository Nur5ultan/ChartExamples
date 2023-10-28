# Примеры построения графиков

import tkinter as tk

# Импорт внешних файлов
import chart_1
import chart_2


# Функция закрытия программы
def do_close():
    window.destroy()


# Создание главного окна
window = tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")
window.resizable(False, False)

# Добавление метки заголовка
lbl_title = tk.Label(
    text="Примеры построения графиков", font=("Helvetica", 16, "bold"), fg="#0000cc"
)
lbl_title.place(x=55, y=25)

# Добавление кнопки и метки для графика 1
btn_chart_1 = tk.Button(
    window, text="График 1", font=("Helvetica", 10, "bold"), command=chart_1.plot_chart
)
btn_chart_1.place(x=40, y=115, width=90, height=30)

lbl_chart_1 = tk.Label(text="График синуса matplotlib")
lbl_chart_1.place(x=170, y=122)

# Добавление кнопки и метки для графика 2
btn_chart_2 = tk.Button(
    window, text="График 2", font=("Helvetica", 10, "bold"), command=chart_2.plot_chart
)
btn_chart_2.place(x=40, y=165, width=90, height=30)

lbl_chart_2 = tk.Label(text="Нормальное распределение")
lbl_chart_2.place(x=170, y=172)

# Добавление кнопки закрытия программы
btn_close = tk.Button(
    window, text="Закрыть", font=("Helvetica", 10, "bold"), command=do_close
)
btn_close.place(x=330, y=400, width=90, height=30)


# Запуск цикла mainloop
window.mainloop()
