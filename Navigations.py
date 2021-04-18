
def Zoom_in(self):
    self.xrange, yrange = self.Graph_After.viewRange()
    if self.xrange[1]-self.xrange[0] > self.duration/1000:
        self.Graph_After.setXRange(self.xrange[0]/2 , self.xrange[1]/2 , padding=0)
        self.Graph_Before.setXRange(self.xrange[0]/2 , self.xrange[1]/2 , padding=0)


def Zoom_out(self):
    self.xrange, yrange = self.Graph_After.viewRange()
    if self.xrange[1]*2 <= self.duration+1:
        self.Graph_After.setXRange(self.xrange[0]*2 , self.xrange[1] * 2, padding=0)
        self.Graph_Before.setXRange(self.xrange[0]*2 , self.xrange[1] * 2, padding=0)
    else:
        self.Graph_After.setXRange(0, self.duration, padding=0)
        self.Graph_Before.setXRange(0, len(self.duration), padding=0)


def scroll_right(self):
    self.xrange, yrange = self.Graph_After.viewRange()
    if self.xrange[1]<self.duration-0.1:
        self.Graph_After.setXRange(self.xrange[0] + self.speed/1000, self.xrange[1] + self.speed/1000, padding=0)
        self.Graph_Before.setXRange(
            self.xrange[0] + self.speed/1000, self.xrange[1] + self.speed/1000, padding=0)


def scroll_left(self):
    self.xrange, yrange = self.Graph_After.viewRange()
    if self.xrange[0]>0:
        self.Graph_After.setXRange(self.xrange[0] - self.speed/1000, self.xrange[1] - self.speed/1000, padding=0)
        self.Graph_Before.setXRange(
            self.xrange[0] - self.speed/1000, self.xrange[1] - self.speed/1000, padding=0)
    else:
        self.Graph_After.setXRange(0, self.xrange[1]-self.xrange[0], padding=0)
        self.Graph_Before.setXRange(0, self.xrange[1]-self.xrange[0], padding=0)


def Update(self):
    self.xrange, yrange = self.Graph_After.viewRange()
    if len(self.data) > 0 and self.actionPlay.isChecked():
        self.Graph_After.setXRange(
            self.xrange[0]+self.speed/10000, self.xrange[1] + self.speed/10000, padding=0)
        self.Graph_Before.setXRange(
            self.xrange[0]+self.speed/10000, self.xrange[1] + self.speed/10000, padding=0)
    if self.xrange[1] > self.duration:
        self.timer.stop()
        self.actionPlay.setChecked(False)
        self.Graph_After.setXRange(
            self.xrange[0]+self.speed/10000, self.duration, padding=0)
        self.Graph_Before.setXRange(
            self.xrange[0]+self.speed/10000, self.duration, padding=0)
    

def SpeedUp(self):
    if self.speed < 1000:
        self.speed +=100


def SpeedDown(self):
    if self.speed >100:
        self.speed -= 100


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
