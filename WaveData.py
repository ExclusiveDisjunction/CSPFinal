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
    Log.LogEvent(f"For plotting, the step in seconds is {step}, the start and end is ({timeStart},{timeEnd}). Array is {len(AudData)} long.")

    i = 0
    t = timeStart
    for point in AudData:
        plt.plot(t, point)
        Log.LogEvent(f"Plotted point ({t},{point}) at index {i}", Log.Debug)
        i += 1
        t += step

    plt.savefig("TotalWaveOutput.png")

    Log.LogEvent("Completed making data graph.")

    # Display that image
    if target != None:
        Log.LogEvent("Attempting to render graph on UI...")

        img = ImageTk.PhotoImage(Image.open(ImgPath))
        target.background = img
        target.create_image(0, 0, anchor=tk.NW, image=img)
        
        Log.LogEvent("Graph rendered on UI.")        

    return ImgPath


if __name__ == "__main__":
    from WaveGrabber import GrabWaveFile
    print(GraphWave(None, GrabWaveFile(None)))
