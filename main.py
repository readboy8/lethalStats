import tkinter as tk
import json
from tkinter import ttk
import re

selected_moon = ""

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

def latest_run_money():
    moon = set_moon_field.get()
    if moon == '':
        print('Invalid Moon')
    else:
        credits = set_money_field.get()
        totalCredits[moon] += int(credits)
        print(totalCredits)
        set_money_field.delete(0, 'end')


root = tk.Tk()

root.geometry('1000x500')
root.title('LethalStats')
mainframe = tk.Frame(root, background='white')
mainframe.pack(fill='both', expand=True)

# title
top_text = ttk.Label(mainframe, text='Select Moon', background='white', font=('Arial', 30))
top_text.grid(row=0, column=0)

# selector
moon_options = ['Experimentation', 'Assurance', 'Vow', 'Offense', 'March', 'Adamance', 'Rend', 'Dine', 'Titan',
                'Artifice', 'Embrion']
set_moon_field = ttk.Combobox(mainframe, values=moon_options, state='readonly')
set_moon_field.grid(row=1, column=0, sticky='NWES', pady=10)


def set_moon(event):
    selected_moon = set_moon_field.get()
    print(selected_moon)


set_moon_field.bind("<<ComboboxSelected>>", set_moon)

# Input money from last run
money_input_text = ttk.Label(mainframe, text='Credits On Last Run', background='white', font=('Arial', 10))
money_input_text.grid(row=3, column=2)
set_money_field = ttk.Entry(mainframe)
set_money_field.grid(row=3, column=0, pady=10, sticky='NWES')
set_latest_credits_button = ttk.Button(mainframe, text='Confirm', command=latest_run_money)
set_latest_credits_button.grid(row=3, column=1, pady=10)

root.mainloop()
