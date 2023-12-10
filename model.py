import tkinter as tk
from WaveData import GraphWave
from WaveData import WaveData
from WaveGrabber import GrabWaveFile
import view
from conf import Log

waveData = WaveData()
root = None

def startGUICommand():
    view.startGUI(root, waveData)


def GraphWaveCommand():
    Log.LogEvent("Graph Wave Command Invoked", Log.Debug)

    if (waveData.getData() == None):
        return

    targetCanvas = GraphWave(root, waveData.getData())
    targetCanvas.grid(row=4, column=0, columnspan=2)


def buildGUI():
    GrabWaveFile(waveData)

    Log.InitLog(level=Log.Info)
    Log.LogEvent("Starting UI")
    
    global root
    root = tk.Tk()
    root.title("SPIDAM")
    root.geometry("500x400+400+400")
    root.resizable(True, True)

    root.grid_columnconfigure(0, weight=1)

    TitleLbl = tk.Label(root, text="SPIDAM Program", font=('Arial 20 bold'))
    SubTitleLbl = tk.Label(root, text="Please select a file to begin")
    # GrabWaveFile sets the data attribute inside waveData obj
    selfile_button = tk.Button(root, text="Select", command=startGUICommand)

    startGUICommand()
    GraphWaveCommand()

    TitleLbl.grid(column=0, row=0, columnspan=2)
    SubTitleLbl.grid(column=0, row=1, sticky='W')
    selfile_button.grid(column=1, row=1, sticky='E', padx=10)

    Log.LogEvent("UI Loaded, begining Main Loop.")
    root.mainloop()
    Log.LogEvent("Shutdown completed sucessfully.")
