import model
import view

import conf.Configuration as Conf
import conf.Log as Log

import DataAna
import WaveGrabber
import WaveTool

class Controller:
    def __init__(self, model: model.Model, view : view.View):
        self.model = model
        self.view = view

        Log.LogEvent("Controller initiated.")

    def LoadAndCalculateFile(self):
        if self.model and self.view:
            # First we need to grab the wave file.
            WaveGrabber.GrabWaveFile(self.model.Data)

            if self.model.Data.Data is None:
                return
        
            # Now that the file is loaded, render the main graph.
            TotalOutputImg = WaveTool.GraphWave(self.model.Data.Data)
            self.view.LoadImageFromPath(TotalOutputImg, self.view.TotalOutputLabel)

            # Next fill the RT60 values and graphs.
            RT60Diff = 0.0
            RT60Low = 0.0
            RT60Mid = 0.0
            RT60High = 0.0

            FreqGraphTot = Conf.Configuration.RetriveConfiguration("frequencyGraphPath")
            FreqGraphLow = Conf.Configuration.RetriveConfiguration("lowFrequencyGraphPath")
            FreqGraphMid = Conf.Configuration.RetriveConfiguration("midFrequencyGraphPath")
            FreqGraphHigh = Conf.Configuration.RetriveConfiguration("highFrequencyGraphPath")

            self.model.ImageFreqData = [("All", RT60Diff, FreqGraphTot), ("Low", RT60Low, FreqGraphLow), ("Mid", RT60Mid, FreqGraphMid), ("High", RT60High, FreqGraphHigh)]
            self.model.CurrentImage = 0
            self.UpdateImageOnCurrentVal()

            # Update Stats
            self.view.FilePathVar.set(self.model.Data.Path)
            self.view.FileLenVar.set(f"{round(self.model.Data.Data.duration_seconds, 2)} seconds")

    def CycleNextFreqImage(self):
        if self.model and self.view:
            # First increment the index
            currentIndex = self.model.CurrentImage
            currentIndex = (currentIndex + 1) % len(self.model.ImageFreqData)

            # Update data and then select data.
            self.model.CurrentImage = currentIndex
            self.UpdateImageOnCurrentVal()            
    def CycleNextFreqImage(self):
        if self.model and self.view:
            # First increment the index
            currentIndex = self.model.CurrentImage - 1
            currentIndex = len(self.model.ImageFreqData) - 1 if currentIndex < 0 else currentIndex

            # Update data and then select data.
            self.model.CurrentImage = currentIndex
            self.UpdateImageOnCurrentVal()  
    def UpdateImageOnCurrentVal(self):  
        if self.model and self.view:
            currentData = self.model.ImageFreqData[self.model.CurrentImage]

            # Update View.
            self.view.FrequencyRangeVar.set(currentData[0] + (" Range" if currentData[0] != "All" else " Ranges"))
            self.view.LoadImageFromPath(self.view.CurrentImage, currentData[1])
            self.view.RT60Var.set(f"{round(currentData[2], 2)} seconds")