
def Zoom(self,flag):
    xrange, yrange = self.Graph_After.viewRange()
    if flag ==1:       #Zoom in
        x = [i/2 for i in xrange]
    elif flag ==0:     #Zoom out
        x = [ i*2 for i in xrange]
    if xrange[1]*2 <= self.duration+1 or flag ==1:
        self.Graph_After.setXRange(x[0], x[1], padding=0)
        self.Graph_Before.setXRange(x[0], x[1], padding=0)
    else:
        self.Graph_After.setXRange(0, self.duration, padding=0)
        self.Graph_Before.setXRange(0, self.duration, padding=0)

def Scroll (self,flag):
    xrange, yrange = self.Graph_After.viewRange()
    if flag == 1:  # scroll right
        x = [i+self.step for i in xrange]
    elif flag == 0:  # scroll left
        x = [i-self.step for i in xrange]
    if x[0]>0 and x[1]<self.duration:
        self.Graph_After.setXRange(x[0], x[1], padding=0)
        self.Graph_Before.setXRange(x[0], x[1], padding=0)
    else:
        self.timer.stop()
        self.actionPlay.setChecked(False)
        
def Update(self):
    xrange, yrange = self.Graph_After.viewRange()
    if self.actionPlay.isChecked():
        Scroll(self,1)



def SpeedUp(self):
    if self.step <0.16:
        self.step *= 2
    # self.timer.setInterval(self.speed)



def SpeedDown(self):
    if self.step >0.0025:
        self.step /=2
    # self.timer.setInterval(self.speed)

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

# def Zoom_in(self):
#     xrange, yrange = self.Graph_After.viewRange()
#     self.Graph_After.setXRange(xrange[0]/2 , xrange[1]/2 , padding=0)
#     self.Graph_Before.setXRange(xrange[0]/2 , xrange[1]/2 , padding=0)


# def Zoom_out(self):
#     xrange, yrange = self.Graph_After.viewRange()
#     if xrange[1]*2 <= self.duration+1:
#         self.Graph_After.setXRange(xrange[0]*2 , xrange[1] * 2, padding=0)
#         self.Graph_Before.setXRange(xrange[0]*2 , xrange[1] * 2, padding=0)
#     else:
#         self.Graph_After.setXRange(0, self.duration, padding=0)
#         self.Graph_Before.setXRange(0,self.duration, padding=0)


# def scroll_right(self):
#     xrange, yrange = self.Graph_After.viewRange()
#     if xrange[1] < self.duration-self.step:
#         self.Graph_After.setXRange(xrange[0] + self.step, xrange[1] + self.step, padding=0)
#         self.Graph_Before.setXRange(xrange[0] + self.step, xrange[1] + self.step, padding=0)
#     else:
#         self.timer.stop()
#         self.actionPlay.setChecked(False)
    #     self.Graph_After.setXRange(
    #         self.duration - self.step, self.duration, padding=0)
    #     self.Graph_Before.setXRange(
    #         self.duration - self.step, self.duration, padding=0)



# def scroll_left(self):
#     xrange, yrange = self.Graph_After.viewRange()
#     if xrange[0]>0:
#         self.Graph_After.setXRange(xrange[0] - self.step, xrange[1] - self.step, padding=0)
#         self.Graph_Before.setXRange(
#             xrange[0] - self.step, xrange[1] - self.step, padding=0)
    # else:
    #     self.Graph_After.setXRange(0, self.step, padding=0)
    #     self.Graph_Before.setXRange(0, self.step, padding=0)


    

