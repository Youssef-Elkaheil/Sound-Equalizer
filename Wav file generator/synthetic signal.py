from scipy.fft import irfft
from scipy.fft import rfft, rfftfreq
from scipy.io.wavfile import write
from matplotlib import pyplot as plt
import numpy as np

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


# Generate a 2 hertz sine wave that lasts for 5 seconds
# x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)
#plt.plot(x, y)
#plt.show()
mixed_tone =0
for i in range(11):
    _, nice_tone = generate_sine_wave(10000*i, SAMPLE_RATE, DURATION)
    nice_tone *=(10-i)
    mixed_tone += nice_tone


#mixed_tone = nice_tone + noise_tone 


normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

plt.plot(mixed_tone[:1000])
plt.show()


# Remember SAMPLE_RATE = 44100 Hz is our playback rate
write("mysinewave.wav", SAMPLE_RATE, normalized_tone)


# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION
print(SAMPLE_RATE , DURATION)

# Note the extra 'r' at the front
yrf = rfft(mixed_tone)
xrf = rfftfreq(N, 1 / SAMPLE_RATE)
#print(yrf)
#print(xrf)
plt.plot(xrf, np.abs(yrf))
plt.show()

# The maximum frequency is half the sample rate
points_per_freq = len(xrf) / (SAMPLE_RATE / 2)
#print(points_per_freq)
# Our target frequency is 4000 Hz
target_idx = int(points_per_freq * 100)
#print (target_idx)
yrf[target_idx:] *=0

plt.plot(xrf, np.abs(yrf))
plt.show()

new_sig = irfft(yrf)

plt.plot(new_sig[:1000])
plt.show()


# norm_new_sig = np.int16(new_sig * (32767 / new_sig.max()))

write("clean.wav", SAMPLE_RATE,new_sig)




