import tkinter as tk
import Log


def startGUI(root, waveData):
    StatsGrid = tk.Frame(root)
    StatsGrid.grid(row=2, column=0, columnspan=2)

    currentRow = 0

    tk.Label(StatsGrid, text="File Information", font='Arial 16 bold').grid(row=currentRow, column=0, columnspan=2)
    currentRow += 1

    tk.Label(StatsGrid, text="File Path: ").grid(row=currentRow, column=0)
    tk.Label(StatsGrid, text=waveData.getPath()).grid(row=currentRow, column=1, columnspan=2)
    currentRow += 1

    tk.Label(StatsGrid, text="Length: ").grid(row=currentRow, column=0)
    tk.Label(StatsGrid, text=f"{round(waveData.getData().duration_seconds, 2)} seconds").grid(row=currentRow, column=1)
    currentRow += 1

