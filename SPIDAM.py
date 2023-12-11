# SPIDAM.py
# Entry point for the SPIDAM program.

from model import Model
from view import View
from controller import Controller
import tkinter as tk

from WaveData import WaveData

import conf.Configuration as Config
import conf.Log as Log

class SPIDAM_App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title = "SPDIAM Audio Tool"
        self.geometry("500x400+400+400")
        self.resizable(True, True)

        self.waveData = WaveData()
        model = Model(self.waveData)

        view = View(self)
        view.grid(row = 0, column = 0, padx= 10, pady=10)

        controller = Controller(model, view)
        view.SetController(controller)

if __name__ == "__main__":
    Config.Configuration.Init("setup.cfg")
    Log.InitLog(level=Log.Info)
<<<<<<< HEAD
    Log.LogEvent("Starting UI")
    Log.LogEvent("<SPIDAM Program>  Copyright (C) <2023>  <Hollan Sellers, Zane Wolfe, Emilio Garcia> This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'. This is free software, and you are welcome to redistribute it under certain conditions; type `show c' for details.")

    root = tk.Tk()
    root.title("SPIDAM")
    root.geometry("500x400+400+400")
    root.resizable(True, True)

    root.grid_columnconfigure(0, weight=1)

    TitleLbl = tk.Label(root, text="SPIDAM Program", font=('Arial 20 bold'))
    SubTitleLbl = tk.Label(root, text="Please select a file to begin")
    # GrabWaveFile sets the data attribute inside waveData obj
    selfile_button = tk.Button(root, text="Select", command=GrabWaveCommand)

    TitleLbl.grid(column=0, row=0, columnspan=2)
    SubTitleLbl.grid(column=0, row=1,sticky='W')
    selfile_button.grid(column=1, row=1, sticky='E', padx=10)
=======
>>>>>>> 015fb6668fc70fd3a51fdf953b17a09760beb5dc

    App = SPIDAM_App()
    App.mainloop()