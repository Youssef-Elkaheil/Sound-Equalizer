def Zoom_in(self):
    xrange, yrange = self.Graph_After.viewRange()
    if xrange[1] > len(self.data)/100:
        self.Graph_After.setXRange(xrange[0]/2 , xrange[1]/2 , padding=0)
        self.Graph_Before.setXRange(xrange[0]/2 , xrange[1]/2 , padding=0)


def Zoom_out(self):
    xrange, yrange = self.Graph_After.viewRange()
    if xrange[1]*2 <= len(self.data)+10000:
        self.Graph_After.setXRange(xrange[0]*2 , xrange[1] * 2, padding=0)
        self.Graph_Before.setXRange(xrange[0]*2 , xrange[1] * 2, padding=0)
    else:
        self.Graph_After.setXRange(0, len(self.data), padding=0)
        self.Graph_Before.setXRange(0, len(self.data), padding=0)


def scroll_right(self):
    xrange, yrange = self.Graph_After.viewRange()
    if xrange[1]<len(self.data):
        self.Graph_After.setXRange(xrange[0] + 500, xrange[1] + 500, padding=0)
        self.Graph_Before.setXRange(
            xrange[0] + 500, xrange[1] + 500, padding=0)


def scroll_left(self):
    xrange, yrange = self.Graph_After.viewRange()
    if xrange[0]>0:
        self.Graph_After.setXRange(xrange[0] - 500, xrange[1] - 500, padding=0)
        self.Graph_Before.setXRange(
            xrange[0] - 500, xrange[1] - 500, padding=0)


