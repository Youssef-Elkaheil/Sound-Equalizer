import numpy as np
from scipy import signal
def ShowSpectrogram(self,MainWindow):
    if self.actionSpectrogram.isChecked():
        if self.actionEqualizer.isChecked():
            MainWindow.resize(1537, 953)
            self.tabWidget.resize(1501, 861)
        else:
            MainWindow.resize(1537, 450)
            self.tabWidget.resize(1501, 350)

        self.Spectrogram_Before.resize(431, 300)
        self.Spectrogram_After.resize(431, 300)
        
    else:
        if self.actionEqualizer.isChecked():
            MainWindow.resize(1110, 953)
            self.tabWidget.resize(1070, 861)
        else:
            MainWindow.resize(1110, 450)
            self.tabWidget.resize(1070, 350)

        self.Spectrogram_Before.resize(0, 0)
        self.Spectrogram_After.resize(0, 0)
        


def Spectrogram(self, data):
    sampling_freq = 10e3
    freq, time, spectrogramPlot = signal.spectrogram(data, sampling_freq)
    self.img1.setImage(spectrogramPlot)
    self.img1.scale(time[-1]/np.size(spectrogramPlot, axis=1),
                    freq[-1]/np.size(spectrogramPlot, axis=0))
    self.Spectroplot1.setLimits(xMin=0, xMax=time[-1], yMin=0, yMax=freq[-1])
    self.Spectroplot1.setLabel('bottom', "Time")
    self.Spectroplot1.setLabel('left', "Frequency")
