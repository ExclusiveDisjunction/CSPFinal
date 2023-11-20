from pydub import AudioSegment
import numpy
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk


class WaveData:
    def __init__(self):
        self.audioSegData = None

    def setData(self, audioSegment):
        self.audioSegData = audioSegment

    def getData(self):
        return self.audioSegData


def CleanWave(seg: AudioSegment) -> AudioSegment:
    chann = seg.channels

    if chann != 1:
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
    if target != None:
        print("Attempting to display graph...")
        img = ImageTk.PhotoImage(Image.open(ImgPath))
        target.background = img
        target.create_image(0, 0, anchor=tk.NW, image=img)
        print("Image Graphed.")

    return ImgPath


if __name__ == "__main__":
    from WaveGrabber import GrabWaveFile
    print(GraphWave(None, GrabWaveFile(None)))
