import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy import pi
from scipy.fftpack import fft

t = np.linspace(0,3,12*1024)
notes = np.array([349.23,174.61,293.66,196.0,293.66,440.0,196.0,392.0,196.0])
count = 0
sum = 0.0
for i in notes:
   unitStepI =  np.reshape([t>=count],np.shape(t))
   unitStepF = np.reshape([t>count+0.3],np.shape(t))
   count += 0.35
   diffUnitStep = np.logical_xor(unitStepI,unitStepF) 
   x = np.sin(2.0 * np.pi * i * t) * diffUnitStep
   plt.plot(t,x)
   sum += x
#sd.play(sum,3.94*1024)
  
B=1024 
N = (3-0)*B
f = np. linspace(0 , 512 , int(N/2))

"Fourier Transform of original song"
x_f = fft(sum)
x_f = 2/N * np.abs(x_f [0:np.int(N/2)])

"Plotting Original Signal Before and After Transform"
plt.subplot(3, 2, 1)
plt.plot(f,x_f)
plt.title('Frequency domain Signal') 
plt.xlabel('Frequency in Hz') 
plt.ylabel('Amplitude')
plt.subplot(3, 2, 2)
plt.plot(t,sum)
plt.title ('Time Domain Signal')
plt.xlabel ('Time')
#plt.ylabel ('Amplitude')

"Generating two random frequencies & using them to create noise"
f1=np.random.randint(0,512,1)
f2=np.random.randint(0,512,1)
noise=(np.sin(2*f1*pi*t))+(np.sin(2*f2*pi*t))

"Adding Noise to the Song"
songxnoise=noise+sum
songxnoise_f=fft(songxnoise)
songxnoise_f = 2/N * np.abs(songxnoise_f [0:np.int(N/2)])

"Plotting song with noise in time domain and frequency domain"
plt.subplot(3,2,3)
plt.plot(f,songxnoise_f)
#plt.title('Frequency domain Signal') 
#plt.xlabel('Frequency in Hz') 
plt.ylabel('Amplitude')
plt.subplot(3,2,4)
plt.plot(t,songxnoise)
#plt.title ('Time Domain Signal')
#plt.xlabel ('Time')
#plt.ylabel ('Amplitude')

"searching for the two peaks"
index= []
max= round(max(x_f))
for i in range(len(songxnoise_f)):
    if round(songxnoise_f[i])>max:
        index.append(i)
f11= round(f[index[0]])
f22= round(f[index[1]])

"Filtering the song"
filteredsong= songxnoise - ((np.sin(2*f11*pi*t))+(np.sin(2*f22*pi*t)))
filteredsong_f=fft(filteredsong)
filteredsong_f = 2/N * np.abs(filteredsong_f [0:np.int(N/2)])
"Plotting filtered song in time and frequency domains"
plt.subplot(3,2,5)
plt.plot(f,filteredsong_f)
plt.title ('filtered song')
plt.ylabel('Amplitude')
plt.subplot(3, 2,6)
plt.plot(t, filteredsong)
plt.title ('filtered song')
plt.xlabel ('Time')

sd.play(filteredsong,3.94*1024)


