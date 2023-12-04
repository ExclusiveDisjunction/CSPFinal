import WaveData
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import Log

def ComputeHighestResonance():
    pass

def DetermineRT60(WaveData: WaveData):
    # Load audio file
    AudioFile = WaveData.getData()
    if (AudioFile == None):
        return None
    
    signal, sample_rate = AudioFile.raw_data, AudioFile.frame_rate
    audio_data = np.frombuffer(signal, dtype=np.int16)
    
    # Calculate the envelope of the signal (absolute value)
    envelope = np.abs(audio_data, dtype=np.int16)
    
    # Normalize the envelope
    NewEnvolope = envelope / np.max(envelope)
    
    # Find peaks in the envelope
    peaks, _ = find_peaks(NewEnvolope, height=0.7)  # Adjust height as needed
    
    # Calculate the time difference between peaks
    time_diff = np.diff(peaks) / sample_rate
    
    # Calculate the RT60 using the time differences
    rt60 = -time_diff.mean() / np.log(0.001)  # Decay to -60 dB (0.001 amplitude)
    
    Log.LogEvent(f"rt60 is {format(rt60, '.3e')}")
    return rt60

def DeterminePreformance():
    pass