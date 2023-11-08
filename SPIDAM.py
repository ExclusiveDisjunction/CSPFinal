import tkinter as tk
from tkinter import N, S, E, W, EW
from tkinter import messagebox

from WaveGrabber import GrabWaveFile

if __name__ == "__main__":
    root = tk.Tk()
    root.title("SPIDAM")
    root.geometry("500x400+400+400")
    root.resizable(True, True)

    root.grid_columnconfigure(0, weight=1)

    TitleLbl = tk.Label(root, text="SPIDAM Program")
    SubTitleLbl = tk.Label(root, text="Please select a file to begin")
    selfile_button = tk.Button(root, text="Select", command=GrabWaveFile)

    TitleLbl.grid(column=0, row=0, sticky='W')
    SubTitleLbl.grid(column=0, row=1,sticky='W')
    selfile_button.grid(column=1, row=1, sticky='E', padx=10)

    root.mainloop()