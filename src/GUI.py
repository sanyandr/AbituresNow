import tkinter as tk

def on_button_click():
    # Здесь можно добавить действие при нажатии на кнопку
    pass

root = tk.Tk()                                                  ##define tk widget
text = tk.Text(root)                                            ##define main textbox
text.pack(expand=True, fill=tk.BOTH)                            ##set pos of textbox

button = tk.Button(root, text="Calculate", command=on_button_click)     ##define calc button on bottom of widget
button.pack(side=tk.BOTTOM)


root.mainloop()