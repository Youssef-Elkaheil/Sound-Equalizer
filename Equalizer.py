import math
import numpy as np
from scipy.fft import irfft
from scipy.fft import rfft, rfftfreq
from scipy.io.wavfile import write

def ShowEqualizer(self, MainWindow):
    if self.actionEqualizer.isChecked():
        if self.actionSpectrogram.isChecked():
            MainWindow.resize(1537, 953)
            self.tabWidget.resize(1501, 861)
        else:
            MainWindow.resize(1110, 953)
            self.tabWidget.resize(1070, 861)
        
        self.Graph_Before.resize(961, 271)
        self.frame.resize(961, 211)

    else:
        if self.actionSpectrogram.isChecked():
            MainWindow.resize(1537, 450)
            self.tabWidget.resize(1501, 350)
        else:
            MainWindow.resize(1110, 450)
            self.tabWidget.resize(1070, 350)
        
        self.Graph_Before.resize(0, 0)
        self.frame.resize(0, 0)


# def Band(self,index):
#     self.band =[]
#     #BW = int(len(self.xrfft) / (self.sampling_rate / 2))
#     BW = math.ceil(len(np.abs(self.data))/10)
#     for i in range(10):
#         self.band.append(self.yrfft[i*BW:(i+1)*BW])
#     return self.band[index]


def Gain(self):
    self.N = self.sampling_rate * self.data/10000
    normalized_tone = np.int16((self.data / self.data.max()) * 32767)
    self.yrfft = rfft(normalized_tone)
    self.xrfft = rfftfreq(self.N, 1 / self.sampling_rate)
    self.points_per_freq = int(len(self.xrfft) / (self.sampling_rate / 2))
    self.BW = int(self.points_per_freq*(self.sampling_rate / 20))
    self.yrfft[:] =0
                #slider *self.BW : (slider+1)*self.BW] *= 0
    self.yt = irfft(self.yrfft)
    self.Graph_After.clear()
    # self.Graph_After.setTitle('After', color='w', size='12pt')
    # self.Graph_After.setLabel("left", "Amplitude")
    # self.Graph_After.setLabel("bottom", "Time")
    # self.Graph_After.plot(self.yt)
    # write("Result.wav", self.sampling_rate, self.yt)

   





