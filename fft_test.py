# import scipy.io.wavfile as wavfile
# import scipy
# import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt
import math
import struct
import wave
import numpy as np
# def generatingSignal(self):
#     if __name__ == '__main__':

#         data_size = 100000
#         fname = "test.wav"
#         frate = 11025.0
#         amp = 64000.0
#         nchannels = 1
#         sampwidth = 2
#         framerate = int(frate)
#         nframes = data_size
#         comptype = "NONE"
#         compname = "not compressed"
#         sine_list = []
#         freq = 0
#         itr = 0
#         for x in range(data_size):
#             if x > itr:
#                 itr += 1000
#                 freq += 10
#             sine_list.append(math.sin(2 * math.pi * freq * (x / frate)))
#         wav_file = wave.open(fname, 'w')
#         wav_file.setparams(
#             (nchannels, sampwidth, framerate, nframes, comptype, compname))
#         for v in sine_list:
#             wav_file.writeframes(struct.pack('h', int(v * amp / 2)))
#         wav_file.close()
        
#         if __name__ == '__main__':
#             data_size = 40000
#             fname = "test.wav"
#             frate = 11025.0
#             wav_file = wave.open(fname, 'r')
#             data = wav_file.readframes(data_size)
#             wav_file.close()
#             data = struct.unpack('{n}h'.format(n=data_size), data)
#             data = np.array(data)

#             w = np.fft.fft(data)
#             freqs = np.fft.fftfreq(len(w))
#             print(freqs.min(), freqs.max())
#             # (-0.5, 0.499975)

#             # Find the peak in the coefficients
#             idx = np.argmax(np.abs(w))
#             freq = freqs[idx]
#             freq_in_hertz = abs(freq * frate)
#             print(freq_in_hertz)
#             # 439.8975
#             generatingSignal()

# dt=0.01
# n = 100000
# fhat = np.fft.fft(self.freq,n)
# psd = fhat * np.conj(fhat)/n 
# freq = (1/(dt*n)) * np.arange(n)
# fig,axs = plt.subplots(2,1)
# plt.sca(axs[0])
# plt.plot(t,f,color='r',linewidth=1.5 , label='noisy')
# plt.plot(t,f_clean ,color='b' ,linewidth=1.5 , label='clean')

# plt.xlim(t[0],t[-1])
# plt.legend()

# fig,axs = plt.subplots(2,1)

# plt.sca(axs[1])
# plt.plot(freq,psd,color='r',linewidth=1.5 , label='noisy')

# plt.xlim(freq[0],freq[-1])
# plt.legend()
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.arange(0,1,dt)
f =np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
f_clean = f
f = f + 2.5*np.random.randn(len(t))
plt.plot(t,f,color='r',linewidth=1.5 , label='noisy')
plt.plot(t,f_clean ,color='b' ,linewidth=1.5 , label='clean')

plt.xlim(t[0],t[-1])
plt.legend()

n = len(t)
fhat = np.fft.fft(f,n)
psd = fhat * np.conj(fhat)/n 
freq = (1/(dt*n)) * np.arange(n)
fig,axs = plt.subplots(2,1)
plt.sca(axs[0])
plt.plot(t,f,color='r',linewidth=1.5 , label='noisy')
plt.plot(t,f_clean ,color='b' ,linewidth=1.5 , label='clean')

plt.xlim(t[0],t[-1])
plt.legend()

fig,axs = plt.subplots(2,1)

plt.sca(axs[1])
plt.plot(freq,psd,color='r',linewidth=1.5 , label='noisy')

plt.xlim(freq[0],freq[-1])
plt.legend()
plt.show()