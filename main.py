from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from scipy.fft import rfft, rfftfreq
from scipy.fft import irfft
import pyqtgraph as pg
from scipy import signal
import RetranslateUI
import Navigations
import Resources
import sys
import numpy as np
import librosa
import os
import sounddevice as sd
from fpdf import FPDF
from scipy.io import wavfile
from pyqtgraph import exporters
import contextlib
import wave

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.getFile()
        self.children = []
    

    


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(QtCore.QRect(0, 0, 1110, 450))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Resources/images/sig.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 0, 1070, 350))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(6, 0))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        #self.tabWidget.setDocumentMode(False)
        # self.tabWidget.setTabsClosable(True)
        # self.tabWidget.setMovable(True)
        #self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Graph_Before = pg.PlotWidget(self.tab)
        self.Graph_Before.setGeometry(QtCore.QRect(50, 550, 0 , 0))
        self.Graph_Before.setObjectName("Graph_Before")
        self.Graph_Before.setTitle("Before")

        self.Spectrogram_Before = pg.PlotWidget(self.tab)
        self.Spectrogram_Before.setGeometry(QtCore.QRect(1050, 520, 0, 0))
        self.Spectrogram_Before.setObjectName("Spectrogram_Before")

        self.Spectrogram_After = pg.PlotWidget(self.tab)
        self.Spectrogram_After.setGeometry(QtCore.QRect(1050, 10, 0, 0))
        self.Spectrogram_After.setObjectName("Spectrogram_After")



        self.Graph_After = pg.PlotWidget(self.tab)
        self.Graph_After.setGeometry(QtCore.QRect(50, 10, 961, 271))
        self.Graph_After.setObjectName("Graph_After")
        self.Graph_After.setTitle("After")
        
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(50, 310, 0, 0))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 15, 961, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.Slider = []
        for i in range(10):
            self.Slider.append(QtWidgets.QSlider(self.layoutWidget))
            sizePolicy.setHeightForWidth(
                self.Slider[i].sizePolicy().hasHeightForWidth())
            self.Slider[i].setSizePolicy(sizePolicy)
            self.Slider[i].setMaximum(5)
            self.Slider[i].setMinimum(0)
            self.Slider[i].setSliderPosition(1)
            self.Slider[i].setOrientation(QtCore.Qt.Vertical)
            self.Slider[i].setInvertedControls(False)
            self.Slider[i].setTickPosition(
                QtWidgets.QSlider.TicksBothSides)
            self.Slider[i].setTickInterval(1)
            self.Slider[i].setObjectName("Slider_{}".format(i+1))
            self.horizontalLayout.addWidget(self.Slider[i])

        self.SpectroSlider =[]
        for i in range(2):
            self.SpectroSlider.append(QtWidgets.QSlider(self.tab))
            sizePolicy.setHeightForWidth(
                self.SpectroSlider[i].sizePolicy().hasHeightForWidth())
            self.SpectroSlider[i].setSizePolicy(sizePolicy)
            self.SpectroSlider[i].setMaximum(10)
            self.SpectroSlider[i].setMinimum(0)
            self.SpectroSlider[i].setSliderPosition(10*i)
            self.SpectroSlider[i].setOrientation(QtCore.Qt.Horizontal)
            self.SpectroSlider[i].setInvertedControls(False)
            self.SpectroSlider[i].setTickPosition(
                QtWidgets.QSlider.TicksBothSides)
            self.SpectroSlider[i].setTickInterval(1)
            self.SpectroSlider[i].setGeometry(QtCore.QRect(1075,425-i*50,380,35))
            self.SpectroSlider[i].setObjectName("scpectoSlider_{}".format(i+1))
        


        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 180, 961, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = []
        for i in range(10):
            self.label.append(QtWidgets.QLabel(self.layoutWidget_2))
            self.label[i].setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.label[i].setIndent(3+i*6)
            self.label[i].setObjectName("label_{}".format(i+1))
            self.horizontalLayout_2.addWidget(self.label[i])

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1537, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNavigation = QtWidgets.QMenu(self.menubar)
        self.menuNavigation.setObjectName("menuNavigation")
        self.menuScroll = QtWidgets.QMenu(self.menuNavigation)
        self.menuScroll.setObjectName("menuScroll")
        self.menuZoom = QtWidgets.QMenu(self.menuNavigation)
        self.menuZoom.setObjectName("menuZoom")
        self.menuSpeed = QtWidgets.QMenu(self.menuNavigation)
        self.menuSpeed.setObjectName("menuSpeed")
        self.menuTheme = QtWidgets.QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        self.GraphTheme = QtWidgets.QMenu(self.menuTheme)
        self.GraphTheme.setObjectName("GraphTheme")
        self.SpectroTheme = QtWidgets.QMenu(self.menuTheme)
        self.SpectroTheme.setObjectName("SpectroTheme")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionWhite = QtWidgets.QAction(MainWindow)
        self.actionWhite.setObjectName("actionWhite")
        self.actionBlack = QtWidgets.QAction(MainWindow)
        self.actionBlack.setObjectName("actionBlack")
        self.actiontheme =[]
        for i in range(3):
            self.actiontheme.append(QtWidgets.QAction(MainWindow))
            self.actiontheme[i].setObjectName("actiontheme{n}]".format(n=i))

        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Resources/images/open.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")

        # self.actionNew = QtWidgets.QAction(MainWindow)
        # self.actionNew.setObjectName("actionNew")

        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Resources/images/save.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionTab = QtWidgets.QAction(MainWindow)
        self.actionTab.setObjectName("actionTab")
        self.actionZoom_in = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            ":/Resources/images/zoom in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_in.setIcon(icon3)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            ":/Resources/images/zoom out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_out.setIcon(icon4)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionLeft = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Resources/images/back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLeft.setIcon(icon5)
        self.actionLeft.setObjectName("actionLeft")
        self.actionRight = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Resources/images/next.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRight.setIcon(icon6)
        self.actionRight.setObjectName("actionRight")
        self.actionFaster = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(
            ":/Resources/images/Speed Up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFaster.setIcon(icon7)
        self.actionFaster.setObjectName("actionFaster")
        self.actionSlower = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(
            ":/Resources/images/Speed Down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSlower.setIcon(icon8)
        self.actionSlower.setObjectName("actionSlower")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        self.actionPlay.setCheckable(True)
        self.actionPlay.setChecked(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Resources/images/play.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap(":/Resources/images/pause.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionPlay.setIcon(icon9)
        self.actionPlay.setObjectName("actionPlay")
        self.actionSpectrogram = QtWidgets.QAction(MainWindow)
        self.actionSpectrogram.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(
            ":/Resources/images/spectr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpectrogram.setIcon(icon10)
        self.actionSpectrogram.setObjectName("actionSpectrogram")
        self.actionEqualizer = QtWidgets.QAction(MainWindow)
        self.actionEqualizer.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(
            ":/Resources/images/Equalizer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEqualizer.setIcon(icon11)
        self.actionEqualizer.setObjectName("actionEqualizer")
        self.actionSound = QtWidgets.QAction(MainWindow)
        self.actionSound.setCheckable(True)
        self.actionSound.setChecked(False)
        icon12 = QtGui.QIcon() 
        icon12.addPixmap(QtGui.QPixmap(
            "images/sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  
        self.actionSound.setIcon(icon12)    
        self.actionSound.setObjectName("actionSound")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        # self.actionClose_Tab = QtWidgets.QAction(MainWindow)
        # self.actionClose_Tab.setObjectName("actionClose_Tab")
        # self.actionGraph_theme = QtWidgets.QAction(MainWindow)
        # self.actionGraph_theme.setObjectName("actionGraph_theme")
        # self.actionSpectrogram_theme = QtWidgets.QAction(MainWindow)
        # self.actionSpectrogram_theme.setObjectName("actionSpectrogram_theme")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        # self.menuFile.addAction(self.actionNew)
        # self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        # self.menuFile.addAction(self.actionClose_Tab)

        self.menuScroll.addAction(self.actionLeft)
        self.menuScroll.addAction(self.actionRight)
        self.menuZoom.addAction(self.actionZoom_in)
        self.menuZoom.addAction(self.actionZoom_out)
        self.menuSpeed.addAction(self.actionFaster)
        self.menuSpeed.addAction(self.actionSlower)
        self.GraphTheme.addAction(self.actionWhite)
        self.GraphTheme.addAction(self.actionBlack)
        for i in range(3):
            self.SpectroTheme.addAction(self.actiontheme[i])

        self.menuNavigation.addAction(self.menuZoom.menuAction())
        self.menuNavigation.addSeparator()
        self.menuNavigation.addAction(self.menuScroll.menuAction())
        self.menuNavigation.addSeparator()
        self.menuNavigation.addAction(self.actionPlay)
        self.menuNavigation.addAction(self.actionSound)
        self.menuNavigation.addAction(self.menuSpeed.menuAction())
        self.menuNavigation.addSeparator()
        self.menuNavigation.addAction(self.actionSpectrogram)
        self.menuNavigation.addAction(self.actionEqualizer)
        self.menuTheme.addAction(self.GraphTheme.menuAction())
        self.menuTheme.addAction(self.SpectroTheme.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuNavigation.menuAction())
        self.menubar.addAction(self.menuTheme.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_out)
        self.toolBar.addAction(self.actionZoom_in)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSlower)
        self.toolBar.addAction(self.actionLeft)
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionSound)
        self.toolBar.addAction(self.actionRight)
        self.toolBar.addAction(self.actionFaster)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEqualizer)
        self.toolBar.addAction(self.actionSpectrogram)
        self.data =[]
        self.Pallete0 = [75, 0, 115, 255]
        self.Pallete0_5 = [0, 180, 190, 255]
        self.Pallete1 = [245, 110, 0, 255]
        self.speed = 500
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: Navigations.Update(self))
        self.timer.setInterval(100)
        self.timer.start()
        self.open =0
        self.duration =0
        self.minvalue = 0
        self.middlevalue =0.5
        self.maxvalue = 1

                                                                        #Methods' Declaration
        retranslateUi = RetranslateUI.retranslateUi

                                                                        #Calling Methods

        retranslateUi(self, MainWindow)
        self.actionOpen.triggered.connect(self.getFile)
        # self.actionNew.triggered.connect(self.show_child)
        self.actionSpectrogram.triggered.connect(
            lambda : Navigations.ShowSpectrogram(self,MainWindow))
        self.actionEqualizer.triggered.connect(
            lambda: Navigations.ShowEqualizer(self, MainWindow))
        self.actionZoom_in.triggered.connect(lambda : Navigations.Zoom_in(self))
        self.actionZoom_out.triggered.connect(lambda : Navigations.Zoom_out(self))
        self.actionLeft.triggered.connect(lambda : Navigations.scroll_left(self))
        self.actionRight.triggered.connect(lambda : Navigations.scroll_right(self))
        self.actionPlay.triggered.connect(self.timer.start)
        self.actionFaster.triggered.connect(lambda : Navigations.SpeedUp(self))
        self.actionSlower.triggered.connect(lambda : Navigations.SpeedDown(self))
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSound.triggered.connect(self.play_audio)
        self.actionWhite.triggered.connect(self.White_background)
        self.actionBlack.triggered.connect(self.Black_background)
        self.actiontheme[0].triggered.connect(lambda : self.theme(1))
        self.actiontheme[1].triggered.connect(lambda: self.theme(2))
        self.actiontheme[2].triggered.connect(lambda: self.theme(3))
        for i in range(10):
            self.Slider[i].valueChanged.connect(lambda : self.Gain(self.data))
        
        self.SpectroSlider[0].valueChanged.connect(self.minchange)
        self.SpectroSlider[1].valueChanged.connect(self.maxchange)
        

    def White_background(self):
        self.Graph_Before.setBackground('w')
        self.Graph_After.setBackground('w')
        self.Spectrogram_Before.setBackground('w')
        self.Spectrogram_After.setBackground('w')

    def Black_background(self):
        self.Graph_Before.setBackground('#000')
        self.Graph_After.setBackground('#000')
        self.Spectrogram_Before.setBackground('#000')
        self.Spectrogram_After.setBackground('#000')
    
    def theme (self,i=1):
        if i ==1:
            self.Pallete0 = [75, 0, 115, 255]
            self.Pallete0_5 = [0, 180, 190, 255]
            self.Pallete1 = [245, 110, 0, 255]
        elif i == 2:
            self.Pallete0 = [245, 0, 115, 255]
            self.Pallete0_5 = [0, 180, 190, 255]
            self.Pallete1 = [75, 110, 0, 255]
        elif i == 3:
            self.Pallete0 = [0, 180, 190, 255]
            self.Pallete0_5 = [245, 110, 0, 255]
            self.Pallete1 = [75, 0, 115, 255]

        yt = self.fft(self.signalData)
        self.Spectrogram(self.signalData)
        self.updateSpectrogram(yt)

    def colorchange(self):
        self.minvalue = (self.SpectroSlider[0].value()/10)
        self.maxvalue = (self.SpectroSlider[1].value()/10)
        self.middlevalue = (self.maxvalue + self.minvalue)/2

        yt = self.fft(self.signalData)
        self.Spectrogram(self.signalData)
        self.updateSpectrogram(yt)

    def maxchange(self):
        if self.SpectroSlider[1].value() > self.SpectroSlider[0].value():
            self.colorchange()
        else:
            self.SpectroSlider[1].setSliderPosition(
                self.SpectroSlider[0].value()+1)

    def minchange(self):
        if self.SpectroSlider[1].value() > self.SpectroSlider[0].value():
            self.colorchange()
        else:    
            self.SpectroSlider[0].setSliderPosition(
                self.SpectroSlider[1].value()-1)
            
       
    
    def getFile(self):
        if self.open ==0:
            self.filePath = QFileDialog.getOpenFileName(filter="wav (*.wav)")[0]
            self.fileName = os.path.basename(self.filePath)

            self.tabWidget.addTab(self.tab, self.fileName)
            with contextlib.closing(wave.open(self.filePath, 'r')) as f:
                self.frames = f.getnframes()
                self.rate = f.getframerate()
            self.duration = self.frames / float(self.rate)
            self.samplingfrequency, self.signalData = wavfile.read(self.filePath)
            self.array=np.asarray(self.signalData)

            
            if len(self.array.shape) == 2:
                for i in range(len(self.signalData)):
                    self.data.append(self.signalData[i][0])
            else:
                for i in range(len(self.signalData)):
                    self.data.append(self.signalData[i])
            self.time = np.arange(0,self.duration,1/self.samplingfrequency)
            intial_plot = self.fft(self.data)
            self.Graph_After.setXRange(0, self.duration, padding=0)
            self.Graph_Before.setXRange(0,self.duration, padding=0)
            self.plotAfter(intial_plot)
            self.plotBefore(intial_plot)
            self.Spectrogram(self.signalData)
            self.updateSpectrogram(self.signalData)
            self.open = 1
        else:
            self.show_child()

    def Gain(self,data):
        update =  self.fft(data)
        self.plotAfter(update)
        self.updateSpectrogram(update)
        if self.actionSound.isChecked():
            self.play_audio()

    def fft(self,data):
        self.N = self.samplingfrequency * int(self.duration)
        self.yrfft = rfft(np.real(data))
        self.xrfft = rfftfreq(int(self.N), 1.0 / self.samplingfrequency)
        # self.max_freq = np.max(self.xrfft)
        sumofgain =0
        self.BW = int(len(self.yrfft)/10)
        for i in range (10):
            self.yrfft[i*self.BW : (i+1)*self.BW]*=self.Slider[i].value()
            sumofgain += self.Slider[i].value()
        if sumofgain == 0:
            self.yrfft[:] =0
        yt = irfft(self.yrfft)
        return np.real(yt) 

    def Spectrogram(self, data):
        self.Spectrogram_Before.clear()
        self.Spectrogram_Before.plotItem.clear()
        pg.setConfigOptions(imageAxisOrder='row-major')
        freq, time, Spectrodata = signal.spectrogram(
            data, self.samplingfrequency)
        img_After = pg.ImageItem()
        self.Spectrogram_Before.addItem(img_After)
        hist_After = pg.HistogramLUTItem()
        hist_After.setImageItem(img_After)
        hist_After.setLevels(min=np.min(Spectrodata), max=np.max(Spectrodata))
        hist_After.gradient.restoreState(
            {'mode': 'rgb',
                'ticks':[(self.maxvalue, self.Pallete1), 
                        (self.middlevalue, self.Pallete0_5),
                        (self.minvalue, self.Pallete0)]})
        img_After.setImage(Spectrodata)
        img_After.scale(time[-1]/np.size(Spectrodata, axis=1),
                        freq[-1]/np.size(Spectrodata, axis=0))
        self.Spectrogram_Before.addItem(img_After)
        self.Spectrogram_Before.setLimits(
            xMin=time[0], xMax=time[-1],
             yMin=freq[0], yMax=freq[-1])
        self.Spectrogram_Before.setYRange(freq[0], freq[-1])
        self.Spectrogram_Before.setLabel('bottom', "Time", units='s')
        self.Spectrogram_Before.setLabel('left', "Frequency", units='Hz')
        self.Spectrogram_Before.setLabel('right', "Frequency", units='Hz')
        self.Spectrogram_Before.plotItem.setTitle("After")
        
    def updateSpectrogram(self,data):
        self.Spectrogram_After.clear()
        self.Spectrogram_After.plotItem.clear()
        pg.setConfigOptions(imageAxisOrder='row-major')
        freq, time, Spectrodata = signal.spectrogram(
            data, self.samplingfrequency)        
        img_After = pg.ImageItem()
        self.Spectrogram_After.addItem(img_After)
        hist_After = pg.HistogramLUTItem()
        hist_After.setImageItem(img_After)
        hist_After.setLevels(min=np.min(Spectrodata), max=np.max(Spectrodata))
        hist_After.gradient.restoreState(
            {'mode': 'rgb',
                'ticks':[(self.maxvalue , self.Pallete1),
                        (self.middlevalue,self.Pallete0_5),
                        (self.minvalue , self.Pallete0)]})
        img_After.setImage(Spectrodata)
        img_After.scale(time[-1]/np.size(Spectrodata, axis=1),
                        freq[-1]/np.size(Spectrodata, axis=0))
        self.Spectrogram_After.addItem(img_After)
        self.Spectrogram_After.setLimits(
            xMin=time[0], xMax=time[-1],
            yMin=freq[0], yMax=freq[-1])
        self.Spectrogram_After.setYRange(freq[0], freq[-1])
        self.Spectrogram_After.setLabel('bottom', "Time", units='s')
        self.Spectrogram_After.setLabel('left', "Frequency", units='Hz')
        self.Spectrogram_After.setLabel('right', "Frequency", units='Hz')
        self.Spectrogram_After.plotItem.setTitle("After")
        
    def play_audio(self):
        if self.actionSound.isChecked():
            sd.play(self.fft(self.data) / np.max(self.fft(self.data)),
                    self.samplingfrequency,loop=True)
        else:
            sd.stop(self.data)
            self.actionSound.setChecked(False)

    def saveFile(self):
        # allows the user to save the file and name it as they like
        if len(self.data) >0:
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(
                None, "WAV files (.wav)")
            name = filename
            if filename:
                if QtCore.QFileInfo(filename).suffix() == "":
                    filename += ".wav"
                self.generate_WavFile(filename)
                self.PDF_Report(name)

    def generate_WavFile(self, filename):
        maximum = np.max(np.abs(self.yt))
        data = (self.yt / maximum).astype(np.float32)
        wavfile.write(filename, int(self.samplingfrequency), data)  

    def PDF_Report(self,filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 15)
        pdf.set_xy(0, 0)

        pdf.cell(0, 10, 'Graph After', ln=1, align='C')
        exporter = exporters.ImageExporter(self.Graph_After.plotItem)
        exporter.parameters()['width'] = 500
        exporter.parameters()['height'] = 250
        exporter.export('GraphAfter.png')
        pdf.image('GraphAfter.png', x=None, y=None, w=180, h=50)

        pdf.cell(0, 10, 'spectrogram After', ln=1, align='C')

        exporter = exporters.ImageExporter(self.Spectrogram_After.plotItem)
        exporter.parameters()['width'] = 500
        exporter.parameters()['height'] = 250
        exporter.export('SpectroAfter.png')
        pdf.image('SpectroAfter.png', x=None, y=None, w=180, h=50)

        pdf.cell(0, 10, 'Graph Before', ln=1, align='C')
        exporter = exporters.ImageExporter(self.Graph_Before.plotItem)
        exporter.parameters()['width'] = 500
        exporter.parameters()['height'] = 250
        exporter.export('GraphBefore.png')
        pdf.image('GraphBefore.png', x=None, y=None, w=180, h=50)

        pdf.cell(0, 10, 'Spectrogram Before', ln=1, align='C')
        exporter = pg.exporters.ImageExporter(self.Spectrogram_Before.plotItem)
        exporter.parameters()['width'] = 500
        exporter.parameters()['height'] = 250
        exporter.export('SpectroBefore.png')
        pdf.image('SpectroBefore.png', x=None, y=None, w=180, h=50)

        pdf.output(filename.replace('.wav' ,'.pdf'))

    def show_child(self):
        child = ApplicationWindow()
        child.show()
        self.children.append(child)

    def plotAfter(self,data):
        self.Graph_After.clear()
        self.Graph_After.setTitle('After', color='w', size='12pt')
        self.Graph_After.setLabel("left", "Amplitude")
        self.Graph_After.setLabel("bottom", "Time")
        self.Graph_After.setYRange(-max(data),max(data))
        self.Graph_Before.setYRange(-max(data),
                                    max(data))
        self.Graph_After.plot(self.time,data)

    def plotBefore(self,data):
        self.Graph_Before.clear()
        self.Graph_Before.setTitle('Before', color='w', size='12pt')
        self.Graph_Before.setLabel("left", "Amplitude")
        self.Graph_Before.setLabel("bottom", "Time")
        self.Graph_Before.plot(self.time, data)

app = QtWidgets.QApplication(sys.argv)
application = ApplicationWindow()
application.show()
app.exec_()
