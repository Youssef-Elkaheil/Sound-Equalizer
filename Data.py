from PyQt5.QtWidgets import QFileDialog
import librosa
import os
import Spectrogram
spectrogram = Spectrogram.Spectrogram
def getFile(self):
        """ This function will get the address of the Wav file location
			also calls a plotData function 
		"""
        
        
        self.filePath = QFileDialog.getOpenFileName(filter="wav (*.wav)")[0]
        print("File :", self.filePath)
        self.fileName = os.path.basename(self.filePath)
        plotData(self,self.fileName)


def plotData(self, fileName):

    self.data, self.sampling_rate = librosa.load(
        fileName, sr=None, mono=True, offset=0.0, duration=None)

    self.Graph_After.clear()
    self.Graph_After.setTitle('After', color='w', size='12pt')
    self.Graph_After.setLabel("left", "Amplitude")
    self.Graph_After.setLabel("bottom", "Time")
    self.Graph_After.plot(self.data)

    self.Graph_Before.clear()
    self.Graph_Before.setTitle('Before', color='w', size='12pt')
    self.Graph_Before.setLabel("left", "Amplitude")
    self.Graph_Before.setLabel("bottom", "Time")
    self.Graph_Before.plot(self.data)

    spectrogram(self,self.data)
    print(self.data)
    print(self.sampling_rate)
    print(len(self.data))


    
