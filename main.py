import tkinter as tk
from tkinter import ttk
import pickle

expTotal = 0
assTotal = 0
vowTotal = 0
offTotal = 0
marTotal = 0
adaTotal = 0
renTotal = 0
dinTotal = 0
titTotal = 0
artTotal = 0
embTotal = 0

expDeaths = 0
assDeaths = 0
vowDeaths = 0
offDeaths = 0
marDeaths = 0
adaDeaths = 0
renDeaths = 0
dinDeaths = 0
titDeaths = 0
artDeaths = 0
embDeaths = 0

selected_moon = ""

totalDeaths = {
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
    def __init__(self):

        def latest_run_deaths():
            moon = set_moon_field.get()
            if moon == '':
                print('Invalid Moon')
            else:
                deaths = set_deaths_field.get()
                totalDeaths[moon] += int(deaths)
                print(totalDeaths)
                set_deaths_field.delete(0, 'end')
            expDeaths = totalDeaths['Experimentation']
            assDeaths = totalDeaths['Assurance']
            vowDeaths = totalDeaths['Vow']
            offDeaths = totalDeaths['Offense']
            marDeaths = totalDeaths['March']
            adaDeaths = totalDeaths['Adamance']
            renDeaths = totalDeaths['Rend']
            dinDeaths = totalDeaths['Dine']
            titDeaths = totalDeaths['Titan']
            artDeaths = totalDeaths['Artifice']
            embDeaths = totalDeaths['Embrion']

            update(set_moon_field.get(), 'death')

        def latest_run_money():
            moon = set_moon_field.get()
            if moon == '':
                print('Invalid Moon')
            else:
                credits = set_money_field.get()
                totalCredits[moon] += int(credits)
                print(totalCredits)
                set_money_field.delete(0, 'end')
            expTotal = totalCredits['Experimentation']
            assTotal = totalCredits['Assurance']
            vowTotal = totalCredits['Vow']
            offTotal = totalCredits['Offense']
            marTotal = totalCredits['March']
            adaTotal = totalCredits['Adamance']
            renTotal = totalCredits['Rend']
            dinTotal = totalCredits['Dine']
            titTotal = totalCredits['Titan']
            artTotal = totalCredits['Artifice']
            embTotal = totalCredits['Embrion']

            update(set_moon_field.get(), 'money')

        def save():
            with open("./saves/totalCredits.lethalStat", "wb") as outfile:
                pickle.dump(totalCredits, outfile)
            print('bababooey')
            with open("./saves/totalDeaths.lethalStat", "wb") as outfile:
                pickle.dump(totalDeaths, outfile)
                print('bababooey')

        def load():
            loaded_object = {'Experimentation': 0, 'Assurance': 0, 'Vow': 0, 'Offense': 0, 'March': 0, 'Adamance': 0,
                             'Rend': 0,
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

            loaded_deaths_object = {'Experimentation': 0, 'Assurance': 0, 'Vow': 0, 'Offense': 0, 'March': 0,
                                    'Adamance': 0,
                                    'Rend': 0,
                                    'Dine': 0, 'Titan': 0, 'Artifice': 0, 'Embrion': 0}
            with open("./saves/totalDeaths.lethalStat", "rb") as outfile:
                loaded_deaths_object = pickle.load(openfile)
            exp = loaded_deaths_object['Experimentation']
            ass = loaded_deaths_object['Assurance']
            vow = loaded_deaths_object['Vow']
            off = loaded_deaths_object['Offense']
            mar = loaded_deaths_object['March']
            ada = loaded_deaths_object['Adamance']
            ren = loaded_deaths_object['Rend']
            din = loaded_deaths_object['Dine']
            tit = loaded_deaths_object['Titan']
            art = loaded_deaths_object['Artifice']
            emb = loaded_deaths_object['Embrion']

            totalDeaths['Experimentation'] = exp
            totalDeaths['Assurance'] = ass
            totalDeaths['Vow'] = vow
            totalDeaths['Offense'] = off
            totalDeaths['March'] = mar
            totalDeaths['Adamance'] = ada
            totalDeaths['Rend'] = ren
            totalDeaths['Dine'] = din
            totalDeaths['Titan'] = tit
            totalDeaths['Artifice'] = art
            totalDeaths['Embrion'] = emb

            update(set_moon_field.get(), 'no reason')

        def update(moon, reason):
            cmoon = moon
            if moon == 'Experimentation':
                if reason == 'money':
                    moon = totalCredits['Experimentation']
                else:
                    moon = totalDeaths['Experimentation']
                cmoon = 'Experimentation'
            elif moon == 'Assurance':
                if reason == 'money':
                    moon = totalCredits['Assurance']
                else:
                    moon = totalDeaths['Assurance']
                cmoon = 'Assurance'
            elif moon == 'Vow':
                if reason == 'money':
                    moon = totalCredits['Vow']
                else:
                    moon = totalDeaths['Vow']
                cmoon = 'Vow'
            elif moon == 'Offense':
                if reason == 'money':
                    moon = totalCredits['Offense']
                else:
                    moon = totalDeaths['Offense']
                cmoon = 'Offense'
            elif moon == 'March':
                if reason == 'money':
                    moon = totalCredits['March']
                else:
                    moon = totalDeaths['March']
                cmoon = 'March'
            elif moon == 'Adamance':
                if reason == 'money':
                    moon = totalCredits['Adamance']
                else:
                    moon = totalDeaths['Adamance']
                cmoon = 'Adamance'
            elif moon == 'Rend':
                if reason == 'money':
                    moon = totalCredits['Rend']
                else:
                    moon == totalDeaths['Rend']
                cmoon = 'Rend'
            elif moon == 'Dine':
                if reason == 'money':
                    moon = totalCredits['Dine']
                else:
                    moon = totalDeaths['Dine']
                cmoon = 'Dine'
            elif moon == 'Titan':
                if reason == 'money':
                    moon = totalCredits['Titan']
                else:
                    moon = totalDeaths['Titan']
                cmoon = 'Titan'
            elif moon == 'Artifice':
                if reason == 'money':
                    moon = totalCredits['Artifice']
                else:
                    moon = totalDeaths['Artifice']
                cmoon = 'Artifice'
            elif moon == 'Embrion':
                if reason == 'money':
                    moon = totalCredits['Embrion']
                else:
                    moon = totalDeaths['Embrion']
                cmoon = 'Embrion'
            if reason == 'money':
                selected_moon_total_txt_var.set("Total Credits: " + str(moon))
            else:
                selected_moon_total_deaths_txt_var.set("Total Deaths: " + str(moon))
            current_moon_text_var.set(cmoon)

        self.root = tk.Tk()

        self.root.geometry('508x500')
        self.root.title('LethalStats')
        self.mainframe = tk.Frame(background='white')
        self.mainframe.pack(fill='both', expand=True)

        top_text = ttk.Label(self.mainframe, text='Select Moon', background='white', font=('Arial', 18))
        top_text.grid(row=0, column=0, sticky='W')

        # Moon selection
        moon_options = ['Experimentation', 'Assurance', 'Vow', 'Offense', 'March', 'Adamance', 'Rend', 'Dine', 'Titan',
                        'Artifice', 'Embrion']
        set_moon_field = ttk.Combobox(self.mainframe, values=moon_options, state='readonly')
        set_moon_field.grid(row=1, column=0, sticky='W', pady=10)

        def set_moon(event):
            selected_moon = set_moon_field.get()
            print(selected_moon)
            update(set_moon_field.get(), 'null')

        set_moon_field.bind("<<ComboboxSelected>>", set_moon)

        # Input money from last run
        money_input_text = ttk.Label(self.mainframe, text='Credits On Last Run', background='white', font=('Arial', 10))
        money_input_text.grid(row=3, column=0, sticky='W')
        set_money_field = ttk.Entry(self.mainframe)
        set_money_field.grid(row=4, column=0, sticky='WE')
        set_latest_credits_button = ttk.Button(self.mainframe, text='Confirm', command=latest_run_money)
        set_latest_credits_button.grid(row=4, column=1, sticky='W')

        # Input deaths from last run
        deaths_input_text = ttk.Label(self.mainframe, text='Deaths On Last Run', background='white', font=('Arial', 10))
        deaths_input_text.grid(row=3, column=2, sticky='W')
        set_deaths_field = ttk.Entry(self.mainframe)
        set_deaths_field.grid(row=4, column=2, sticky='W')
        set_latest_credits_button = ttk.Button(self.mainframe, text='Confirm', command=latest_run_deaths)
        set_latest_credits_button.grid(row=4, column=3, sticky='W')

        # Total money from selected moon
        selected_moon_total_txt_var = tk.StringVar()
        selected_moon_total_txt_var.set("Total Credits: 0")
        spacer_1 = ttk.Label(self.mainframe, background='white')
        spacer_1.grid(row=5, column=0)
        selected_moon_total = ttk.Label(self.mainframe, textvariable=selected_moon_total_txt_var, background='white',
                                        font=('Arial', 10))
        selected_moon_total.grid(row=7, column=0, sticky='W')

        # Total deaths from selected moon
        selected_moon_total_deaths_txt_var = tk.StringVar()
        selected_moon_total_deaths_txt_var.set("Total Deaths: 0")
        selected_moon_total_deaths = ttk.Label(self.mainframe, textvariable=selected_moon_total_deaths_txt_var,
                                               background='white',
                                               font=('Arial', 10))
        selected_moon_total_deaths.grid(row=8, column=0, sticky='W')

        # current moon text
        current_moon_text_var = tk.StringVar()
        current_moon_text_var.set("Select Moon")
        current_moon_text = ttk.Label(self.mainframe, textvariable=current_moon_text_var, background='white',
                                      font=('Arial', 18))
        current_moon_text.grid(row=6, column=0, sticky='W')

        # Save button
        save_button = ttk.Button(self.mainframe, text='Save', command=save)
        save_button.grid(row=0, column=3, pady=10, sticky='E')

        # Load button
        load_button = ttk.Button(self.mainframe, text='Load', command=load)
        load_button.grid(row=0, column=4, pady=10, sticky='W')

        self.root.mainloop()
        return


if __name__ == "__main__":
    App()
