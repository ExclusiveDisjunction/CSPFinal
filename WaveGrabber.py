from pathlib import Path
from pydub import AudioSegment
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# This file will prompt the user for a file, and convert it to a .wav and then return it.

def GrabWaveFile() -> AudioSegment:
    FilePath = PromptFile()
    AudFile = GrabAudioSegment(FilePath)
    if (AudFile == None):
        return None

    if (AudFile == None):
        messagebox.showinfo("The file requested could not be opened.")
        return None

    if (FilePath.suffix != ".wav"):
        MsgResult = messagebox.askquestion("File not .wav", "The provided file is not .wav, and it will be converted. Is this ok? A copy of the file with an extension of .wav will be created.")
        if (MsgResult != "Yes"):
            return None

        NewPath = os.path.basename(str(FilePath)) + FilePath.stem + ".wav"
        AudFile.export(str(NewPath), format="wav")

        AudFile = GrabAudioSegment(str(NewPath))
        FilePath = NewPath

    return AudFile
    

def GrabAudioSegment(FilePath: Path) -> AudioSegment:
    if (FilePath == None):
        return None
    Suffix = FilePath.suffix
    Suffix = Suffix.removeprefix(".")

    # This code is audioist. It wont open anything other than .wav :(

    try:
        AudioSeg = AudioSegment.from_file(str(FilePath), format=Suffix)
    except FileNotFoundError as e:
        messagebox.showerror("Error:", f"There was the following error: \n\"{str(e)}\"")
        return None

    return AudioSeg

# We will have to first import a file.
def PromptFile() -> Path:
    FilePathRaw = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.wma;*.aac")])

    if (FilePathRaw == ""):
        return None
    
    return Path(FilePathRaw)


if __name__ == "__main__":
    GrabWaveFile()