from pydub import AudioSegment
import numpy
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk

from WaveGrabber import GrabWaveFile

def CleanWave(seg : AudioSegment) -> AudioSegment:
    chann = seg.channels

    if (chann != 1):
        return seg.set_channels(1)
    else:
        return seg

def GraphWave(target: tk.Canvas | None, wave: AudioSegment) -> str:
    """
        Graphs the wave function, and if target is not None, it will output that graph onto the target.
    """

    ImgPath = "TotalWaveOutput.png"

    # Graph the wave function
    AudData = wave.raw_data
    plt.plot(data=AudData)
    plt.savefig(ImgPath)

    # Display that image
    if (target != None):
        img = ImageTk.PhotoImage(Image.open(ImgPath), Image.ANTIALIAS)
        target.background = img;
        target.create_image(0,0,anchor=tk.NW, image=img)

    return ImgPath

if __name__ == "__main__":
    print(GraphWave(None, GrabWaveFile(None)))