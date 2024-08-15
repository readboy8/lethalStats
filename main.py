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

totalVisits = {
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


class App:
    def __init__(self):

        def load():
            def load1():
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

                update(set_moon_field.get(), 'money')

            def load2():
                with open("./saves/totalDeaths.lethalstat", "rb") as openfile:
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

                update(set_moon_field.get(), 'deaths')

            def load3():
                with open("./saves/totalVisits.lethalstat", "rb") as openfile:
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

                totalVisits['Experimentation'] = exp
                totalVisits['Assurance'] = ass
                totalVisits['Vow'] = vow
                totalVisits['Offense'] = off
                totalVisits['March'] = mar
                totalVisits['Adamance'] = ada
                totalVisits['Rend'] = ren
                totalVisits['Dine'] = din
                totalVisits['Titan'] = tit
                totalVisits['Artifice'] = art
                totalVisits['Embrion'] = emb

                update(set_moon_field.get(), 'visits')

            load1()
            load2()
            load3()
            average_deaths()
            average_credit()

        def latest_run_deaths():
            moon = set_moon_field.get()
            if moon == '':
                print('Invalid Moon')
            else:
                deaths = set_deaths_field.get()
                totalDeaths[moon] += int(deaths)
                print(totalDeaths)
                set_deaths_field.delete(0, 'end')

            update(set_moon_field.get(), 'deaths')
            average_deaths()
            average_credit()

        def latest_run_money():
            moon = set_moon_field.get()
            if moon == '':
                print('Invalid Moon')
            else:
                credits = set_money_field.get()
                totalCredits[moon] += int(credits)
                print(totalCredits)
                set_money_field.delete(0, 'end')

            update(set_moon_field.get(), 'money')
            average_deaths()
            average_credit()

        def save():
            with open("./saves/totalCredits.lethalStat", "wb") as outfile:
                pickle.dump(totalCredits, outfile)
            with open("./saves/totalDeaths.lethalStat", "wb") as outfile:
                pickle.dump(totalDeaths, outfile)
            with open("./saves/totalVisits.lethalStat", "wb") as outfile:
                pickle.dump(totalVisits, outfile)

        def update(moon, reason):
            cmoon = moon
            if moon == 'Experimentation':
                if reason == 'money':
                    moon = totalCredits['Experimentation']
                elif reason == 'deaths':
                    moon = totalDeaths['Experimentation']
                elif reason == 'visits':
                    moon = totalVisits['Experimentation']
                cmoon = 'Experimentation'
            elif moon == 'Assurance':
                if reason == 'money':
                    moon = totalCredits['Assurance']
                elif reason == 'deaths':
                    moon = totalDeaths['Assurance']
                elif reason == 'visits':
                    moon = totalVisits['Assurance']
                cmoon = 'Assurance'
            elif moon == 'Vow':
                if reason == 'money':
                    moon = totalCredits['Vow']
                elif reason == 'deaths':
                    moon = totalDeaths['Vow']
                elif reason == 'visits':
                    moon = totalVisits['Vow']
                cmoon = 'Vow'
            elif moon == 'Offense':
                if reason == 'money':
                    moon = totalCredits['Offense']
                elif reason == 'deaths':
                    moon = totalDeaths['Offense']
                elif reason == 'visits':
                    moon = totalVisits['Offense']
                cmoon = 'Offense'
            elif moon == 'March':
                if reason == 'money':
                    moon = totalCredits['March']
                elif reason == 'deaths':
                    moon = totalDeaths['March']
                elif reason == 'visits':
                    moon = totalVisits['March']
                cmoon = 'March'
            elif moon == 'Adamance':
                if reason == 'money':
                    moon = totalCredits['Adamance']
                elif reason == 'deaths':
                    moon = totalDeaths['Adamance']
                elif reason == 'visits':
                    moon = totalVisits['Adamance']
                cmoon = 'Adamance'
            elif moon == 'Rend':
                if reason == 'money':
                    moon = totalCredits['Rend']
                elif reason == 'deaths':
                    moon = totalDeaths['Rend']
                elif reason == 'visits':
                    moon = totalVisits['Rend']
                cmoon = 'Rend'
            elif moon == 'Dine':
                if reason == 'money':
                    moon = totalCredits['Dine']
                elif reason == 'deaths':
                    moon = totalDeaths['Dine']
                elif reason == 'visits':
                    moon = totalVisits['Dine']
                cmoon = 'Dine'
            elif moon == 'Titan':
                if reason == 'money':
                    moon = totalCredits['Titan']
                elif reason == 'deaths':
                    moon = totalDeaths['Titan']
                elif reason == 'visits':
                    moon = totalVisits['Titan']
                cmoon = 'Titan'
            elif moon == 'Artifice':
                if reason == 'money':
                    moon = totalCredits['Artifice']
                elif reason == 'deaths':
                    moon = totalDeaths['Artifice']
                elif reason == 'visits':
                    moon = totalVisits['Artifice']
                cmoon = 'Artifice'
            elif moon == 'Embrion':
                if reason == 'money':
                    moon = totalCredits['Embrion']
                elif reason == 'deaths':
                    moon = totalDeaths['Embrion']
                elif reason == 'visits':
                    moon = totalVisits['Embrion']
                cmoon = 'Embrion'

            if reason == 'money':
                selected_moon_total_txt_var.set("Total Credits: " + str(moon))
            elif reason == 'deaths':
                selected_moon_total_deaths_txt_var.set("Total Deaths: " + str(moon))
            elif reason == 'visits':
                total_attempts_text_var.set("Total Attempts: " + str(moon))

            current_moon_text_var.set(cmoon)

        def plus_attempt():
            moon = set_moon_field.get()
            if moon == '':
                print("Invalid Moon")
            else:
                totalVisits[moon] += 1
                print(totalVisits)
                total_attempts_text_var.set("Total Attempts: " + str(totalVisits[moon]))
                average_deaths()
                average_credit()

        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.geometry('550x250')
        self.root.iconbitmap('lethalstatslogo.ico')
        self.root.title('LethalStats')
        self.mainframe = tk.Frame(background='white')
        self.mainframe.pack(fill='both', expand=True)

        # Save button
        save_button = ttk.Button(self.mainframe, text='Save', command=save)
        save_button.grid(row=0, column=3, pady=10, sticky='E')

        # Load button
        load_button = ttk.Button(self.mainframe, text='Load', command=load)
        load_button.grid(row=0, column=4, pady=10, sticky='W')

        top_text = ttk.Label(self.mainframe, text='Select Moon', background='white', font=('Arial', 18))
        top_text.grid(row=0, column=0, sticky='W')

        # Moon selection
        moon_options = ['Experimentation', 'Assurance', 'Vow', 'Offense', 'March', 'Adamance', 'Rend', 'Dine', 'Titan',
                        'Artifice', 'Embrion']
        set_moon_field = ttk.Combobox(self.mainframe, values=moon_options, state='readonly', width=29)
        set_moon_field.grid(row=1, column=0, sticky='W', pady=10)

        def set_moon(event):
            selected_moon = set_moon_field.get()
            print(selected_moon)
            update(set_moon_field.get(), 'money')
            update(set_moon_field.get(), 'deaths')
            update(set_moon_field.get(), 'visits')
            set_deaths_field.delete(0, 'end')
            set_money_field.delete(0, 'end')
            average_credits_text_var.set("Average Credits: 0")
            average_deaths_text_var.set("Average Deaths: 0")
            average_deaths()
            average_credit()

        set_moon_field.bind("<<ComboboxSelected>>", set_moon)

        # Input money from last run
        money_input_text = ttk.Label(self.mainframe, text='Credits On Last Run', background='white', font=('Arial', 10))
        money_input_text.grid(row=3, column=0, sticky='W')
        set_money_field = ttk.Entry(self.mainframe)
        set_money_field.grid(row=4, column=0, sticky='WE')
        set_latest_credits_button = ttk.Button(self.mainframe, text='Confirm', command=latest_run_money)
        set_latest_credits_button.grid(row=4, column=1, sticky='WE')

        # Input deaths from last run
        deaths_input_text = ttk.Label(self.mainframe, text='Deaths On Last Run', background='white', font=('Arial', 10))
        deaths_input_text.grid(row=3, column=2, sticky='W')
        set_deaths_field = ttk.Entry(self.mainframe)
        set_deaths_field.grid(row=4, column=2, sticky='WE')
        set_latest_credits_button = ttk.Button(self.mainframe, text='Confirm', command=latest_run_deaths)
        set_latest_credits_button.grid(row=4, column=3, sticky='WE')

        # Total money from selected moon
        selected_moon_total_txt_var = tk.StringVar()
        selected_moon_total_txt_var.set("Total Credits: ")
        spacer_1 = ttk.Label(self.mainframe, background='white')
        spacer_1.grid(row=5, column=0)
        selected_moon_total = ttk.Label(self.mainframe, textvariable=selected_moon_total_txt_var, background='white',
                                        font=('Arial', 10))
        selected_moon_total.grid(row=7, column=0, sticky='W')

        # Total deaths from selected moon
        selected_moon_total_deaths_txt_var = tk.StringVar()
        selected_moon_total_deaths_txt_var.set("Total Deaths: ")
        selected_moon_total_deaths = ttk.Label(self.mainframe, textvariable=selected_moon_total_deaths_txt_var,
                                               background='white',
                                               font=('Arial', 10))
        selected_moon_total_deaths.grid(row=8, column=0, sticky='W')

        # current moon text
        current_moon_text_var = tk.StringVar()
        current_moon_text_var.set("")
        current_moon_text = ttk.Label(self.mainframe, textvariable=current_moon_text_var, background='white',
                                      font=('Arial', 18))
        current_moon_text.grid(row=6, column=0, sticky='W')

        # plus one attempt button
        total_attempts_text_var = tk.StringVar()
        total_attempts_text_var.set('Total Attempts: ')
        plus_attempt = ttk.Button(self.mainframe, text='+1 Attempt', command=plus_attempt)
        plus_attempt.grid(row=4, column=4)
        total_attempts = ttk.Label(self.mainframe, textvariable=total_attempts_text_var, background='white')
        total_attempts.grid(row=9, column=0, sticky='W')

        # Average deaths
        def average_deaths():
            moon = set_moon_field.get()
            average_death = totalDeaths[moon] / totalVisits[moon]
            average_death = round(average_death, 0)
            average_deaths_text_var.set("Average Deaths: " + str(average_death))
            print(average_death)

        average_deaths_text_var = tk.StringVar()
        average_deaths_text_var.set("Average Deaths: ")
        average_deaths_label = ttk.Label(self.mainframe, textvariable=average_deaths_text_var, background='white')
        average_deaths_label.grid(row=8, column=2, sticky='W')

        # Average credit
        def average_credit():
            moon = set_moon_field.get()
            average_credits = totalCredits[moon] / totalVisits[moon]
            average_credits = round(average_credits, 0)
            average_credits_text_var.set("Average Credits: " + str(average_credits))
            print(average_credits)

        average_credits_text_var = tk.StringVar()
        average_credits_text_var.set("Average Credits: ")
        average_credits_label = ttk.Label(self.mainframe, textvariable=average_credits_text_var, background='white')
        average_credits_label.grid(row=7, column=2, sticky='W')

        self.root.mainloop()
        return


if __name__ == "__main__":
    App()
