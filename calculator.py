# calculator.py

import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("250x250")

        self.entry = tk.Entry(master, width=25, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_buttons()

    def create_button(self, text, row, column, command=None):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16), command=command)
        button.grid(row=row, column=column, padx=5, pady=5)

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'CE', '(', ')'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            if button == '=':
                self.create_button(button, row_val, col_val, command=self.calculate)
            elif button == 'C':
                self.create_button(button, row_val, col_val, command=self.clear)
            elif button == 'CE':
                self.create_button(button, row_val, col_val, command=self.clear_entry)
            else:
                self.create_button(button, row_val, col_val, command=lambda text=button: self.append_to_entry(text))
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def append_to_entry(self, text):
        self.entry.insert(tk.END, text)

    def clear(self):
        self.entry.delete(0, tk.END)

    def clear_entry(self):
        self.entry.delete(len(self.entry.get())-1, tk.END)

    def calculate(self):
        try:
            result = str(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()