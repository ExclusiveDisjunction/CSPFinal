import tkinter as tk
from tkinter import N, S, E, W, EW
from tkinter import messagebox

from WaveGrabber import GrabWaveFile
from WaveData import GraphWave
from WaveData import WaveData

waveData = WaveData()

targetCanvas = None

def GrabWaveCommand():
    GrabWaveFile(waveData)
    GraphWaveCommand()

def GraphWaveCommand():
    if (waveData.getData() == None or targetCanvas == None):
        return
    
    GraphWave(targetCanvas, waveData.getData())


if __name__ == "__main__":
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

    targetCanvas = tk.Canvas(root)

    root.mainloop()