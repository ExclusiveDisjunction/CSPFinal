from pydub import AudioSegment
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

import Log

class WaveData:
    def __init__(self):
        self.audioSegData = None

    def setData(self, audioSegment):
        self.audioSegData = audioSegment

    def getData(self):
        return self.audioSegData


def CleanWave(seg: AudioSegment) -> AudioSegment:
    Log.LogEvent("Began cleaning wave.")

    chann = seg.channels
    Log.LogEvent(f"Detected {chann} channel(s), acting accordiningly....", Log.Debug)

    if chann != 1:
        return seg.set_channels(1)
    else:
        return seg


def GraphWave(target: tk.Canvas | None, wave: AudioSegment) -> str:
    """
        Graphs the wave function, and if target is not None, it will output that graph onto the target.
    """
    Log.LogEvent("Began graphing wave.")

    ImgPath = "TotalWaveOutput.png"

    # Graph the wave function
    AudData = list(wave.raw_data)
    Log.LogEvent("Graphing wave data now.")

    # Step is FrameRate * Sample Width * 8, in Hz, so step is 1 over that number.

    step = 1 / float(wave.frame_rate * wave.sample_width * 8) # Seconds
    timeStart = 0 # Seconds
    timeEnd = wave.duration_seconds #Seonds

    for pair in (np.arange(timeStart, timeEnd, step), AudData):
        plt.scatter(pair[0], int(pair[1]))


    plt.plot(*AudData)
    plt.savefig(ImgPath)

    Log.LogEvent("Completed making data graph.")

    # Display that image
    if target != None:
        Log.LogEvent("Attempting to render graph on UI...", Log.Debug)

        img = ImageTk.PhotoImage(Image.open(ImgPath))
        target.background = img
        target.create_image(0, 0, anchor=tk.NW, image=img)
        
        Log.LogEvent("Graph rendered on UI.", Log.Debug)        

    return ImgPath


if __name__ == "__main__":
    from WaveGrabber import GrabWaveFile
    print(GraphWave(None, GrabWaveFile(None)))
