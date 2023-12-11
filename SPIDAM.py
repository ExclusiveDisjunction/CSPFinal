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

    App = SPIDAM_App()
    App.mainloop()