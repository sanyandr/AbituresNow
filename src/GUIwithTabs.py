from tkinter import *
from tkinter import ttk

# Создаем окно
window = Tk()
window.title("AbituresNow")

# Создаем виджет Notebook для управления вкладками
tabsystem = ttk.Notebook(window)

# Создаем две вкладки с помощью виджета Frame
tab1 = Frame(tabsystem)
tab2 = Frame(tabsystem)

# Добавляем вкладки в Notebook с текстом
tabsystem.add(tab1, text="Show full rate")
tabsystem.add(tab2, text="Filtered abitures")

# Располагаем Notebook на окне
tabsystem.pack(expand=1, fill="both")

# Создаем поле для вывода текста на первой вкладке
text_field = Text(tab1)
text_field.pack(expand=1, fill="both")

# Создаем кнопку Calculate на первой вкладке
button = Button(tab1, text="Calculate")
button.pack(side=BOTTOM)

# Создаем какой-то контент на второй вкладке (например, список)
listbox = Listbox(tab2)
listbox.insert(1, "Абитуриент 1")
listbox.insert(2, "Абитуриент 2")
listbox.insert(3, "Абитуриент 3")
listbox.pack(expand=1, fill="both")
# Создаем ячейку для вывода количества студентов на обеих вкладках
label = Label(tab2, text="Количество студентов: 3", bg="lightgrey", relief="ridge")
label.place(relx = "0.1", rely = "0.9")

# Создаем ячейку для вывода количества студентов на второй вкладке
label = Label(tab1, text="Количество студентов: 3", bg="lightgrey", relief="ridge")
label.place(relx = "0.1", rely = "0.9")

# Запускаем главный цикл окна
window.mainloop()