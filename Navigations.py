
def Zoom_in(self):
    self.xrange, yrange = self.Graph_After.viewRange()
    if self.xrange[1]-self.xrange[0] > len(self.data)/100:
        self.Graph_After.setXRange(self.xrange[0]/2 , self.xrange[1]/2 , padding=0)
        self.Graph_Before.setXRange(self.xrange[0]/2 , self.xrange[1]/2 , padding=0)


def Zoom_out(self):
    self.xrange, yrange = self.Graph_After.viewRange()
    if self.xrange[1]*2 <= len(self.data)+1000:
        self.Graph_After.setXRange(self.xrange[0]*2 , self.xrange[1] * 2, padding=0)
        self.Graph_Before.setXRange(self.xrange[0]*2 , self.xrange[1] * 2, padding=0)
    else:
        self.Graph_After.setXRange(0, len(self.data), padding=0)
        self.Graph_Before.setXRange(0, len(self.data), padding=0)


def scroll_right(self):
    self.xrange, yrange = self.Graph_After.viewRange()
    if self.xrange[1]<len(self.data):
        self.Graph_After.setXRange(self.xrange[0] + self.speed, self.xrange[1] + self.speed, padding=0)
        self.Graph_Before.setXRange(
            self.xrange[0] + self.speed, self.xrange[1] + self.speed, padding=0)


def scroll_left(self):
    self.xrange, yrange = self.Graph_After.viewRange()
    if self.xrange[0]>0:
        self.Graph_After.setXRange(self.xrange[0] - self.speed, self.xrange[1] - self.speed, padding=0)
        self.Graph_Before.setXRange(
            self.xrange[0] - self.speed, self.xrange[1] - self.speed, padding=0)


def Update(self):
    self.xrange, yrange = self.Graph_After.viewRange()
    if len(self.data) > 0 and self.actionPlay.isChecked():
        self.Graph_After.setXRange(
            self.xrange[0]+self.speed, self.xrange[1] + self.speed, padding=0)
        self.Graph_Before.setXRange(
            self.xrange[0]+self.speed, self.xrange[1] + self.speed, padding=0)
    if self.xrange[1] > len(self.data)-1000 or self.xrange[0] <-100:
        self.timer.stop()

def SpeedUp(self):
    if self.speed < 1000:
        self.speed +=100


def SpeedDown(self):
    if self.speed >100:
        self.speed -= 100
