# Примеры построения графиков

import tkinter as tk

from numpy import place


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

# Добавление кнопки закрытия программы
btn_close = tk.Button(
    window, text="Закрыть", font=("Helvetica", 10, "bold"), command=do_close
)
btn_close.place(x=330, y=400, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()
