import random
import pyperclip
from tkinter import *
from tkinter.ttk import Combobox, Style

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("650x300")
        self.create_widgets()

    def create_widgets(self):
        # Font and Colors
        font_style = ("Arial", 12)

        # Title
        title_label = Label(self.master, text="Password Generator", font=("Arial", 20, "bold"))
        title_label.grid(row=0, columnspan=5, pady=20)

        # Labels and Entry
        Label(self.master, text="Password", font=font_style).grid(row=4, column=1, pady=10, padx=5, sticky='E')
        self.password_entry = Entry(self.master, font=font_style)
        self.password_entry.grid(row=4, column=2, pady=10, padx=5, sticky='W')

        Label(self.master, text="Length", font=font_style).grid(row=1, column=1, pady=5, padx=5, sticky='E')
        self.length_combo = Combobox(self.master, values=list(range(8, 33)), font=font_style)
        self.length_combo.current(0)
        self.length_combo.grid(row=1, column=2, pady=5, padx=5, sticky='W')

        # Buttons
        copy_button = Button(self.master, text="Copy", command=self.copy_password, font=font_style, padx=10, pady=5, bd=2, relief="raised", cursor="hand2")
        copy_button.grid(row=4, column=3, pady=10, padx=5, sticky='W')

        generate_button = Button(self.master, text="Generate", command=self.generate_password, font=font_style, padx=10, pady=5, bd=2, relief="raised", cursor="hand2")
        generate_button.grid(row=3, column=2, pady=10, padx=5, sticky='W')

        # Radio Buttons
        self.strength_var = IntVar(value=0)
        radio_low = Radiobutton(self.master, text="Low Security", variable=self.strength_var, value=1, font=font_style) 
        radio_low.grid(row=2, column=2, pady=5, padx=5, sticky='W')

        radio_middle = Radiobutton(self.master, text="Medium Security", variable=self.strength_var, value=0, font=font_style)
        radio_middle.grid(row=2, column=3, pady=5, padx=5, sticky='W')

        radio_strong = Radiobutton(self.master, text="Strong Security", variable=self.strength_var, value=3, font=font_style)
        radio_strong.grid(row=2, column=4, pady=5, padx=5, sticky='W')

        # Center the UI
        for child in self.master.winfo_children():
            child.grid_configure(padx=10, pady=5)
        self.center_window()

    def generate_password(self):
        length = int(self.length_combo.get())
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=~`[]{}|;:,.<>/?"
        password = ""

        if self.strength_var.get() == 1:
            password = ''.join(random.choice(lower) for _ in range(length))
        elif self.strength_var.get() == 0:
            password = ''.join(random.choice(upper) for _ in range(length))
        elif self.strength_var.get() == 3:
            password = ''.join(random.choice(digits) for _ in range(length))

        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

    def copy_password(self):
        random_password = self.password_entry.get()
        pyperclip.copy(random_password)

    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x_coordinate = (self.master.winfo_screenwidth() - width) // 2
        y_coordinate = (self.master.winfo_screenheight() - height) // 2
        self.master.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


if __name__ == "__main__":
    root = Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
