import tkinter as tk
from tkinter import ttk


class App():
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry('500x500')
        self.root.title('LethalStats')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        self.root.mainloop()


if __name__ == '__main__':
    App()