import WaveData

import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
import soundfile as sf

import conf.Log as Log
import conf.Configuration as Conf


def ComputeMidFrequency(file_path):
    # Load the WAV file
    sample_rate, data = wavfile.read(file_path)

    # Calculate FFT
    frequencies = np.fft.fftfreq(len(data), 1 / sample_rate)

    # Find the midpoint index
    midpoint_index = len(frequencies) // 2
    mid_frequency = frequencies[midpoint_index]
    return mid_frequency


def ComputeLowestFrequency(file_path):
    sample_rate, data = wavfile.read(file_path)

    # Calculate FFT
    fft_result = np.fft.fft(data)
    frequencies = np.fft.fftfreq(len(data), 1 / sample_rate)
    magnitude_spectrum = np.abs(fft_result)

    # Find the index of the maximum amplitude
    min_index = np.argmin(magnitude_spectrum)
    lowest_frequency = frequencies[min_index]
    return lowest_frequency


def ComputeHighestResonance(file_path):
    sample_rate, data = wavfile.read(file_path)

    # Calculate FFT
    fft_result = np.fft.fft(data)
    frequencies = np.fft.fftfreq(len(data), 1 / sample_rate)
    magnitude_spectrum = np.abs(fft_result)

    # Find the index of the maximum amplitude
    max_index = np.argmax(magnitude_spectrum)
    highest_frequency = frequencies[max_index]
    return highest_frequency


def ComputeHighestResonance(WaveData: WaveData):
    # Load audio file
    AudioFile = WaveData.getData()
    if (AudioFile == None):
        return None

    signal, sample_rate = AudioFile.raw_data, AudioFile.frame_rate
    audio_data = np.frombuffer(signal, dtype=np.int16)

    # Calculate the envelope of the signal (absolute value)
    envelope = np.abs(audio_data, dtype=np.int16)
    return np.max(envelope)


def DeterminePreformance():
    pass


def calculate_rt60(WaveData: WaveData.WaveData):
    def find_target_frequency(freqs):
        for x in freqs:
            if x > 1000:
                break
        return x

    def frequency_check():
        global target_frequency
        target_frequency = find_target_frequency(freqs)
        index_of_frequency = np.where(freqs == target_frequency)[0][0]
        data_for_frequency = spectrum[index_of_frequency]
        data_in_db_fun = 10 * np.log10(data_for_frequency)
        return data_in_db_fun

    sample_rate, data = wavfile.read(WaveData.getPath())
    spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap("autumn_r"))

    data_in_db = frequency_check()
    plt.figure()

    plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color="#004bc6")
    plt.xlabel("Time (s)")
    plt.ylabel("Power (dB)")

    index_of_max = np.argmax(data_in_db)
    value_of_max = data_in_db[index_of_max]
    plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')

    sliced_array = data_in_db[index_of_max:]
    value_of_max_less_5 = value_of_max - 5

    def find_nearest_value(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
    index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
    plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')

    value_of_max_less_25 = value_of_max - 25
    value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
    index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
    plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')

    rt20 = (t[index_of_max_less_5] - t[index_of_max_less_25])[0]
    rt60 = 3 * rt20
    plt.grid()

    plt.savefig(Conf.Configuration.RetriveConfiguration("rt60plot"))
    return [int(target_frequency), round(abs(rt60), 2)]


if __name__ == "__main__":
    Conf.Configuration.Init("setup.cfg")
    Log.InitLog()

    waveData = WaveData.WaveData()
    WaveData.GrabWaveFile(waveData, None)

    if (waveData.getData() != None):
        calculate_rt60(waveData)
