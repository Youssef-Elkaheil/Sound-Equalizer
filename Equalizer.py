import math
import numpy as np

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

# def setBands(self):
        # bands=[]
        # self.eq_bands=[]
        # BW = math.ceil(len(np.abs(self.data))/20)
# 
        # for i in range(0, 20):
            # bands.append(self.data[i*BW:(i+1)*BW])
# 
        # self.eq_bands.clear()
        # self.eq_bands = bands.copy()
#    
# 
# def gain(self,i,Gain=1):
    # after_eq=[]
    # after_eq.clear()
# 
    # self.eq_bands[i]=self.bands[i]*Gain
    # self.eq_bands[20-i-1]=self.bands[20-i-1]*Gain
    # for sublist in self.eq_bands :
        # for x in sublist:
                # after_eq.append(x)
    # recover=np.array(self.recover_signal())
# 
    # self.fft(3,recover)
    # self.Graph_After.clear()
    # self.Graph_After.plot(recover)




