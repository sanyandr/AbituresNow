import tkinter as tk
from tkinter import ttk

# Создаем главное окно
window = tk.Tk()
window.title("AbituresNow")

# Создаем менеджер вкладок
tab_control = ttk.Notebook(window)

# Создаем первую вкладку
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Критерии")

# Создаем вторую вкладку
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Полный список")

# Создаем переменную для хранения выбранного значения из dropdown меню
selected_value = tk.StringVar()

# Создаем dropdown меню на первой вкладке
dropdown = ttk.Combobox(tab1, textvariable=selected_value)
dropdown["values"] = ("ИВТ", "ПРИ", "ИСТ", "МКН", "РФ")
dropdown.pack(padx=10, pady=10)

# Создаем функцию для расчета и вывода массива строк на второй вкладке
def calculate():
    # Получаем выбранное значение из dropdown меню
    value = selected_value.get()
    # Создаем массив строк на основе выбранного значения
    array = [value + str(i) for i in range(1, 11)]
    # Очищаем поле для вывода на второй вкладке
    output.delete("1.0", tk.END)
    # Выводим массив строк на второй вкладке
    output.insert(tk.END, "\n".join(array))

# Создаем кнопку Calculate на первой вкладке
button = tk.Button(tab1, text="Calculate", command=calculate)
button.pack(padx=10, pady=10)

# Создаем поле для вывода на второй вкладке
output = tk.Text(tab2)
output.pack(padx=10, pady=10)

# Размещаем менеджер вкладок на главном окне
tab_control.pack(expand=1, fill="both")

# Запускаем главный цикл приложения
window.mainloop()