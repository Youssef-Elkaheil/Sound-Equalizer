import math
import numpy as np
def bands(self):
        global bands_list, eq_bands
        BW = math.ceil(len(np.abs(yf))/20)

        for i in range(0, 20):
            bands_list.append(yf[i*BW:(i+1)*BW])

        eq_bands.clear()
        eq_bands = bands_list.copy()
   

def gain(self,i,Gain=1):
    global after_eq
    after_eq.clear()

    eq_bands[i]=bands_list[i]*Gain
    eq_bands[20-i-1]=bands_list[20-i-1]*Gain
    for sublist in eq_bands :
        for x in sublist:
                after_eq.append(x)
    recover=np.array(self.recover_signal())

    self.fft(3,recover)

