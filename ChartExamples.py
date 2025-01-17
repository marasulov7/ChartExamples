#Примеры построения графиков  
import tkinter as tk

# Функция закрытия окна
def do_close():
    window.destroy()

# Создание главного окна
window=tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

# Добавление метки заголовка
lbl_title = tk.Label(text="Примеры построения графиков", font=('Helvetica', 16, 'bold'), fg='#0000cc') #fg-цвет текста
lbl_title.place(x=55, y=25)

# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close) # шрифт, размер, жирный+вызов ф закр окна
btnClose.place(x=330, y=400, width=90, height=30) #функция place размещает элемент в нужной точке+ширина и высота эл-та

# Запуск цикла mainloop
window.mainloop()
