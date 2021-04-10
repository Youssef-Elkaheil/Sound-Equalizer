from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import os
def getFile(self):
        """ This function will get the address of the csv file location
			also calls plotData function 
		"""

        self.filePath = QFileDialog.getOpenFileName(filter="csv (*.csv)")[0]
        print("File :", self.filePath)
        self.reader = pd.read_csv(self.filePath, header=1)
        self.fileName = os.path.basename(self.filePath)
        self.plotData(self.fileName)


def plotData(self, fileName):

        self.reader = self.reader[1:].astype(float)
        file = self.reader.iloc[:, 0]
        data = []
        styles = {"color": "#fff", "font-size": "12px"}
        for row in file:
            data.append(row)

        self.data1 = data
        self.After.clear()
        self.After.setTitle(fileName, color='w', size='12pt')
        self.After.setLabel("left", "volt", **styles, units="mV")
        self.After.setLabel("bottom", "Time(msec)", **styles,)
        self.After.plot(data)


