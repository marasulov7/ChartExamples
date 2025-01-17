#Примеры построения графиков  
import tkinter as tk
#импорт внешних файлов
import chart1

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

# Добавление кнопки и метки для графика 1
btn_chart1 = tk.Button(window, text="График 1", font = ('Helvetica', 10, 'bold'), command=chart1.plot_chart)
btn_chart1.place(x=40, y=115, width=90, height=30)

lbl_chart1 = tk.Label(text="График синуса matplotlib")
lbl_chart1.place(x=170, y=122)


# Добавление кнопки и метки для графика 2
btn_chart2 = tk.Button(window, text="График 2", font = ('Helvetica', 10, 'bold'))
btn_chart2.place(x=40, y=165, width=90, height=30)

lbl_chart2 = tk.Label(text="Нормальное распределение")
lbl_chart2.place(x=170, y=172)

# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close) # шрифт, размер, жирный+вызов ф закр окна
btnClose.place(x=330, y=400, width=90, height=30) #функция place размещает элемент в нужной точке+ширина и высота эл-та

# Запуск цикла mainloop
window.mainloop()
