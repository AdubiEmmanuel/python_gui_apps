import tkinter as tk

def button_click(symbol):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + symbol)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Simple Calculator")

display = tk.Entry(root, width=20, font=('Arial', 14))
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (symbol, row, col) in buttons:
    btn = tk.Button(root, text=symbol, width=5, height=2,
                    command=lambda s=symbol: button_click(s))
    btn.grid(row=row, column=col)

root.mainloop()
