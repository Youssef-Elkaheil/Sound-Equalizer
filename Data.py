from PyQt5.QtWidgets import QFileDialog
from scipy import signal
import numpy as np
import librosa
global fileName, samples, sampling_rate, T

def getFile(self):

    fileName, _ = QFileDialog.getOpenFileName(
        None, "QFileDialog.getOpenFileName()", "", "WAV Files (*.wav)")

    samples, sampling_rate = librosa.load(
        fileName, sr=None, mono=True, offset=0.0, duration=None)
    l = len(samples)
    T = int(l / sampling_rate)
    print(l)
    print(T)
    self.Graph_After(samples, sampling_rate, l,pen ='r',font=5)
    # self.plot_spectro(samples[:T*sampling_rate], sampling_rate)
    



def plotData(self):
    self.Graph_After.clear()

    self.Graph_After.setTitle('After', color='w', size='12pt')
    self.Graph_After.setLabel("left", "Amplitude")
    self.Graph_After.setLabel("bottom", "Time")
    # self.Graph_After.setXRange(np.min(self.time), np.max(self.time), padding=0.01)
    # self.Graph_After.setYRange(np.min(self.data),np.max(self.data), padding=5)
    self.Graph_After.plot(samples)
    #print( samples)
    self.Graph_Before.clear()
    self.Graph_Before.setTitle('Before', color='w', size='12pt')
    self.Graph_Before.setLabel("left", "Amplitude")
    self.Graph_Before.setLabel("bottom", "Time")
    # self.Graph_Before.setXRange(np.min(self.time), np.max(self.time), padding=0.01)
    # self.Graph_Before.setYRange(np.min(samples), np.max(samples), padding=5)
    self.Graph_Before.plot(samples)

    Spectrogram(samples)
    print(samples)
    print(sampling_rate)
    print(len(samples))



def ShowSpectrogram(self, MainWindow):
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
    self.sampling_freq = 10e2*3

    freq, time, spectrogramPlot = signal.spectrogram(
        data, self.sampling_freq)
    self.hist_Before.setLevels(np.min(spectrogramPlot),
                               np.max(spectrogramPlot))
    self.img_Before.setImage(spectrogramPlot)
    self.img_Before.scale(time[-1]/np.size(spectrogramPlot, axis=1),
                          np.max(freq)/np.size(spectrogramPlot, axis=0))
    self.Spectroplot_Before.setLimits(
        xMin=0, xMax=time[-1], yMin=0, yMax=freq[-1])
    self.Spectroplot_Before.setLabel('bottom', "Time")
    self.Spectroplot_Before.setLabel('left', "Frequency")

    self.hist_After.setLevels(np.min(spectrogramPlot),
                              np.max(spectrogramPlot))
    self.img_After.setImage(spectrogramPlot)
    self.img_After.scale(time[-1]/np.size(spectrogramPlot, axis=1),
                         np.max(freq)/np.size(spectrogramPlot, axis=0))
    self.Spectroplot_After.setLimits(
        xMin=0, xMax=time[-1], yMin=0, yMax=freq[-1])
    self.Spectroplot_After.setLabel('bottom', "Time")
    self.Spectroplot_After.setLabel('left', "Frequency")
