import tkinter as tk
from WaveData import WaveData

import conf.Log as Log

class Model:
    def __init__(self, Data: WaveData):
        self.Data = Data
        self.ImageFreqData = { ("All", "", 0.00), ("Low", "", 0.00), ("Mid", "", 0.00), ("High", "", 0,00)}
        self.CurrentImage = 0
        Log.LogEvent("Model initiated")

    @property
    def Data(self):
        return self.__data
    
    @Data.setter
    def Data(self, value: WaveData):
        self.__data = value
        Log.LogEvent("Data in Model was changed.", Log.Debug)
