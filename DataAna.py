import WaveData
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import Log

def ComputeFrequencyRange(audio_signal: np.array, sampling_rate: float) -> (np.array, np.array):
    """
        Using Fast Forier Transform, convert the audio signal into a fast forier array and the frequency range. 
        Returns both.
    """
    FastForierRes = np.fft.fft(audio_signal)
    return (FastForierRes, np.fft.fftfreq(len(FastForierRes), d=1/sampling_rate))

def PlotFrequencyRange(audio_signal: np.array, sampling_rate: float, outPath: str) -> None:
    """
        Plots the frequency range of the audio signal.
    """
    Log.LogEvent("Plotting Frequency Range")
    totalResult = ComputeFrequencyRange(audio_signal, sampling_rate)
    fft_result, fft_freq = totalResult[0], totalResult[1]

    plt.plot(fft_freq, np.abs(fft_result))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Spectrum')
    
    Log.LogEvent(f"Plot Determined, Outputting to path \"{outPath}\"")
    plt.savefig(outPath)
    Log.LogEvent(f"Graph outputted.")


def ComputeHighestResonance(audio_signal: np.array, sampling_rate: float) -> float:
    """
        Computes the Highest Resonance of a plot by using the audio signal as an array, and using the sample rate.
        Uses the Fast Forier Transform to compute the frequency plot and then determine the value of the highest resonance.
    """
    # Compute the FFT of the audio signal
    FastForierRes = np.fft.fft(audio_signal)
    Frequency = ComputeFrequencyRange(FastForierRes, sampling_rate)
    return ComputeHighestResonance(FastForierRes, Frequency)


def ComputeHighestResonance(FastForierRes: np.array, Frequency: np.array) -> float:
    """
        Determine the Highest Resonance using the pre-calculated fast forier transform, and its frequency plot.
    """
    # Find the index of the highest peak in the spectrum (excluding DC component)
    peak_index = np.argmax(np.abs(FastForierRes[1:])) + 1

    # Convert index to frequency
    highest_resonance = np.abs(Frequency[peak_index])

    return float(highest_resonance)


def DetermineRT60(WaveData: WaveData) -> float:
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

import WaveGrabber
import WaveData

if __name__ == "__main__":
    data = WaveData.WaveData()
    WaveGrabber.GrabWaveFile(data, None)
    AudioFile = data.getData()
    if (AudioFile != None):
        AudioFile = AudioFile
        
        signal, sample_rate = AudioFile.raw_data, AudioFile.frame_rate
        audio_data = np.frombuffer(signal, dtype=np.int16)

        PlotFrequencyRange(audio_data, sample_rate, "FrequencyPlot.png")