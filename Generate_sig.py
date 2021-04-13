import math
import struct
import wave
import numpy as np
def generatingSignal():
    if __name__ == '__main__':

        data_size = 100000
        fname = "test.wav"
        frate = 11025.0
        amp = 64000.0
        nchannels = 1
        sampwidth = 2
        framerate = int(frate)
        nframes = data_size
        comptype = "NONE"
        compname = "not compressed"
        sine_list = []
        freq = 100
        itr = 10000
        for x in range(data_size):
            if x > itr:
                itr += 10000
                freq += 20
            sine_list.append(math.sin(2 * math.pi * freq * (x / frate)))
        wav_file = wave.open(fname, 'w')
        wav_file.setparams(
            (nchannels, sampwidth, framerate, nframes, comptype, compname))
        for v in sine_list:
            wav_file.writeframes(struct.pack('h', int(v * amp / 2)))
        wav_file.close()
        
        if __name__ == '__main__':
            data_size = 40000
            fname = "test.wav"
            frate = 11025.0
            wav_file = wave.open(fname, 'r')
            data = wav_file.readframes(data_size)
            wav_file.close()
            data = struct.unpack('{n}h'.format(n=data_size), data)
            data = np.array(data)

            w = np.fft.fft(data)
            freqs = np.fft.fftfreq(len(w))
            print(freqs.min(), freqs.max())
            # (-0.5, 0.499975)

            # Find the peak in the coefficients
            idx = np.argmax(np.abs(w))
            freq = freqs[idx]
            freq_in_hertz = abs(freq * frate)
            print(freq_in_hertz)
            # 439.8975
generatingSignal()
