import tkinter as tk
from tkinter import ttk

totalCredits = {
    'Experimentation': 0,
    'Assurance': 0,
    'Vow': 0,
    'Offense': 0,
    'March': 0,
    'Adamance': 0,
    'Rend': 0,
    'Dine': 0,
    'Titan': 0,
    'Artifice': 0,
    'Embrion': 0
}

class App():

    def set_moon(self):
        current_moon = self.set_moon_field.get()
        self.top_text.config(text=current_moon)

    def latest_run_money(self):
        totalCredits["placeholder"] += 1
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry('1000x500')
        self.root.title('LethalStats')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        #title
        self.top_text = ttk.Label(self.mainframe, text='LethalStats', background='white', font=('Arial', 30))
        self.top_text.grid(row=0, column=0)

        #moon selector
        moon_options = ['Experimentation', 'Assurance', 'Vow', 'Offense', 'March', 'Adamance', 'Rend', 'Dine', 'Titan', 'Artifice', 'Embrion']
        self.set_moon_field = ttk.Combobox(self.mainframe, values=moon_options, state='readonly')
        self.set_moon_field.grid(row=1, column=0, sticky='NWES', pady=10)
        set_moon_button = ttk.Button(self.mainframe, text='Set Moon', command=self.set_moon)
        set_moon_button.grid(row=1, column=1, pady=10)


        #Input money from last run
        self.money_input_text = ttk.Label(self.mainframe, text='Credits On Last Run', background='white', font=('Arial', 10))
        self.money_input_text.grid(row=3, column=2)
        self.set_money_field = ttk.Entry(self.mainframe)
        self.set_money_field.grid(row=3, column=0, pady=10, sticky='NWES')
        set_latest_credits_button = ttk.Button(self.mainframe, text='Confirm', command=self.latest_run_money)
        set_latest_credits_button.grid(row=3, column=1, pady=10)

        self.root.mainloop()
        return


if __name__ == '__main__':
    App()
