import tkinter as tk
from tkinter import N, S, E, W, EW
from tkinter import messagebox

from WaveGrabber import GrabWaveFile
from WaveData import GraphWave
from WaveData import WaveData

from DataAna import DetermineRT60

import Log

waveData = WaveData()

root = None

def GrabWaveCommand():
    Log.LogEvent("Grab Wave Command Invoked", Log.Debug)

    GrabWaveFile(waveData)

    StatsGrid = tk.Frame(root)
    StatsGrid.grid(row = 2, column = 0, columnspan = 2)

    currentRow = 0

    tk.Label(StatsGrid, text="File Information", font=('Arial 16 bold')).grid(row = currentRow, column = 0, columnspan = 2)
    currentRow += 1

    tk.Label(StatsGrid, text="File Path: ").grid(row = currentRow, column = 0)
    tk.Label(StatsGrid, text=waveData.getPath()).grid(row = currentRow, column=1, columnspan = 2)
    currentRow += 1

    tk.Label(StatsGrid, text="Length: ").grid(row = currentRow, column = 0)
    tk.Label(StatsGrid, text=f"{round(waveData.getData().duration_seconds, 2)} seconds").grid(row = currentRow, column = 1)
    currentRow += 1

    tk.Label(StatsGrid, text="RT60: ").grid(row = currentRow, column = 0)
    tk.Label(StatsGrid, text=f"{format(DetermineRT60(waveData), '.0e')}").grid(row = currentRow, column = 1)
    currentRow += 1

    GraphWaveCommand()

def GraphWaveCommand():
    Log.LogEvent("Graph Wave Command Invoked", Log.Debug)

    if (waveData.getData() == None):
        return

    targetCanvas = GraphWave(root, waveData.getData())
    targetCanvas.grid(row = 4, column = 0, columnspan=2)


if __name__ == "__main__":
    Log.InitLog(level=Log.Info)
    Log.LogEvent("Starting UI")

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

    Log.LogEvent("UI Loaded, begining Main Loop.")
    root.mainloop()
    Log.LogEvent("Shutdown completed sucessfully.")