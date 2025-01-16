#Примеры построения графиков  
import tkinter as tk

# Функция закрытия окна
def do_close():
    window.destroy()

# Создание главного окна
window=tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close) # фонт - выделить кнопку, жирный+вызов ф закр окна
btnClose.place(x=330, y=400, width=90, height=30) #функция place размещает элемент в нужной точке+ширина и высота эл-та

# Запуск цикла mainloop
window.mainloop()
