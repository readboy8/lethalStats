import tkinter as tk
import json
from tkinter import ttk
import pickle


def latest_run_money():
    moon = set_moon_field.get()
    if moon == '':
        print('Invalid Moon')
    else:
        credits = set_money_field.get()
        totalCredits[moon] += int(credits)
        print(totalCredits)
        set_money_field.delete(0, 'end')


def save():
    #save_json = json.dumps(totalCredits, indent=4)
    with open("./saves/totalCredits.lethalStat", "wb") as outfile:
        pickle.dump(totalCredits, outfile)


def load():
    loaded_object = {'Experimentation': 0, 'Assurance': 0, 'Vow': 0, 'Offense': 0, 'March': 0, 'Adamance': 0, 'Rend': 0,
                     'Dine': 0, 'Titan': 0, 'Artifice': 0, 'Embrion': 0}

    with open("./saves/totalCredits.lethalstat", "rb") as openfile:
        loaded_object = pickle.load(openfile)
    exp = loaded_object['Experimentation']
    ass = loaded_object['Assurance']
    vow = loaded_object['Vow']
    off = loaded_object['Offense']
    mar = loaded_object['March']
    ada = loaded_object['Adamance']
    ren = loaded_object['Rend']
    din = loaded_object['Dine']
    tit = loaded_object['Titan']
    art = loaded_object['Artifice']
    emb = loaded_object['Embrion']

    totalCredits['Experimentation'] = exp
    totalCredits['Assurance'] = ass
    totalCredits['Vow'] = vow
    totalCredits['Offense'] = off
    totalCredits['March'] = mar
    totalCredits['Adamance'] = ada
    totalCredits['Rend'] = ren
    totalCredits['Dine'] = din
    totalCredits['Titan'] = tit
    totalCredits['Artifice'] = art
    totalCredits['Embrion'] = emb


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

# JSON save button
save_button = ttk.Button(mainframe, text='Save', command=save)
save_button.grid(row=0, column=3, pady=10, sticky='NWES')

# JSON load button
load_button = ttk.Button(mainframe, text='Load', command=load)
load_button.grid(row=0, column=4, pady=10, sticky='NWES')

root.mainloop()
