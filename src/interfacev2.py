import tkinter as tk
from tkinter import ttk
import Parser
import Logic
def buildInterface():
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
    tab_control.add(tab2, text="Результат")

    # Создаем переменную для хранения выбранного значения из dropdown меню
    selected_oop = tk.StringVar()
    selected_prior = tk.IntVar()
    # Создаем dropdown меню на первой вкладке
    dropdown = ttk.Combobox(tab1, textvariable=selected_oop, width=60)
    dropdown["values"] = ("Программная инженерия", "Математика и компьютерные науки", 
                        "Конкурсная группа (ИВТ, ИСТ, ПрИ, ПИ)", "Конкурсная группа (МКН, МОАИС)", 
                        "Конкурсная группа (ПМФ, РФ)")
    dropdown.pack(padx=10, pady=10)
    dropdown1 = ttk.Combobox(tab1, textvariable=selected_prior, width=10)
    dropdown1["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    dropdown1.pack(padx=50, pady=50, side=tk.RIGHT)

    # Создаем функцию для запуска парсера
    def parse():
        oopValue = selected_oop.get()
        Parser.parseSite(oopValue)

    # Создаем функцию для расчета абитурентов по заданному приоритету
    def calculate():
        # Получаем выбранное значение из dropdown меню
        priorValue = selected_prior.get()
        calculated = Logic.calculateAbitures(priorValue)
        # Очищаем поле для вывода на второй вкладке
        output.delete("1.0", tk.END)
        # Выводим массив строк на второй вкладке
        output.insert(tk.END, calculated)
   
    # Создаем кнопку Parse на первой вкладке
    button = tk.Button(tab1, text="Parse", command=parse)
    button.pack(padx=150, pady=10, side=tk.LEFT)

    # Создаем кнопку Calculate на первой вкладке
    button = tk.Button(tab1, text="Calculate", command=calculate)
    button.pack(padx=0, pady=10, side=tk.RIGHT)

    # Создаем поле для вывода на второй вкладке
    output = tk.Text(tab2)
    output.pack(padx=10, pady=10)

    # Размещаем менеджер вкладок на главном окне
    tab_control.pack(expand=1, fill="both")

    # Запускаем главный цикл приложения
    window.mainloop()