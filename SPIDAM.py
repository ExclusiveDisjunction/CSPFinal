import tkinter as tk
from tkinter import N, S, E, W, EW
from tkinter import messagebox

from WaveGrabber import GrabWaveFile
from WaveData import GraphWave
from WaveData import WaveData

import Log
import threading

waveData = WaveData()

targetCanvas = None
MainImageLoc = (2, 0)
root = None

def GrabWaveCommand():
    Log.LogEvent("Grab Wave Command Invoked", Log.Debug)

    GrabWaveFile(waveData)
    GraphWaveCommand()

def GraphWaveCommand():
    Log.LogEvent("Graph Wave Command Invoked", Log.Debug)

    if (waveData.getData() == None):
        return

    targetCanvas = GraphWave(root, waveData.getData())
    targetCanvas.grid(row = MainImageLoc[0], column = MainImageLoc[1], columnspan=2)


if __name__ == "__main__":
    Log.InitLog(level=Log.Info)
    Log.LogEvent("Starting UI")

    root = tk.Tk()
    root.title("SPIDAM")
    root.geometry("500x400+400+400")
    root.resizable(True, True)

    root.grid_columnconfigure(0, weight=1)

    TitleLbl = tk.Label(root, text="SPIDAM Program")
    SubTitleLbl = tk.Label(root, text="Please select a file to begin")
    # GrabWaveFile sets the data attribute inside waveData obj
    selfile_button = tk.Button(root, text="Select", command=GrabWaveCommand)

    TitleLbl.grid(column=0, row=0, sticky='W')
    SubTitleLbl.grid(column=0, row=1,sticky='W')
    selfile_button.grid(column=1, row=1, sticky='E', padx=10)

    Log.LogEvent("UI Loaded, begining Main Loop.")
    root.mainloop()
    Log.LogEvent("Shutdown completed sucessfully.")