from PyQt5.QtWidgets import QFileDialog
import librosa
import os


def getFile(self):
        """ This function will get the address of the csv file location
			also calls a readData function 
		"""
        self.filePath = QFileDialog.getOpenFileName(filter="wav (*.wav)")[0]
        print("File :", self.filePath)
        self.fileName = os.path.basename(self.filePath)
        plotData(self,self.fileName)


def plotData(self, fileName):

    data, self.sampling_rate = librosa.load(
        fileName, sr=None, mono=True, offset=0.0, duration=None)
    self.After.clear()
    self.After.setTitle(fileName, color='w', size='12pt')
    self.After.setLabel("left", "Amplitude")
    self.After.setLabel("bottom", "Time")
    self.After.plot(data)
    print(data)

