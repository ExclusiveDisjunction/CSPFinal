import tkinter as tk
from tkinter import N, S, E, W
from tkinter import messagebox

from WaveGrabber import GrabWaveFile

if __name__ == "__main__":
    root = tk.Tk()
    root.title("SPIDAM")
    root.geometry("500x400+400+400")
    root.resizable(True, True)

    root.grid_columnconfigure(0, weight=1)

    """

        LAYOUT

        Row 0, Header (Frame)
        Row 1, Commands

    """

    # Base Frames
    Header = tk.Frame(root)
    CommandPallet = tk.Frame(root)

    Header.grid(column=0, row=0, sticky=E+W)
    CommandPallet.grid(column = 0, row = 1, sticky=E+W)

    # Header Items
    TitleLbl = tk.Label(Header, text="SPIDAM Program")
    SubTitleLbl = tk.Label(Header, text="Please select a file to begin")

    TitleLbl.grid(column=0, row=0)
    SubTitleLbl.grid(column=0, row=1)

    root.mainloop()