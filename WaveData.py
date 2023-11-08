from pydub import AudioSegment
import tkinter as tk
from PIL import Image, ImageTk

def CleanWave(seg : AudioSegment) -> AudioSegment:
    chann = seg.channels

    if (chann != 1):
        return seg.set_channels(1)
    else:
        return seg

def GraphWave(target: tk.Canvas, wave: AudioSegment):
    # Graph the wave function
    ImgPath = "TotalWaveOutput.png"

    # Display that image
    img = ImageTk.PhotoImage(Image.open(ImgPath), Image.ANTIALIAS)
    target.background = img;
    target.create_image(0,0,anchor=tk.NW, image=img)