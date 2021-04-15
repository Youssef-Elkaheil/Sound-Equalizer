def Zoom_in(self):
    self.xrange, self.yrange = self.Graph_After.viewRange()
    if self.xrange[1]-self.xrange[0] > len(self.data)/100:
        self.Graph_After.setXRange(self.xrange[0]/2 , self.xrange[1]/2 , padding=0)
        self.Graph_Before.setXRange(self.xrange[0]/2 , self.xrange[1]/2 , padding=0)


def Zoom_out(self):
    self.xrange, self.yrange = self.Graph_After.viewRange()
    if self.xrange[1]*2 <= len(self.data)+10000:
        self.Graph_After.setXRange(self.xrange[0]*2 , self.xrange[1] * 2, padding=0)
        self.Graph_Before.setXRange(self.xrange[0]*2 , self.xrange[1] * 2, padding=0)
    else:
        self.Graph_After.setXRange(0, len(self.data), padding=0)
        self.Graph_Before.setXRange(0, len(self.data), padding=0)


def scroll_right(self):
    self.xrange, self.yrange = self.Graph_After.viewRange()
    if self.xrange[1]<len(self.data):
        self.Graph_After.setXRange(self.xrange[0] + 100, self.xrange[1] + 100, padding=0)
        self.Graph_Before.setXRange(
            self.xrange[0] + 100, self.xrange[1] + 100, padding=0)


def scroll_left(self):
    self.xrange, self.yrange = self.Graph_After.viewRange()
    if self.xrange[0]>0:
        self.Graph_After.setXRange(self.xrange[0] - 100, self.xrange[1] - 100, padding=0)
        self.Graph_Before.setXRange(
            self.xrange[0] - 100, self.xrange[1] - 100, padding=0)


def Update(self):

    if len(self.data) > 0 and self.actionPlay.isChecked():
        xrange1, yrange1 = self.Graph_After.viewRange()
        self.Graph_After.setXRange(
            xrange1[0]+100, xrange1[1] + 100, padding=0)
        self.Graph_Before.setXRange(
            xrange1[0]+100, xrange1[1] + 100, padding=0)
        if xrange1[1] > len(self.data)-100:
            self.timer.stop()
