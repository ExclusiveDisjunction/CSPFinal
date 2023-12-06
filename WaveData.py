from pydub import AudioSegment
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

import Log

class WaveData:
    def __init__(self):
        self.audioSegData = None
        self.Path = None

    def setData(self, audioSegment, path):
        self.audioSegData = audioSegment
        self.Path = path

    def getData(self):
        return self.audioSegData
    def getPath(self):
        return self.Path

def CleanWave(seg: AudioSegment) -> AudioSegment:
    Log.LogEvent("Began cleaning wave.")

    chann = seg.channels
    Log.LogEvent(f"Detected {chann} channel(s), acting accordiningly....", Log.Debug)

    if chann != 1:
        return seg.set_channels(1)
    else:
        return seg


def GraphWave(root: tk.Tk | None, wave: AudioSegment) -> tk.Label:
    """
        Graphs the wave function, and if target is not None, it will output that graph onto the target.
    """
    Log.LogEvent("Began graphing wave.")
    print(root)

    ImgPath = "TotalWaveOutput.png"

    # Graph the wave function
    Log.LogEvent("Graphing wave data now.")

    # Step is FrameRate * Sample Width * 8, in Hz, so step is 1 over that number.

    framerate = wave.frame_rate
    frames = wave.raw_data
    signal = np.frombuffer(frames, dtype=np.int16)

    time = np.linspace(0, len(signal) / framerate, num=len(signal))

    plt.figure(figsize=(10,4))
    plt.plot(time, signal, color='b')
    plt.title('Total Audio Waveform')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.savefig(ImgPath)

    Log.LogEvent("Completed making data graph.")

    # Display that image
    if root != None:
        Log.LogEvent("Attempting to render graph on UI...")

        image = Image.open(ImgPath)
        tk_image = ImageTk.PhotoImage(image)

        label = tk.Label(root, image = tk_image)
        label.image = tk_image
        
        Log.LogEvent("Graph rendered on UI.") 
        return label    

    return None


if __name__ == "__main__":
    from WaveGrabber import GrabWaveFile
    print(GraphWave(None, GrabWaveFile(None)))
