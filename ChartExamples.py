# Примеры построения графиков

import tkinter as tk


# Функция закрытия программы
def do_close():
    window.destroy()


# Создание главного окна
window = tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")
window.resizable(False, False)

# Добавление кнопки закрытия программы
btn_close = tk.Button(window, text="Закрыть", font=("Helvetica", 10, "bold"), command=do_close)
btn_close.place(x=330, y=400, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()
