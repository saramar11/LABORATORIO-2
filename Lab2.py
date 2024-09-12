# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:43:50 2024

Autoras:
    Garcia Trujillo Mariana 
    Pinzon Rodriguez Sara Mariana

Laboratorio 2: fiesta de coctel
    
"""
from scipy.io import wavfile
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA
from scipy.io.wavfile import write
from scipy.signal import butter, filtfilt
print(" " )
print("MICROFONO 1")

#PASAR DE MP4 A .WAV
from moviepy.editor import AudioFileClip

AudioFileClip('S12c.mp4').write_audiofile('S12C.wav', codec='pcm_s16le')


#leer primer archivo de wav 
sample_rate_S1, data_S1 = wavfile.read('S12C.wav')

print(" " )
print("Info basica S1")
print(f"Frecuencia de muestreo S1: {sample_rate_S1} Hz")
print(f"Forma de los datos S1: {data_S1.shape}")

if len(data_S1.shape)>1:
    S1 = data_S1[:,0]+data_S1[:,1]
    print("S1 es monoooo")
else:
    print("S1 es estereoooo")
    
#PASAR RUIDO DE MP4 A .WAV
from moviepy.editor import AudioFileClip

AudioFileClip('R12c.mp4').write_audiofile('R12C.wav', codec='pcm_s16le')    

sample_rate_R1, data_R1 = wavfile.read('R12C.wav')


print(" " )
print("Info basica R1")
print(f"Frecuencia de muestreo R1: {sample_rate_R1} Hz") 
print(f"Forma de los datos R1: {data_R1.shape}")


if len(data_R1.shape)>1:
    R1 = data_R1[:,1] #+data_R1[:,1]
    print("R1 es monoooo")
else:
    print("R1 es estereoooo")
    
# Paso 3: Convertir amplitud a voltaje
max_amplitude = 2**15  # 32768 para 16 bits
voltajeS = S1 / max_amplitude
voltajer= R1 / max_amplitude


print(" " )
print("Calculo de SNR microfono 1")
potencia_S1 = np.mean(voltajeS ** 2)
potencia_S1_deci ="{:.4f}".format(potencia_S1)
print(f"Potencia S1: {potencia_S1_deci}")

potencia_R1 = np.mean(voltajer ** 2)
potencia_R1_deci ="{:.11f}".format(potencia_R1)
print(f"Potencia R1: {potencia_R1_deci}")

snr1 = 10*math.log10(potencia_S1/potencia_R1)
snr1_deci ="{:.4f}".format(snr1)
print(f"SNR mic 1: {snr1_deci} dB")


#vectores de tiempo
time_S1 = np.arange(len(S1))/float(sample_rate_S1)
time_R1 = np.arange(len(R1))/float(sample_rate_R1)


if len(S1) != len(R1):
    raise ValueError("Las señales deben tener el mismo tamaño")
    

#GRAFICA MICROFONO 1
plt.subplot(3,1,1)
plt.plot(time_S1, voltajeS)
plt.title('Onda de sonido1')
plt.xlabel('Tiempo (s)')
plt.ylabel('voltaje')

plt.subplot(3,1,2)
plt.plot(time_R1, voltajer)
plt.title('Onda de Ruido1')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje')
plt.tight_layout()
plt.show()



print(" " )
print("MICROFONO 2")


#PASAR DE MP4 A .WAV
from moviepy.editor import AudioFileClip

AudioFileClip('S22c.mp4').write_audiofile('S22C.wav', codec='pcm_s16le')

#leer primer archivo de wav 
sample_rate_S2, data_S2 = wavfile.read('S22C.wav')

print(" " )
print("Info basica S2")
print(f"Frecuencia de muestreo S2: {sample_rate_S2} Hz")
print(f"Forma de los datos S2: {data_S2.shape}")

if len(data_S2.shape)>1:
    S2 = data_S2[:,1] 
    print("S2 es monoooo")
else:
    print("S2 es estereoooo")
    
#PASAR RUIDO DE MP4 A .WAV
from moviepy.editor import AudioFileClip

AudioFileClip('R22c.mp4').write_audiofile('R22C.wav', codec='pcm_s16le')


sample_rate_R2, data_R2 = wavfile.read('R22C.wav')


print(" " )
print("Info basica R2")
print(f"Frecuencia de muestreo R2: {sample_rate_R2} Hz") 
print(f"Forma de los datos R2: {data_R2.shape}")


if len(data_R2.shape)>1:
    R2 = data_R2[:,1] #+data_R2[:,1]
    print("R2 es monoooo")
else:
    print("R2 es estereoooo")
    
    
# Paso 3: Convertir amplitud a voltaje
max_amplitude = 2**15  # 32768 para 16 bits
voltajeS2 = S2 / max_amplitude
voltajer2= R2 / max_amplitude 
    

print(" " )
print("Calculo de SNR microfono 2")
potencia_S2 = np.sum(voltajeS2 ** 2)/len(S2)
potencia_S2_deci ="{:.10f}".format(potencia_S2)
print(f"Potencia S2: {potencia_S2_deci}")

potencia_R2 = np.sum(voltajer2 ** 2)/len(R2)
potencia_R2_deci ="{:.10f}".format(potencia_R2)
print(f"Potencia R2: {potencia_R2_deci}")

snr2 = 10*math.log10(potencia_S2/potencia_R2)
snr2_deci ="{:.4f}".format(snr2)
print(f"SNR mic 2: {snr2_deci} dB")


#vectores de tiempo
time_S2 = np.arange(len(S2))/float(sample_rate_S2)
time_R2 = np.arange(len(R2))/float(sample_rate_R2)


if len(S2) != len(R2):
    raise ValueError("Las señales deben tener el mismo tamaño")

#GRAFICA MICROFONO 2
plt.subplot(3,1,1)
plt.plot(time_S2, voltajeS2)
plt.title('Onda de sonido 2')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje')

plt.subplot(3,1,2)
plt.plot(time_R2, voltajer2)
plt.title('Onda de Ruido 2')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje')
plt.tight_layout()
plt.show()


print(" " )
print("MICROFONO 3")

#PASAR DE MP4 A .WAV
from moviepy.editor import AudioFileClip

AudioFileClip('S32c.mp4').write_audiofile('S32C.wav', codec='pcm_s16le')

#leer primer archivo de wav 
sample_rate_S3, data_S3 = wavfile.read('S32C.wav')

print(" " )
print("Info basica S3")
print(f"Frecuencia de muestreo S3: {sample_rate_S3} Hz")
print(f"Forma de los datos S2: {data_S2.shape}")


if len(data_S3.shape)>1:
    S3 = data_S3[:,1]#+data_S3[:,1]
    print("S3 es monoooo")
else:
    print("S3 es estereoooo")
    
#PASAR RUIDO DE MP4 A .WAV
from moviepy.editor import AudioFileClip

AudioFileClip('R32c.mp4').write_audiofile('R32C.wav', codec='pcm_s16le')
    

sample_rate_R3, data_R3 = wavfile.read('R32C.wav')


print(" " )
print("Info basica R3")
print(f"Frecuencia de muestreo R3: {sample_rate_R3} Hz") 
print(f"Forma de los datos R3: {data_R3.shape}")


if len(data_R3.shape)>1:
    R3 = data_R3[:,1]#+data_R3[:,1]
    print("R3 es monoooo")
else:
    print("R3 es estereoooo")
    
# Paso 3: Convertir amplitud a voltaje
max_amplitude = 2**15  # 32768 para 16 bits
voltajeS3 = S3 / max_amplitude
voltajer3= R3 / max_amplitude

    

print(" " )
print("Calculo de SNR microfono 3")
potencia_S3 = np.sum(voltajeS3 ** 2)/len(S3)
potencia_S3_deci ="{:.4f}".format(potencia_S3)
print(f"Potencia S3: {potencia_S3_deci}")

potencia_R3 = np.sum(voltajer3 ** 2)/len(R3)
potencia_R3_deci ="{:.10f}".format(potencia_R3)
print(f"Potencia R3: {potencia_R3_deci}")

snr3 = 10*math.log10(potencia_S3/potencia_R3)
snr3_deci ="{:.10f}".format(snr3)
print(f"SNR mic 3: {snr3_deci} dB")


#vectores de tiempo
time_S3 = np.arange(len(S3))/float(sample_rate_S3)
time_R3 = np.arange(len(R3))/float(sample_rate_R3)


if len(S3) != len(R3):
    raise ValueError("Las señales deben tener el mismo tamaño")

#GRAFICA MICROFONO 3
plt.subplot(3,1,1)
plt.plot(time_S3, voltajeS3)
plt.title('Onda de sonido 3')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje')

plt.subplot(3,1,2)
plt.plot(time_R3, voltajer3)
plt.title('Onda de Ruido 3')
plt.xlabel('Tiempo (s)')
plt.ylabel('Volteje')
plt.tight_layout()
plt.show()

# Función para aplicar filtro pasa-bajo
def apply_lowpass_filter(signal, cutoff_freq, sample_rate, order=5):
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

# Leer archivos de audio mezclados
sample_rate_S1, mixed1 = wavfile.read('S12C.wav')
sample_rate_S2, mixed2 = wavfile.read('S22C.wav')
sample_rate_S3, mixed3 = wavfile.read('S32C.wav')

# Verificar si las señales son estéreos y convertir a mono si es necesario
def convert_to_mono(data):
    if len(data.shape) > 1:
        return data[:, 0]
    return data

mixed1 = convert_to_mono(mixed1)
mixed2 = convert_to_mono(mixed2)
mixed3 = convert_to_mono(mixed3)

# Aplicar filtro pasa-bajo
cutoff_frequency = 3000  # Frecuencia de corte en Hz
mixed1_filtered = apply_lowpass_filter(mixed1, cutoff_frequency, sample_rate_S1)
mixed2_filtered = apply_lowpass_filter(mixed2, cutoff_frequency, sample_rate_S2)
mixed3_filtered = apply_lowpass_filter(mixed3, cutoff_frequency, sample_rate_S3)

# Crear una matriz de señales observadas
X = np.c_[mixed1_filtered, mixed2_filtered, mixed3_filtered]

# Aplicar ICA para separar las fuentes
ica = FastICA(n_components=3, random_state=0)
S = ica.fit_transform(X)

# Normalizar las señales separadas
def normalize_signal(signal):
    max_val = np.max(np.abs(signal))
    return (signal / max_val * 32767).astype(np.int16)

write('fuente_1.wav', sample_rate_S1, normalize_signal(S[:, 0]))
write('fuente_2.wav', sample_rate_S2, normalize_signal(S[:, 1]))
write('fuente_3.wav', sample_rate_S3, normalize_signal(S[:, 2]))

print("Señales separadas guardadas como 'fuente_1.wav', 'fuente_2.wav' y 'fuente_3.wav'.")

# Graficar señales separadas en el dominio temporal
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(S[:, 0])
plt.title('Fuente 1 (Temporal)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')

plt.subplot(3, 1, 2)
plt.plot(S[:, 1])
plt.title('Fuente 2 (Temporal)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')

plt.subplot(3, 1, 3)
plt.plot(S[:, 2])
plt.title('Fuente 3 (Temporal)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()



print("Señales separadas guardadas como 'fuente_1.wav', 'fuente_2.wav' y 'fuente_3.wav'.")

# Normalizar las señales para que estén en el dominio del voltaje
def normalize_signal(signal):
    return signal / np.max(np.abs(signal))

# Función para graficar el espectro
def plot_spectrum(signal, sample_rate, title):
    n = len(signal)
    fft_values = np.fft.fft(signal)
    f = np.fft.fftfreq(n, 1/sample_rate)
    magnitudes = np.abs(fft_values) / n
    magnitudes[1:n//2] *= 2
    positive_frequencies = f[:n // 2]
    positive_magnitudes = magnitudes[:n // 2]
    
    plt.semilogx(positive_frequencies, positive_magnitudes)
    plt.title(title)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Voltaje')
    plt.grid(True)

# Graficar las señales separadas en el dominio espectral
plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
plot_spectrum(S[:, 0], sample_rate_S1, 'Fuente 1 (Espectral)')

plt.subplot(3, 1, 2)
plot_spectrum(S[:, 1], sample_rate_S2, 'Fuente 2 (Espectral)')

plt.subplot(3, 1, 3)
plot_spectrum(S[:, 2], sample_rate_S3, 'Fuente 3 (Espectral)')

plt.tight_layout()
plt.show()

# Graficar comparación de señales
# Asegúrate de que 'S1' esté definido si es la señal original que quieres comparar
# En este ejemplo, usamos 'mixed1' como la señal original para ilustrar

def plot_comparison(original, mixed, recovered, sample_rate):
    plt.figure(figsize=(12, 8))
    
    # Graficar señal original
    plt.subplot(3, 1, 1)
    plot_spectrum(normalize_signal(original), sample_rate, 'Señal Original')
    
    # Graficar mezcla
    plt.subplot(3, 1, 2)
    plot_spectrum(normalize_signal(mixed), sample_rate, 'Señal Mezclada')
    
    # Graficar señal recuperada
    plt.subplot(3, 1, 3)
    plot_spectrum(normalize_signal(recovered), sample_rate, 'Señal Recuperada')
    
    plt.tight_layout()
    plt.show()

# Comparar la primera fuente recuperada con la señal original
# Asumiendo que original_signal es la señal original a comparar
original_signal = normalize_signal(mixed1)  # Asegúrate de tener la señal original correcta
recovered_signal_1 = normalize_signal(S[:, 2])

plot_comparison(original_signal, mixed1, recovered_signal_1, sample_rate_S1)


print(" " )

"""CALCULO DEL NUEVO SNR"""
# Calcular la potencia de la señal recuperada
potencia_recuperada = np.sum(np.abs(recovered_signal_1 ** 2)) / len(recovered_signal_1)

potencia = np.sum(np.abs(voltajer ** 2)) / len(S1)

# Calcular el nuevo SNR
snr_recuperado = 10 * math.log10(potencia_recuperada / potencia)
snr_recuperado_deci = "{:.4f}".format(snr_recuperado)
print(f"SNR de la señal recuperada respecto al ruido original: {snr_recuperado_deci} dB")
print(" " )



"""CALCULO DE LAS CARACTERISTICAS ESTADISTICAS"""
# Función para calcular las estadísticas básicas
def calcular_estadisticas(signal, nombre):
    max_val = np.max(signal)
    min_val = np.min(signal)
    media_val = np.mean(signal)
    mediana_val = np.median(signal)
    
    print(f'Estadísticas de {nombre}:')
    print(f'Máximo: {max_val}')
    print(f'Mínimo: {min_val}')
    print(f'Media: {media_val}')
    print(f'Mediana: {mediana_val}')
    print('--------------------------')
    print(" " )

# Señales temporales
print("...... Estadísticas Temporales......")
calcular_estadisticas(S[:, 0], 'Fuente 1 (Temporal)')
calcular_estadisticas(S[:, 1], 'Fuente 2 (Temporal)')
calcular_estadisticas(S[:, 2], 'Fuente 3 (Temporal)')

# Función para calcular el espectro y sus estadísticas
def calcular_estadisticas_espectro(signal, sample_rate, nombre):
    # FFT de la señal
    fft_values = np.fft.fft(signal)
    
    # Calcular las frecuencias y magnitudes
    magnitudes = np.abs(fft_values) / len(signal)
    magnitudes[1:len(signal)//2] *= 2  # Corrección de doble contabilidad
    
    # Filtrar las frecuencias positivas
    positive_magnitudes = magnitudes[:len(signal) // 2]
    
    # Calcular estadísticas
    calcular_estadisticas(positive_magnitudes, nombre)
    print(" " )

# Señales espectrales
print("..... Estadísticas Espectrales....")
calcular_estadisticas_espectro(S[:, 0], sample_rate_S1, 'Fuente 1 (Espectral)')
calcular_estadisticas_espectro(S[:, 1], sample_rate_S2, 'Fuente 2 (Espectral)')
calcular_estadisticas_espectro(S[:, 2], sample_rate_S3, 'Fuente 3 (Espectral)')