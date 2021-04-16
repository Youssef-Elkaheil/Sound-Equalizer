# def BrowseSignal(self):
#         global fileName , sampling_rate, audio2
#         fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
#             None, "QFileDialog.getOpenFileName()", "", "WAV Files (*.wav)") 
#         audio2, sampling_rate = librosa.load(fileName, sr=None, duration=20.0)
#         l = len(audio2)
#         self.changeslidervalue()
#         self.plotAudio(audio2, l)
#         self.graphWidgets[0].plotItem.getViewBox().setLimits(xMin=0, xMax=l)

#     def stop_audio(self):
#         sd.stop()    
    
#     def speedTimer(self):
#         for i in range(2):
#             self.graphWidgets[i].plotItem.getViewBox().scaleBy(x=0.1, y=1) #Increases the scale of X axis and Y axis
#         self.timer= QtCore.QTimer()
#         self.timer.setInterval(20) #delay interval for dynamic signal
#         self.timer.timeout.connect(self.DynamicSignal)
#         # self.timer.timeout.connect(self.DynamicSignal2)
#          #connect timer to our dynamic signal
#         self.timer.start()

#     def DynamicSignal(self):
#         for i in range(2):
#            self.graphWidgets[i].plotItem.getViewBox().translateBy(x=l/100, y=0)

#     def plotAudio(self,file,length):
#         self.graphWidgets[0].plot(file[0:length],pen="b")

#     def play_audio(self):
#         sd.play(adjusted_file, sampling_rate)
    
#     def addNewWindow(self):
#         window3=MainApp()
#         window3.show()
#         self.newWindows.append(window3)
        
#     def zoomIn(self):
#         for i in range(2):
#            self.graphWidgets[i].plotItem.getViewBox().scaleBy(x=0.5, y=1) #Increases the scale of X axis and Y axis

#     def zoomOut(self):
#         for i in range(2):
#            self.graphWidgets[i].plotItem.getViewBox().scaleBy(x=2, y=1) #Decreases scale of X axis and Y axis 

#     def ScrollLeft(self):
#         for i in range(2):
#            self.graphWidgets[i].plotItem.getViewBox().translateBy(x=-1000, y=0)

#     def ScrollRight(self):
#         for i in range(2):
#            self.graphWidgets[i].plotItem.getViewBox().translateBy(x=1000, y=0)

#     def loopslider(self):
#         global i
#         i = 0
#         while i < 10:
#             sliderArray[i].valueChanged.connect(self.changeslidervalue)
#             i += 1

#     def changeslidervalue(self):
#         global i
#         i = 0
#         gainArray = []
#         while i < 10:
#             gainArray.append(sliderArray[i].value())
#             i += 1
#         self.audioRun(*gainArray)
#         return gainArray

#     def audioRun(self,*gainArray):
#         Rs = self.processAudio(audio2, sampling_rate, *gainArray)

#     def processAudio(self, audio2, sampling_rate, gain1, gain2, gain3, gain4, gain5, gain6, gain7, gain8, gain9, gain10):
#         n=l
#         global yf
#         yf = rfft(audio2)
#         T=1/sampling_rate
#         xf = rfftfreq(n,T)
#         global bandwidth
#         bandwidth1=np.where(xf==((sampling_rate)/20))
#         bandwidth=bandwidth1[0][0]
#         print("type of bandwidth",type(bandwidth))
#         band1=yf[0:bandwidth]*gain1
#         band2=yf[bandwidth:2*bandwidth]*gain2
#         band3=yf[2*bandwidth:3*bandwidth]*gain3
#         band4=yf[3*bandwidth:4*bandwidth]*gain4
#         band5=yf[4*bandwidth:5*bandwidth]*gain5
#         band6=yf[5*bandwidth:6*bandwidth]*gain6
#         band7=yf[6*bandwidth:7*bandwidth]*gain7
#         band8=yf[7*bandwidth:8*bandwidth]*gain8
#         band9=yf[8*bandwidth:9*bandwidth]*gain9
#         band10=yf[9*bandwidth:10*bandwidth]*gain10
#         global new_yfft
#         new_yfft=np.concatenate([band1,band2,band3,band4,band5,band6,band7,band8,band9,band10])
#         new_yfft[len(new_yfft): len(yf)] = 0
#         self.plotting(new_yfft)
#         self.colorPallete()
#         self.play_audio()
#         # ============================================================================

#     def plotting(self,new_yfft):
#         global adjusted_file
#         adjusted_file = irfft(new_yfft)
#         self.graphWidgets[1].plotItem.clear()
#         self.graphWidgets[1].plot(adjusted_file,pen = "r")
#         self.graphWidgets[1].plotItem.getViewBox().setLimits(xMin=0,xMax=l)
#         # pass
    
#     def colorPallete(self):
#         if self.comboBox.currentText()=='Palette 1':           
#             self.spectro('viridis')
#         elif self.comboBox.currentText()=='Palette 2':
#             self.spectro('plasma')
#         elif self.comboBox.currentText()=='Palette 3':
#             self.spectro('cool')
#         elif self.comboBox.currentText()=='Palette 4':
#             self.spectro('rainbow')
#         else:
#             self.spectro('GnBu')
           
#     def showSpectro(self):
#         if self.checkBox.isChecked()==True:
#             self.verticalWidget.show()
#         else:
#             self.verticalWidget.hide()

#     def spectro(self,colorMap):
#         fig = plt.figure()
#         plt.subplot(111)
#         self.spectrogram= plt.specgram(adjusted_file, Fs=sampling_rate, cmap=colorMap)
#         plt.colorbar()
#         fig.savefig('plot.png')
#         self.upload()
            
#     def upload(self):
#         self.spectroWidget.setPixmap(QtGui.QPixmap("plot.png"))
#         self.spectroWidget.setScaledContents(True)

#     def generatePDF(self, filename):
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font('Arial', 'B', 15)
#         pdf.set_xy(0,0)
#         for i in range(2):
#             pdf.cell(0, 10,ln=1,align='C')
#             exporter = pg.exporters.ImageExporter(self.graphWidgets[i].plotItem)               
#             exporter.parameters()['width'] = 250  
#             exporter.parameters()['height'] = 250         
#             exporter.export('fileName'+str(i+1)+'.png')
#             pdf.image(('fileName'+str(i+1)+'.png'),x=None,y=None, w=180,h=70)

#         pdf.cell(0, 10,ln=1,align='C')
#         pdf.image('plot.png',x=None,y=None, w=200,h=100)

#         pdf.output(filename)

#     def printPDF(self):
#         # allows the user to save the file and name it as they like
#         filename, _ = QtWidgets.QFileDialog.getSaveFileName(
#             self, "Export PDF", None, "PDF files (.pdf);;All Files()"
#         )
#         if filename:
#             if QtCore.QFileInfo(filename).suffix() == "":
#                 filename += ".pdf"
#             self.generatePDF(filename)

#     def generate_WavFile(self, filename):
#         maximum = np.max(np.abs(adjusted_file))
#         print(type(maximum))
#         print('adjusted_file',type(adjusted_file))
#         data = (adjusted_file / maximum).astype(np.float32)
#         name=filename
#         # name=name.format(self.flag)
#         save = wavfile.write(name, int(sampling_rate), data)
#         plt.subplot(211)
#         plot(adjusted_file)

#     def saveFile(self):
#         # allows the user to save the file and name it as they like
#         filename, _ = QtWidgets.QFileDialog.getSaveFileName(
#             self, "Export WAV", None, "WAV files (.wav);;All Files()"
#         )
#         if filename:
#             if QtCore.QFileInfo(filename).suffix() == "":
#                 filename += ".wav"
#             self.generate_WavFile(filename)

# class MainApp2(QMainWindow,MAIN_WINDOW2):
#     def __init__(self,parent=None):
#         super(MainApp2,self).__init__(parent)
#         QMainWindow.__init__(self)
#         self.setupUi(self)
        
#         self.pushButton.clicked.connect(self.fftt)
        
#     def fftt(self):
        
#         n=l
#         T=1/sampling_rate  
#         global yf
#         yf = rfft(audio2)
#         xf = rfftfreq(n,T)
        
#         self.fourWidget.plot(xf,np.abs(yf),pen = "b")
#         print(len(new_yfft))
#         print("len of yf",len(yf))
#         print("len of xf",len(xf))
#         self.fourWidget2.plot(xf[1:],np.abs(new_yfft)[ : len(xf)], pen='r')
# # from PyQt5.QtWidgets import QFileDialog
# # from scipy import signal
# # import pandas as pd
# # import numpy as np
# # import librosa
# # import os
# # global fileName, samples, sampling_rate, T


# # def getFile(self):

# #         self.filePath = QFileDialog.getOpenFileName(filter="wav (*.wav)")[0]
# #         print("File :", self.filePath)
# #         self.fileName = os.path.basename(self.filePath)
# #         self.data, self.sampling_rate = librosa.load(
# #             self.filePath, sr=None, mono=True, offset=0.0, duration=None)
# #         self.Graph_After.clear()
# #         self.Graph_After.setTitle('After', color='w', size='12pt')
# #         self.Graph_After.setLabel("left", "Amplitude")
# #         self.Graph_After.setLabel("bottom", "Time")
# #         self.Graph_After.plot(self.data)
# #         print(self.data)

# #         self.Graph_Before.clear()
# #         self.Graph_Before.setTitle('Before', color='w', size='12pt')
# #         self.Graph_Before.setLabel("left", "Amplitude")
# #         self.Graph_Before.setLabel("bottom", "Time")

# #         self.Graph_Before.plot(self.data)

# #         Spectrogram(self,self.data)
# #         print(self.data)
# #         print(self.sampling_rate)
# #         print(len(self.data))
    

# # def ShowSpectrogram(self, MainWindow):
# #     if self.actionSpectrogram.isChecked():
# #         if self.actionEqualizer.isChecked():
# #             MainWindow.resize(1537, 953)
# #             self.tabWidget.resize(1501, 861)
# #         else:
# #             MainWindow.resize(1537, 450)
# #             self.tabWidget.resize(1501, 350)

# #         self.Spectrogram_Before.resize(431, 300)
# #         self.Spectrogram_After.resize(431, 300)

# #     else:
# #         if self.actionEqualizer.isChecked():
# #             MainWindow.resize(1110, 953)
# #             self.tabWidget.resize(1070, 861)
# #         else:
# #             MainWindow.resize(1110, 450)
# #             self.tabWidget.resize(1070, 350)

# #         self.Spectrogram_Before.resize(0, 0)
# #         self.Spectrogram_After.resize(0, 0)


# # def Spectrogram(self, data):
# #     self.sampling_freq = 10e2*3

# #     freq, time, spectrogramPlot = signal.spectrogram(
# #         data, self.sampling_freq)
# #     self.hist_Before.setLevels(np.min(spectrogramPlot),
# #                                np.max(spectrogramPlot))
# #     self.img_Before.setImage(spectrogramPlot)
# #     self.img_Before.scale(time[-1]/np.size(spectrogramPlot, axis=1),
# #                           np.max(freq)/np.size(spectrogramPlot, axis=0))
# #     self.Spectroplot_Before.setLimits(
# #         xMin=0, xMax=time[-1], yMin=0, yMax=freq[-1])
# #     self.Spectroplot_Before.setLabel('bottom', "Time")
# #     self.Spectroplot_Before.setLabel('left', "Frequency")

# #     self.hist_After.setLevels(np.min(spectrogramPlot),
# #                               np.max(spectrogramPlot))
# #     self.img_After.setImage(spectrogramPlot)
# #     self.img_After.scale(time[-1]/np.size(spectrogramPlot, axis=1),
# #                          np.max(freq)/np.size(spectrogramPlot, axis=0))
# #     self.Spectroplot_After.setLimits(
# #         xMin=0, xMax=time[-1], yMin=0, yMax=freq[-1])
# #     self.Spectroplot_After.setLabel('bottom', "Time")
# #     self.Spectroplot_After.setLabel('left', "Frequency")
# def getFile(self):

#         self.filePath = QFileDialog.getOpenFileName(filter="wav (*.wav)")[0]
#         print("File :", self.filePath)
#         self.fileName = os.path.basename(self.filePath)
#         self.data, self.sampling_rate = librosa.load(
#             self.filePath, sr=None, mono=True, offset=0.0, duration=None)
#         self.Time = len(self.data) / self.sampling_rate
#         self.Graph_After.clear()
#         self.Graph_After.setTitle('After', color='w', size='12pt')
#         self.Graph_After.setLabel("left", "Amplitude")
#         self.Graph_After.setLabel("bottom", "Time")

#         self.Graph_After.plot(self.data)

#         self.Graph_Before.clear()
#         self.Graph_Before.setTitle('Before', color='w', size='12pt')
#         self.Graph_Before.setLabel("left", "Amplitude")
#         self.Graph_Before.setLabel("bottom", "Time")

#         self.Graph_Before.plot(self.data)
        
        
#         self.Spectrogram(self.data)
#         print(self.data)
#         print(self.sampling_rate)
#         print(len(self.data))


#     def Spectrogram(self, data):

#         self.img_After.clear()
#         self.img_Before.clear()
#         pg.setConfigOptions(imageAxisOrder='row-major')

#         freq, time, spectrogramPlot = signal.spectrogram(
#             data, self.sampling_rate)
            
#         self.hist_Before.setLevels(np.min(spectrogramPlot),
#                                 np.max(spectrogramPlot))

#         self.img_Before.setImage(spectrogramPlot)

#         self.img_Before.scale(time[-1]/np.size(spectrogramPlot, axis=1),
#                             np.max(freq)/np.size(spectrogramPlot, axis=0))

#         self.Spectroplot_Before.setLimits(
#             xMin=0, xMax=time[-1], yMin=0, yMax=freq[-1])
        

#         self.hist_After.setLevels(np.min(spectrogramPlot),
#                                 np.max(spectrogramPlot))
#         self.img_After.setImage(spectrogramPlot)
#         self.img_After.scale(time[-1]/np.size(spectrogramPlot, axis=1),
#                             np.max(freq)/np.size(spectrogramPlot, axis=0))
#         self.Spectroplot_After.setLimits(
#             xMin=0, xMax=time[-1], yMin=0, yMax=freq[-1])
#         self.Spectroplot_Before.setLabel('bottom', "Time")
#         self.Spectroplot_Before.setLabel('left', "Frequency")
#         self.Spectroplot_After.setLabel('bottom', "Time")
#         self.Spectroplot_After.setLabel('left', "Frequency")

#     def Gain(self):
#         self.N = self.sampling_rate * self.data/10000
#         normalized_tone = np.int16((self.data / self.data.max()) * 32767)
#         self.yrfft = rfft(normalized_tone)
#         self.xrfft = rfftfreq(self.N, 1 / self.sampling_rate)
#         self.points_per_freq = int(len(self.xrfft) / (self.sampling_rate / 2))
#         self.BW = int(self.points_per_freq*(self.sampling_rate / 20))
#         self.yrfft[:] = 0
#         #slider *self.BW : (slider+1)*self.BW] *= 0
#         self.yt = irfft(self.yrfft)
#         self.Graph_After.clear()
#         # self.Graph_After.setTitle('After', color='w', size='12pt')
#         # self.Graph_After.setLabel("left", "Amplitude")
#         # self.Graph_After.setLabel("bottom", "Time")
#         # self.Graph_After.plot(self.yt)
#         # write("Result.wav", self.sampling_rate, self.yt)
