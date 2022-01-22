from cgitb import text
from distutils.command.config import config
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)



class Load_Profile_Analyser:
    def __init__(self, master, country, csv_path):
        self.master = master
        self.csv_path = csv_path
        self.country = country
        self.data_frame = pd.read_csv(self.csv_path)
        self.power_consumption = np.array(self.data_frame['power'])
        self.data_frame.time = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        self.time = self.data_frame['time']
        
        #GUI STUFF
        self.graph = LabelFrame(self.master, text="Load Profile", padx=20, pady=20, height=600, width=550)
        self.results = LabelFrame(self.master, text="Results")
        self.heading = Label(self.master, text="Load Profile Analysis", font=(('Helvetiva', 20)))
        self.heading.grid(row=1, column=0, columnspan=2)
        self.heading2 = Label(self.master, text=self.country, font=(('Helvetiva', 20)))
        self.heading2.grid(row=2, column=0, columnspan=2)
        self.graph.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
        #self.lbl = Label(self.graph, text="WILL BE REPLACED BY GRAPHS")
        #self.lbl.pack()
        self.results = LabelFrame(self.master, text="Results", padx=20, pady=20)
        self.results.grid(row=4, column=0, padx=10, pady=20)
        self.btn_analyse = Button(self.master, text="Analyse", padx=30, pady=30, command=self.analyse_handler)
        self.btn_analyse.grid(row=4, column=1, padx=10, pady=10)
        self.data = self.load_profile_analysis(self.power_consumption)
        #RESULT LABELS:
        self.energy_gen = Label(self.results, text="Energy Gerneratedin 24 hours: ")
        self.max_demand = Label(self.results, text='Max Demand:  ')
        self.energy_consumed = Label(self.results, text="Average Energy Consumed in 24 hours: " )
        self.load_factor = Label(self.results, text='Load Factor: ' )

        self.energy_gen.pack()
        self.max_demand.pack()
        self.energy_consumed.pack()
        self.load_factor.pack()

    def load_profile_analysis(self, power_consumption):
        sorted_power_consumption = sorted(power_consumption, reverse=True)
        energy_generated = sum(power_consumption)
        
        return (
            energy_generated,
            sorted_power_consumption[0],
            sum(power_consumption)/len(power_consumption),
            energy_generated/(sorted_power_consumption[0]*24)
             )
        
    def load_profile(self):
        fig = Figure(figsize = (5, 5),
                 dpi = 100)
        plot1 = fig.add_subplot(111)
        plot1.plot(self.data_frame['time'], self.data_frame['power'])
        canvas = FigureCanvasTkAgg(fig,
                               master = self.graph)
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas,
                                   self.graph)
        toolbar.update()
        canvas.get_tk_widget().pack()
        

    def analyse_handler(self):
        self.energy_gen.config(text="Energy Gerneratedin 24 hours: {0} MWh".format(self.data[0]))
        self.max_demand.config(text='Max Demand: {0} MW'.format(self.data[1]))
        self.energy_consumed.config(text="Average Energy Consumed in 24 hours: {0}".format(self.data[2]))
        self.load_factor.config(text='Load Factor: {0}'.format(self.data[3]) )
        self.load_profile()


