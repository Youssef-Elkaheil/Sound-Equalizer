import math
import numpy as np
from scipy.fft import irfft
from scipy.fft import rfft, rfftfreq
from scipy.io.wavfile import write
global fileName, samples, sampling_rate, T

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



def Gain(self):
    pass
# def bands(self):
#     self.N = self.sampling_rate * len(self.data)

#     self.yrf = rfft(self.data)
#     #print(self.samplingfrequency, len(self.duration))
#     self.xrf = rfftfreq(int(self.N), (1 / self.samplingfrequency))

#     self.BW = int(len(self.xrf)/10)

#     self.yrfcopy = []
#     for i in range(10):
#         self.yrfcopy.append(self.yrf[i * self.BW: (i+1)*self.BW])
#     self.yrfcopy = self.yrf.copy()


# def Gain(self, slider, Gain=1):

    
#     self.yrfcopy[slider] = self.yrf[slider]*Gain
#     self.ynew = []

#     for i in self.yrf:
#         print (i)
#         for g in i:
            
#             self.ynew.append(g)
    
#     print (self.yrf)
#     #print(self.yirfft)
#     # print(self.yrf)
#     # print(self.y_after)
#     self.yt = irfft(np.array(self.yrf))
#     self.Graph_After.clear()
#     self.Graph_After.setTitle('After', color='w', size='12pt')
#     self.Graph_After.setLabel("left", "Amplitude")
#     self.Graph_After.setLabel("bottom", "Time")
#     self.Graph_After.plot(np.real(self.yt))
    
#     #write("Result.wav", self.samplingfrequency, self.yt)
