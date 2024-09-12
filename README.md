# LABORATORIO-2

Para el siguiente laboratorio se instalaron tres micrófonos en distintas partes inicialmente de una sala insonorizada. En primera instancia se realizó una grabación simultánea entre los tres micrófonos del ruido ambiente de la sala, y posterior a ellos se grabó de la misma duración una recreación de fiesta de cóctel, en donde tres personas se encuentran hablando al mismo tiempo. Para este laboratorio se elaboró un código el cual permite filtrar una única voz dentro de las tres voces que se escuchan.

Sala insonorizada donde se realizaron las primeras grabaciones:

[![IMG-0699.jpg](https://i.postimg.cc/k43TM0vx/IMG-0699.jpg)](https://postimg.cc/gwsVNB5J)

Sin embargo, se tuvieron que realizar las grabaciones de voz por segunda vez debido a inconvenientes que se estaban presentando al momento del procesamiento de las señales. Esta vez, se realizó la grabación con tres dispositivos de la misma marca en una habitación de la casa tanto del ruido ambiente como de los sonidos con las voces de tres personas hablando simultáneamente.

### Grabación del sonido y ruido

Para esto se usaron tres dispositivos electrónicos como micrófonos (un iPad y dos iPhone) que tuvieran una frecuencia de muestreo igual, en este caso de 44.1 kHz. Se ubicaron en diferentes partes de la habitación, dichas ubicaciones son evidentes en las siguientes fotos.

Microfono 1:

[![Mic1.png](https://i.postimg.cc/L8dLfHDh/Mic1.png)](https://postimg.cc/rKJD22vL)

Microfono 2:

[![Mic2.png](https://i.postimg.cc/9FHGSdRJ/Mic2.png)](https://postimg.cc/JtKDHBQk)

Microfono 3:

[![Mic3.png](https://i.postimg.cc/kG3t0C4B/Mic3.png)](https://postimg.cc/KkfzTdt2)

Disposición de personas y micrófonos en la habitación:

[![mics2.png](https://i.postimg.cc/zvhsFm68/mics2.png)](https://postimg.cc/XBV1nPnz)

Como se puede evidenciar en la anterior figura, los micrófonos se encontraban distribuidos en la habitación al igual que cada persona.
Inicialmente, se realizó un grabación del ruido ambiente con una duración de un minuto donde ninguna de las presentes realizara ningun ruido de fondo, posteriormente se grabó el mismo minuto pero ahora con cada persona hablando hacia una dirección diferente a donde estaba ubicado el micrófono cercano a cada una, y con una distancia mínima hacia cada micrófono de un metro.

### Librerías
Las principales librerías que se utilizaron fueron las siguientes:

[![pipscikit.png](https://i.postimg.cc/XYsvtFHm/pipscikit.png)](https://postimg.cc/pmnxF9tJ)

De las cuales *scipy.io* es una librería de la cual se extrae el *wavfile* el cual permite convertir archivo MP4 a archivos *.wav* dentro del código. *Numpy*, es fundamental para trabajar con cálculos con arreglos y matrices, mediante funciones tanto matemáticas las cuales permiten manejar una gran cantidad de datos. *math*, contiene funciones básicas aritméticas para realizar cálculos dentro del código. Y  *matplotlib.pyplot*, para realizar gráficas.

Por otro lado, para que este código funcione, hay que considerar varios paquetes de Python que deben ser instalados para usar las librerías correspondientes.
En primer lugar esta:
[![scijitcodigo.png](https://i.postimg.cc/rpbwwTL9/scijitcodigo.png)](https://postimg.cc/PLWjSBJL)
La cual permitió que para este laboratorio se tuvieran las funciones correspondientes para realizar la separación de audio mediante ICA, y todo los aspectos requeridos para realizar una transformación rápida de Fourier. Para que pudiera funcionar, es necesario instalar el siguiente paquete en la ventana de comandos de la siguiente forma:
[![pipscikit.png](https://i.postimg.cc/XYsvtFHm/pipscikit.png)](https://postimg.cc/pmnxF9tJ)

[![scipywrtircodi.png](https://i.postimg.cc/25j0Spx3/scipywrtircodi.png)](https://postimg.cc/bZMxmBWj)
Esta funciona para guardar archivos tipo *.wav* en la carpeta del dispositivo en donde se encuentra el código. Para esta librería es necesario haber instalado el paquete el la ventana de comandos mediante la siguiente línea.
[![scipypip.png](https://i.postimg.cc/RFsQFNZD/scipypip.png)](https://postimg.cc/zbhR2DWC)

Para trabajar con archivos de audio en Python es de vital importancia tener instalado el siguiente paquete:
[![simpleaudiopip.png](https://i.postimg.cc/W3WCvpL2/simpleaudiopip.png)](https://postimg.cc/Q970g3dP)
Por otro lado, está la instalación del siguiente paquete el cual permite manipular audios en formatos compatibles con el dispositivo.

[![pipmoviepy.png](https://i.postimg.cc/25vnY2s3/pipmoviepy.png)](https://postimg.cc/p9WmYYXt)

Por último, en lo que son las librerías se utilizó:

[![signal.png](https://i.postimg.cc/Df5L7WMQ/signal.png)](https://postimg.cc/pyhpZdxy)

La cual se utilizó para implementar filtros digitales dentro del código para el procesamiento de la señal. Butter para filtros butterworth, y filtfilt para que la señal que es filtrada contenga el mínimo desfase. 


### Formato de audio

Teniendo en cuenta que estos audios fueron grabados mediante aparatos electrónicos de la misma marca, se utilizó la aplicación de “Notas de Voz” disponible para cada usuario con sistema operativo iOs el cual guardaba los audios en formato MP4. Adicionalmente, se debe de considerar para el procesamiento de las señales que se verán posteriormente es de gran importancia que los audios sean simultáneos al mismo tiempo. Debido a esta condición, se editaron estos audios con la aplicación iMovie con el fin de ajustar los audios para que fueran simultáneos con un tiempo de captura de 30 segundos exactos de lo que se grabó con los micrófonos.

Se usaron estos nuevos archivos de sonido MP4 con el mismo valor de tiempo y se ingresaron al código con el fin de convertirlos al formato *.wav*. Anteriormente se estaban convirtiendo estos archivos mediante sitios web, donde se probaron múltiple con el fin de identificar si era influyente esta conversión en los resultados obtenidos. Finalmente, se optó por convertirlos dentro del mismo código de python mediante el uso de la librería  correspondiente, mencionada anteriormente.

Para verificar estos datos dentro del código se realizó una serie de líneas de código las cuales extraían la información correspondiente de cada audio utilizado. 

[![infos1.png](https://i.postimg.cc/GpBgNqWH/infos1.png)](https://postimg.cc/DWTc4dyT) 

Obteniendo así la siguiente información correspondiente al audio captado por el primer micrófono:

[![infobasicas1.png](https://i.postimg.cc/KjVbMJgL/infobasicas1.png)](https://postimg.cc/bSQ4X0gN)

A partir de esto se puede observar que en primera instancia la frecuencia de muestreo de este audio es de 44100 Hz así como se había mencionado anteriormente. También es evidente que los datos de este audio están almacenados en una matriz bidimensional de dos columnas con un total de 1324323 de datos, el hecho de que sea bidimensional implica que este archivo es estéreo, es decir que utiliza dos canales de sonido para crear una sensación de espacialidad en el audio. Sin embargo, para este procesamiento es necesario utilizar únicamente un solo canal, es decir volverlo un audio mono. Para esta finalidad se utilizaron las siguientes líneas de código, así mismo, por medio de mensajes mostrados en la ventana se puede evidenciar si se convirtió de estéreo a mono satisfactoriamente.

Esto que se mostró únicamente con el archivo del sonido 1, se realizó también con los demás archivos tanto de sonido como de ruido de la misma manera con la única diferencia de que se debía de tener en cuenta el nombre para cada uno de ellos. 

### Gráficas de Ruido y Sonido de los micrófonos

Para efectos de practicidad, se estará postulando el ejemplo con el primer sonido y ruido únicamente ya que con los otros sería el mismo procedimiento con la diferencia del archivo con el que se está trabajando. 

Una vez teniendo los audios en el formato *.wav* es necesario leer este archivo dentro del código de Python, por lo que realiza la siguiente línea de código:

[![sample.png](https://i.postimg.cc/L6j1FBxC/sample.png)](https://postimg.cc/rKFmSWXx)

El *wavfile.read(‘S12C.wav’)* Se encarga de tomar el archivo que contiene ese nombre y lo lee para devolver dos valores, los cuales corresponden a la tasa de muestreo y los datos que el audio contiene.

El *sample_rate* hace referencia a lo que se mencionaba anteriormente que es la frecuencia de muestreo la cual es definida por los dispositivos utilizados, para el caso de este laboratorio los dispositivos utilizados cuentan con una frecuencia de muestreo de 48kHz. Finalmente, el data es un arreglo (en este caso bidimensional ya que es estéreo comprobado por la función print dentro del código) en donde se encuentran las amplitudes de la señal de audio para cada muestra.

Así como se mencionó en el postulado de *Formato de audio* este archivo es estéreo ya que el *data* esta en dos dimensiones, es necesario usar únicamente una de sus dos columnas para el tratamiento de este audio, este cambio de estereo a mono se postuló anteriormente. 

*Para el sonido S1*

[![1wav.png](https://i.postimg.cc/s2jtFwDz/1wav.png)](https://postimg.cc/87YyMd6X)

[![s1.png](https://i.postimg.cc/76cwLMLv/s1.png)](https://postimg.cc/cgQV93YT)

Se procede a realizar la conversión del archivo del ruido correspondiente al micrófono 1 el cual al igual que el sonido pasa de MP4 a .wav junto con la selección de una sola columna de audio para pasar de estéreo a mono. Asimismo, con esa línea de osigo se asegura que el archivo nuevo .wav del sonido se guarde igualmente en la carpeta donde se encuentra el proyecto.

*Para el ruido R1*

 Se realiza el mismo procedimiento con el ruido y su respectivo archivo.

 [![ruidowv.png](https://i.postimg.cc/4N07MSfC/ruidowv.png)](https://postimg.cc/XpwYBxBx)

 [![lenR1.png](https://i.postimg.cc/76qf0vVz/lenR1.png)](https://postimg.cc/TyHdv4B2)

 Es importante tener en cuenta que al trabajar un archivo .wav la unidades que éste contiene son unidades adimensionales por lo tanto, es necesario realizar un vector de tiempo con el objetivo de asociar esos valores a una unidad física por cada una de las muestras durante un intervalo de tiempo real que corresponde al eje x  logrando el análisis de la señal a lo largo de un periodo específico identificando los momentos exactos en los que la señal sufre o presenta cambios.

*Vector del tiempo para el sonido 1 (TS1)*                            	

[![TS1.png](https://i.postimg.cc/qqwf3sJM/TS1.png)](https://postimg.cc/GT4S0sTZ)
 
*Vector del tiempo para el Ruido 1 (TR1)*

[![TR1.png](https://i.postimg.cc/ZYcXjLmJ/TR1.png)](https://postimg.cc/G94MmG9f)

Para el eje y se procede a realizar una normalización con el fin de convertir la amplitud a valores de voltaje con el fin de realizar las operaciones correspondientes al cálculo del SNR para que este tenga una unidad definida y de esta forma tener claro qué unidades se está trabajando con el fin de evitar errores durante el cálculo. Para esto te tuvo en cuenta que los archivos .wav emplean formato PCM de 16 bits por lo cual el rango de la máxima amplitud varía desde -32768 a 32767, con esto en mente se empleó la normalización de voltaje de -1V a 1V.

[![ampli.png](https://i.postimg.cc/qRtM8kKz/ampli.png)](https://postimg.cc/qhTTrHjT)

Una vez teniendo estos dos componentes, es posible graficar a estas señales usando la librería **matplotlib**. En este caso se realizó dos subplot para que el ruido y el sonido  tuvieran el mismo tamaño de la señal ya que en caso de no ser así se mostrará un error el cual tendrá el resultado de la diferencia de las señales.

[![lenvalueerror.png](https://i.postimg.cc/7ZskXFw7/lenvalueerror.png)](https://postimg.cc/CRqXx6ZL)

Seguido a esto se busca que el primer micrófono se encontrará en una misma página presentando así su sonido y ruido correspondientes. Para esto, se realizó el siguiente código:

[![plots1.png](https://i.postimg.cc/qRTcZMsZ/plots1.png)](https://postimg.cc/1gvN8SYp)

Obteniendo así la siguiente figura:

[![Figure-1of.png](https://i.postimg.cc/9FgS7dD2/Figure-1of.png)](https://postimg.cc/gnRN96yt)

Con esto se observa que la gráfica correspondiente al sonido 1 y ruido 1 presentan valores en milivoltios dentro de la escala normalizada.

**Variabilidad:** La señal del sonido muestra una variabilidad considerable a lo largo del tiempo, lo que es típico en señales de audio donde diferentes sonidos o voces pueden estar presentes. La amplitud no es constante, lo que indica dinámicas en la fuente de sonido.

**Tiempo:** Al igual que la onda de sonido, esta gráfica también se extiende a lo largo de 30 segundos, mostrando niveles de ruido consistentes aparte del pico mencionado.

**Comparación de amplitudes:** La onda de sonido tiene una amplitud diez veces mayor que la onda de ruido en la mayoría de los puntos, lo que es favorable para la claridad del sonido.


### Calculo de SNR

Para esto, se define al SNR (relación señal-ruido) como una medida la cual permite calcular y determinar en una señal si hay más ruido que información de la señal o viceversa, mediante la siguiente fórmula.  

 [![SNR.png](https://i.postimg.cc/BZwNcFYm/SNR.png)](https://postimg.cc/bdkQqZjn)

Y para calcular la potencia de cada señal, se realizaba mediante: 

[![potencia.png](https://i.postimg.cc/xjgWzgbh/potencia.png)](https://postimg.cc/LhYCdtD3)

Donde: 

P = Potencia  

n = es la longitud de la señal adquirida (la longitud del ruido debe ser igual a la de la señal original).     

A partir del resultado de SNR obtenido se determina que, si es un valor positivo, hay más información de la señal que ruido. Mientras que, si es un valor negativo, indica que hay más ruido en la señal contaminada que información importante. 

[![snrmayoa.png](https://i.postimg.cc/v80Gs5b7/snrmayoa.png)](https://postimg.cc/YjL5NG4j)


Teniendo en cuenta las fórmulas presentadas anteriormente se implementan dentro del código con el fin de obtener el SNR entre la señal que contiene las voces su ruido balnco el cual fue grabado mediante el mismos dispositivo  y ubicado en la misma posición con el fin de lograra una mayor exactitud en el análisis del audio 

#### Potencia y señal del ruido:

##### Microfono 1 

[![potysnrrys.png](https://i.postimg.cc/bJJ2RkPz/potysnrrys.png)](https://postimg.cc/sBkXjB18)

Calculo del SNR:

[![snrmic1.png](https://i.postimg.cc/qMw55dVj/snrmic1.png)](https://postimg.cc/6y7c8gQv)	

Mediante este código se obtuvieron diferentes potencias de la señal y ruido para cada uno de los micrófonos con su correspondiente SN aplicado para cada uno de los micrófonos:
Calculo de SNR microfono 1

Potencia S1: 0.0019

Potencia R1: 0.00000016793

SNR mic 1: 40.5714 dB

Del micrófono 1 se puede determinar que hay más información de la señal que el ruido en ella debido a que su SNR es positivo y mayor a 10 dB indicando una buena calidad de audio.

##### Resultados para el micrófono 2: 

[![Figure-2of.png](https://i.postimg.cc/W3sSKzdS/Figure-2of.png)](https://postimg.cc/NyP12g7r)

**Relación señal-ruido (SNR) :**1 a partir de las diferencias de amplitud, la señal (sonido) es mucho más fuerte que el ruido, lo que implica una relación señal-ruido (SNR) alta. Una SNR alto.

**Diferencia de amplitud :** La onda sonora tiene variaciones de amplitud mucho mayores en comparación con el ruido, lo que indica que el sonido tiene más energía o es más dominante en la señal general. Es probable que el ruido sea de fondo con menor intensidad.

**Tiempo:** Al igual que la onda de sonido, esta gráfica también se extiende a lo largo de 30 segundos, mostrando niveles de ruido consistentes aparte del pico mencionado.

##### Calculo de SNR microfono 2
Potencia S2: 0.0004024857
Potencia R2: 0.0000011568
SNR mic 2: 25.4149 dB
En este caso el SNR del micrófono 2 también se encuentra sobre los 10dB esto se podría ser debido a la posición del micrófono junto con la de las voces ya que este se encontraba alejado de los participantes del audio haciendo que la potencia del sonido sea un poco mas baja 

##### Resultados del micrófono 3:

[![Figure-3of.png](https://i.postimg.cc/bv99QPmn/Figure-3of.png)](https://postimg.cc/R3qtBk5C)

**Comparación de amplitudes:** La onda de sonido tiene una amplitud diez veces mayor que la onda de ruido en la mayoría de los puntos, lo que es favorable para la claridad del sonido.

**Eventos notables:** Hay un pico evidente alrededor de los 15 segundos, donde la amplitud del ruido aumenta bruscamente. Este pico puede ser un evento en donde se presento un ruido o sonido mucho más fuerte que el que se presentaba durante el tiempo de grabación.

**Tiempo:** Al igual que la onda de sonido, esta gráfica también se extiende a lo largo de 30 segundos, mostrando niveles de ruido consistentes aparte del pico mencionado.

##### Calculo de SNR microfono 3:

Potencia S3: 0.0006

Potencia R3: 0.0000004179

SNR mic 3: 31.3684748231 dB

Al igual que el caso anterior el SNR de la fuente 3 es superior a los 10 dB, por lo tanto se considera como un valor aceptable en donde hay más información que ruido al comparar las grabaciones de las voces con las del ruido ambiente tomado.

### Separación por ICA:

El **ICA:**  (Independent Component Analysis) se usa ICA para separar las señales mezcladas en componentes independientes, para esto se inicia con la lectura de las señales que se desean separar implementando los tres micrófonos los cuales contienen partes de la señal que se desean recuperar teniendolas en cuenta como señales mezcladas (*Mixed*) para cada uno de los micrófonos.

Para la correcta separación por ICA se decidió aplicar un filtro pasabajos con el fin de eliminar lasa señales con frecuencias muy altas ya que estas distorsionan de gran manera el resultado del audio final haciendo que este saliera con demasiada distorsión con esto en mente se procedió a la implementación del filtro eliminando las frecuencias no deseadas para la posterior separación de audio por ICA. 

[![Filtro.png](https://i.postimg.cc/KYTY17Dp/Filtro.png)](https://postimg.cc/CZF0tqtb)
 En donde:
**signal:** La señal de audio que quieres filtrar.
**cutoff_freq:** La frecuencia de corte del filtro (en Hz).
**order:** Es el orden del filtro. Cuanto mayor sea el orden, más pronunciada será la pendiente de corte del filtro.
Seguido a esto se realiza el cálculo de la frecuencia de muestreo por Nyquist para que las frecuencias por encima de la frecuencia de Nyquist se reflejarán en el espectro.

[![nyquist.png](https://i.postimg.cc/m2r2YWSH/nyquist.png)](https://postimg.cc/Jt9L8gvr)

Se realiza la normalización de la frecuencia con el fin de que la frecuencia de corte sea independiente de la frecuencia de muestreo de la señal.

Se implementa el filtro Butterworth mediante la función butter y se utiliza un filtro pasa bajos. Con esto se puede proceder al filtrado de la señal y su correspondiente retorno el cual será la señal señal filtrada con la que se trabajará dentro del ICA.

[![butter.png](https://i.postimg.cc/cLnWhxtr/butter.png)](https://postimg.cc/4YsjNT5g)

[![audiomezclado.png](https://i.postimg.cc/8ccQ6NVk/audiomezclado.png)](https://postimg.cc/hzk5FFjN)

La función **wavfile.read()** carga la señal de audio y su frecuencia de muestreo.

**sample_rate_S1, sample_rate_S2, sample_rate_S3:** Son las frecuencia de muestreo en Hz.

**mixed1, mixed2, mixed3:** Señales de audio en forma de arrays.

**Conversión a mono:** Verifica si la señal es estéreo (si tiene dos canales), y si es así, selecciona uno de los canales (el canal izquierdo en este caso) para convertir la señal a mono. El ICA funciona mejor con señales en mono, por lo que si los archivos de audio son estéreo, es necesario convertirlos.

[![tomono.png](https://i.postimg.cc/RhksZBSD/tomono.png)](https://postimg.cc/zHkSx4RC)

Se aplica el filtro pasa-bajo a cada una de las señales con una frecuencia de corte de 3000 Hz. Esto elimina frecuencias superiores a 3000 Hz, lo que puede ayudar a eliminar ruido de alta frecuencia o información no deseada antes de aplicar ICA.

[![LP.png](https://i.postimg.cc/2jLfrjTT/LP.png)](https://postimg.cc/DmhNcT9b)

Se crea una matriz de observaciones: Matriz** X **en la que cada columna es una señal filtrada **(mixed1_filtered, mixed2_filtered, mixed3_filtered)**.
Ya que el ICA requiere una matriz de señales observadas donde cada columna representa una grabación (o mezcla). Esta matriz se pasa luego al algoritmo ICA.

#### Implementación de ICA para la separación de fuentes

[![ICA.png](https://i.postimg.cc/gJq8ZbH7/ICA.png)](https://postimg.cc/dk3LbXXR)

Utiliza la función ** FastICA** para separar las mezclas en sus componentes independientes.

- **n_components=3:** Se indica que queremos 3 componentes independientes, ya que tenemos 3 señales de entrada.

- **random_state=0:** Para asegurar la reproducibilidad de los resultados.
Como resultado **S** Es una matriz con las señales separadas en sus columnas.

#### Normalización de las señales separadas

[![normi.png](https://i.postimg.cc/90QRwRM4/normi.png)](https://postimg.cc/xJBTWdLY)

Se escala la señal para que su valor máximo absoluto sea 32767, lo que es típico en archivos WAV de 16 bits. Se convierten los valores a enteros, los valores normalizados a enteros de 16 bits **(np.int16)**, que es el formato utilizado por archivos WAV.

**Finalmente**, las señales separadas se normalizan y se guardan como archivos de audio WAV y se muestra el mensaje que confirma que las señales fueron correctamente guardadas.

[![writey.png](https://i.postimg.cc/Vvh6SKpT/writey.png)](https://postimg.cc/YL1kZzpf)

### Gráfica de las señales en el dominio espectral y temporal

Estas son el resultado del código utilizado anteriormente para la separación por ICA.Se generan las gráficas de las tres fuentes resultantes da la separación por ICA, estas al estar en un archivo .wav estas representadas en función del número de muestras en el eje ** x**  y amplitud en el eje **y** las cuales como se mencionó anteriormente son unidades adimensionales.

Cada **plt.subplot(3, 1, n)** crea un gráfico para una de las fuentes separadas (n = 1, 2, 3). Y **plt.tight_layout()** asegura que los gráficos no se superponen y están bien organizados. Esto con el fin de visualizar el comportamiento de la señal en el dominio temporal.

Nuevamente es necesario aplicar la normalización correspondiente a los datos guardados en el archivo.wav con el fin de realizar el análisis temporal de los sonidos en función del tiempo y del voltaje.

[![AenV.png](https://i.postimg.cc/hP65PVy5/AenV.png)](https://postimg.cc/ykhPL3zm)

Esta función convierte las amplitudes de las señales separadas (que están en formato numérico) a valores de voltaje. Se basa en la profundidad de bits del archivo de audio (en este caso, 16 bits). Para un archivo de audio de 16 bits, el valor máximo de amplitud es 32768.

Se genera el vector de tiempo mediante la función **generate_time_vector** para analizar la señal en función del tiempo, el vector de tiempo en función de la longitud de la señal y la frecuencia de muestreo (sample rate). El tiempo se calcula como la cantidad de muestras dividida por la frecuencia de muestreo, lo que nos da el tiempo total en segundos para cada muestra.


[![Vtemp.png](https://i.postimg.cc/k5dYWqdN/Vtemp.png)](https://postimg.cc/87tbS8cs)

Finalmente se obtiene la gráfica del análisis temporal de los sonidos mediante:

[![graftempo.png](https://i.postimg.cc/RCjYvcbb/graftempo.png)](https://postimg.cc/hh1sr7n9)

Para obtener las siguientes gráficas:

[![Figura-analisis-temporal.png](https://i.postimg.cc/tgTk3TMx/Figura-analisis-temporal.png)](https://postimg.cc/872LD1Dp)

**1. Fuente 1 (Voltaje vs Tiempo):**
- La señal es constante en su magnitud a lo largo del tiempo, aunque presenta algunas variaciones en las amplitudes de picos y valles.
- Los valores de voltaje varían entre -0.0002 V y 0.0002 V.

**2. Fuente 2 (Voltaje vs Tiempo):**
- Esta señal tiene un comportamiento más variable en comparación con la Fuente 1. Al principio, presenta mayores variaciones de amplitud y presenta mas ruido hasta el segundo 15, después de lo cual tiende a estabilizarse. 
- Los valores de voltaje están dentro de un rango similar, pero las variaciones al principio son más grandes, lo que podría indicar una señal más intensa o con más componentes de alta frecuencia en los primeros segundos.

**3. Fuente 3 (Voltaje vs Tiempo):**
- La señal de la Fuente 3 también muestra variaciones notables en amplitud, pero sus picos son más pequeños en comparación con las dos primeras fuentes.
- Hay varias oscilaciones que podrían estar asociadas con componentes de frecuencia más baja o con eventos que ocurren de forma más periódica pero menos intensa en términos de amplitud.

Al visualizar estas señales se procede a normalizarlas nuevamente las señales ubicadas en el .wav para convertir los valores adimensionales a magnitudes físicas que se puedan operar como lo es el voltaje para el eje **y** el tiempo en el eje **x** esto dentro del rango - 1 a 1   voltios.

[![normidevltaje.png](https://i.postimg.cc/C5Yf4rxQ/normidevltaje.png)](https://postimg.cc/jwg5xXNH)

Se utiliza la función para graficar los espectros para esto se requiere convertir las desde el dominio del tiempo a el dominio de la frecuencia haciendo uso de la transformada rápida de fourier (FFT) con el fin de una mejor interpretación dentro de las frecuencias (bajos, agudos entre otras) 

[![fxdeespectro.png](https://i.postimg.cc/kgVDWPy5/fxdeespectro.png)](https://postimg.cc/0zs8q3Fg)

En donde:

- **np.fft.fft(signal):** Calcula la transformada rápida de Fourier para obtener las componentes de frecuencia de la señal.

- **np.fft.fftfreq(n, 1/sample_rate):** Genera las frecuencias correspondientes a los valores de la FFT.

- **magnitudes[1:n//2] *= 2:** Dado que la FFT devuelve tanto las frecuencias positivas como las negativas, esta línea duplica las magnitudes de las frecuencias positivas (excepto el componente de frecuencia cero).

- **plt.semilogx(...):** Gráfica las magnitudes de las frecuencias en escala logarítmica para visualizar mejor el espectro de frecuencias.

Al analizar la señal en el dominio de la frecuencia se puede visualizar las diferentes frecuencias que se encuentran dentro de la señal separada.

#### Gráfica de la señal espectral

Se utiliza la función **plot_spectrum** para graficar las tres señales separadas en el dominio de la frecuencia.  Obteniendo:

[![figure-dominio-espectra-sepatadas.png](https://i.postimg.cc/wvxpchdk/figure-dominio-espectra-sepatadas.png)](https://postimg.cc/QBzwjKCB)

Gráfica el espectro de cada una de las tres fuentes separadas en frecuencias (espectro de magnitudes).Cada gráfico muestra cómo las frecuencias están distribuidas dentro de la señal en el eje x (frecuencia en Hz) y el eje y (magnitud o voltaje). De esta forma se observa cuales son las frecuencias que predominan en cada una de las señales separadas.

En donde se obtiene:

[![figure-expetral-separadas-frec.png](https://i.postimg.cc/SNYprSHH/figure-expetral-separadas-frec.png)](https://postimg.cc/Cz0tMgh4)

En donde:


**Fuente 1 (Espectral)**
- El espectro de esta señal tiene picos prominentes en la región de frecuencias entre 10¹ (10 Hz) y 10³ (1,000 Hz), con algunos picos más pequeños en torno a 10⁴ Hz (10,000 Hz).
- La mayor parte de la energía de la señal parece estar concentrada entre 100 y 1,000 Hz, lo que podría corresponder a componentes en donde el sonido fue mas fuerte dentro de estos rangos.
  
**Fuente 2 (Espectral)**
- En esta señal, se observa una concentración de energía alrededor de los mismos rangos, pero con un pico principal más marcado en el rango de 100 a 500 Hz.
- Tiene menos contenido en las frecuencias más altas en comparación con la Fuente 1, lo que sugiere que podría corresponder a una señal más simple o con menos armónicos presentes.

**Fuente 3 (Espectral)**
- El espectro de la Fuente 3 es algo similar al de la Fuente 1, con una alta densidad de energía entre 10¹ (10 Hz) y 10³ Hz (1,000 Hz).
- Se observan varios picos entre 100 Hz y 2,000 Hz, lo que sugiere que esta señal también tiene componentes de frecuencias medias.
- En general, parece más compleja que la Fuente 2, pero menos que la Fuente 1 en términos de distribución de picos.

#### Comparación entre las señales procesadas de un solo microfono (senal original mezclada y recuperada correspondientes al micrófono 3)

Se hace uso de la función **plot_comparison(original, mixed, recovered, sample_rate)** la cual compara visualmente el espectro de frecuencia de tres señales: la señal original, la señal mezclada y la señal recuperada.

Para cada señal (original, mezclada y recuperada), se normaliza utilizando **normalize_signal.**

Luego se grafica el espectro de cada una de estas señales utilizando la función **plot_spectrum.**

Se muestran las tres señales una debajo de la otra para una comparación visual directa entre la señal original con la señal mezclada y la señal recuperada utilizando ICA, para esto Se normaliza cada señal y luego se grafica su espectro de frecuencia.l Este análisis es útil para evaluar la efectividad del proceso de separación de señales (por ejemplo, usando técnicas como el ICA), demostrando que la mayor parte de la información original se ha mantenido en la señal recuperada, en donde:

1. Se convierte la amplitud a voltaje para las señales separadas y se grafica en función del tiempo.

2. Se normalizan las señales para graficar su espectro en función de la frecuencia.

3. Se comparan las señales originales, mezcladas y recuperadas tanto en el dominio temporal como en el espectral.

[![plot-comparison.png](https://i.postimg.cc/jqws8478/plot-comparison.png)](https://postimg.cc/rzTXsWgW)

Obteniendo finalmente:

[![Figure-comparacion-senals.png](https://i.postimg.cc/59CV59hT/Figure-comparacion-senals.png)](https://postimg.cc/XX4m4W7k)

**1. Señal Original**
- **Eje X (Frecuencia en Hz):** La señal original presenta varios picos prominentes en el rango de frecuencias de 10² (100 Hz) a 10³ Hz (1,000 Hz), con algunos picos más débiles más allá de 10³ Hz.
- **Eje Y (Voltaje en V):** La amplitud máxima de la señal está en el rango de 0.006 V, con la mayor parte de la energía distribuida en el rango entre 100 Hz y 1,000 Hz.
- **Análisis:** La señal original tiene un comportamiento complejo con múltiples componentes frecuenciales en el rango de 100 Hz a 1,000 Hz. Estos picos sugieren que hay varias frecuencias importantes, lo que indica una señal con varias componentes o armónicos.
  
**2. Señal Mezclada**
- **Eje X (Frecuencia en Hz):** La señal mezclada tiene una estructura espectral similar a la señal original, pero con una mayor amplitud en las bajas frecuencias (cercanas a 100 Hz).

- **Eje Y (Voltaje en V):** La señal mezclada también alcanza picos de alrededor de 0.006 V. Sin embargo, la energía se ha distribuido de manera ligeramente distinta, con las frecuencias más bajas teniendo mayor prominencia.
- **Análisis:** El hecho de que la señal mezclada mantiene muchas características de la señal original pero con mayor presencia en las frecuencias bajas podría ser indicativo de cómo varias señales han sido combinadas o sumadas. Esto sugiere la interferencia de otras señales de baja frecuencia.
  
**3. Señal Recuperada**
- **Eje X (Frecuencia en Hz):** La señal recuperada muestra una estructura espectral que se asemeja a la señal original, con picos principales alrededor de los mismos rangos de frecuencia (100 Hz a 1,000 Hz). Sin embargo, hay algunas diferencias en la distribución exacta de la energía.
- **Eje Y (Voltaje en V):** La señal recuperada presenta picos de hasta 0.006 V, al igual que la señal original. Sin embargo, hay una ligera caída en las amplitudes en las frecuencias más altas.
- **Análisis:** La señal recuperada parece haber capturado la mayoría de las características clave de la señal original, ya que este micrófono se encontraba en medio de la habitación. Esto indica que el proceso de recuperación ha sido eficaz en retener la mayor parte de la información original, aunque podría haber alguna pérdida o distorsión en las frecuencias más altas.

**Comparación General:**
- Las tres señales muestran similitudes significativas en cuanto a los picos de frecuencia más importantes, especialmente en el rango de 100 Hz a 1,000 Hz, lo que indica que las características fundamentales de la señal original han sido preservadas tanto en la mezcla como en la recuperación.
- La señal mezclada tiene una mayor presencia de bajas frecuencias, lo que es común en las señales mezcladas donde múltiples fuentes pueden estar interfiriendo.
- La señal recuperada ha logrado retener la mayor parte de la estructura de la señal original, lo que indica que el proceso de separación y recuperación ha sido exitoso, aunque podría haber cierta pérdida o alteración de los componentes más sutiles en las frecuencias altas.

#### Cálculos de estadísticas (características de las señales temporales y espectrales)

La función **calcular_estadisticas**calcula y muestra estadísticas básicas sobre una señal Para este caso se decidió analizar los puntos máximos, mínimos la media y la mediana de cada una de las señales que se encuentran en el análisis temporal y espectral con el fin de entender el comportamiento de las misma en función de la frecuencia y el tiempo.

[![calculos-estadisticos-codigo.png](https://i.postimg.cc/PJ4KbwT1/calculos-estadisticos-codigo.png)](https://postimg.cc/N2K1BLy0)

Dando como resultados:

##### Estadísticas Temporales

1. **Fuente 1 (Temporal):**
- **Máximo:** 6.5467
- **Mínimo:** -7.1606
- **Media:** 1.922e-17 (prácticamente cero)
- **Mediana:** 0.0135

La media cercana a cero indica que la señal está centrada alrededor del cero. La mediana es muy baja, lo que indica que la mayoría de los valores de la señal están cerca de cero, aunque hay algunas oscilaciones notables (máximo y mínimo bastante altos).

2. **Fuente 2 (Temporal):**
- **Máximo:** 6.2538
- **Mínimo:** -6.1142
- **Media:** 1.3002e-17 (cero)
- **Mediana:** 2.3084e-05 (cero)

Similar a la Fuente 1, la media y la mediana son muy cercanas a cero, indicando que la señal está equilibrada alrededor del cero. Sin embargo, la mediana es más cercana a cero que en la Fuente 1, lo que sugiere menos variabilidad en torno a cero.

3. **Fuente 3 (Temporal):**
- **Máximo:** 6.9160
- **Mínimo:** -7.0647
- **Media:** 4.9482e-18 (prácticamente cero)
- **Mediana:** 0.0038

Al igual que las otras dos fuentes, la media es muy cercana a cero. La mediana es un poco mayor que en las otras fuentes, pero aún así, bastante baja.

**Conclusiones Temporales:**

- **Amplitud:** Las señales tienen una amplitud considerable, con valores máximos y mínimos que sugieren variabilidad significativa. Las diferencias entre los máximos y mínimos en cada señal pueden indicar la intensidad del audio.
- **Centro de la señal:** La media cercana a cero en todas las señales indica que la señal está centrada alrededor de cero.
- **Mediana:** La mediana baja en todas las señales sugiere que la mayoría de los datos están cerca del centro. Las pequeñas diferencias en la mediana pueden indicar ligeras diferencias en la distribución de la señal entre las diferentes fuentes.

#####Estadísticas Espectrales:

1. **Fuente 1 (Espectral):**
- **Máximo:** 0.0431
- **Mínimo:** 1.8779e-17 (cero)
- **Media:** 0.0004
- **Mediana:** 8.0762e-11 (cero)
  
La media de las magnitudes espectrales es bastante baja, indicando que la mayor parte de la energía de la señal está concentrada en frecuencias de baja amplitud. El máximo en el espectro sugiere la presencia de una frecuencia dominante en la señal.

- **Fuente 2 (Espectral):**
- **Máximo:** 0.0747
- **Mínimo:** 1.3145e-17 (prácticamente cero)
- **Media:** 0.0004
- **Mediana:** 7.5222e-11 (prácticamente cero)
  
Similar a la Fuente 1, la media es baja y el máximo indica una frecuencia dominante en el espectro. La diferencia principal es que el máximo es mayor, lo que sugiere una mayor amplitud en algunas frecuencias comparado con la Fuente 1.

3. **Fuente 3 (Espectral):**
- **Máximo:** 0.0507
- **Mínimo:** 4.3781e-18 (prácticamente cero)
- **Media:** 0.0004
- **Mediana:** 8.6092e-11 (prácticamente cero)

Los resultados son similares a los de las otras fuentes espectrales. La media es baja y el máximo es intermedio entre las otras dos fuentes, indicando variabilidad en la amplitud de las frecuencias.

**Conclusiones Espectrales:**
- **Amplitud espectral:** Las señales muestran una magnitud máxima en el espectro que varía entre 0.0431 y 0.0747. Esto indica la presencia de ciertas frecuencias dominantes que tienen una amplitud significativamente mayor en comparación con la mayoría de las otras frecuencias.
- **Energía promedio y mediana:** La media y mediana bajas sugieren que la energía de la señal está distribuida en frecuencias con bajas magnitudes en general. La mediana extremadamente baja indica que la mayoría de las frecuencias tienen magnitudes muy bajas, lo que es típico si solo unas pocas frecuencias dominan el espectro.
- **Comparación entre fuentes:** Las diferencias en los valores máximos espectrales sugieren que las fuentes tienen diferentes niveles de intensidad en sus componentes de frecuencia.

### SNR de la senal recuperada

Una vez ya se realizó el procedimiento de la separación de la voz mediante la mezcla de los tres audios usando ICA, se utilizó el audio de la fuente en donde se escucha con mayor nitidez una única voz entre las tres personas presentes en la habitación siendo esta *fuente 3* la cual según lo estipulado por el código es el correspondiente al micrófono 3, con el ruido captado desde el inicio con este micrófono *voltajer3*. Cabe resaltar que en esta señal recuperada la voz que se escucha con mayor nitidez corresponde a la persona que inicialmente se considera como **S1** en el esquemático presentado al inicio, lo cual significa que se encontraba al otro lado de la habitación.

Con esto en mente se vuelve a calcular la potencia de cada una de las señales, tanto de la recuperada con la voz de S1 en el micrófono 3 (fuente 3), como la del ruido.

** Línea de código para el cálculo de la potencia de la señal recuperada: **

[![potenreupf.png](https://i.postimg.cc/2SZsN0w6/potenreupf.png)](https://postimg.cc/DS7jqdRk)

**Resultado de la potencia de la señal recuperada** 

[![Potenf3.png](https://i.postimg.cc/hvN2CqN0/Potenf3.png)](https://postimg.cc/kRFN4LJV)

De igual forma, se realizó el mismo procedimiento con la señal del ruido del micrófono 3 que fue utilizado desde el principio del código.

[![potenr3odigo.png](https://i.postimg.cc/nzJjGSdQ/potenr3odigo.png)](https://postimg.cc/kVTgnsPn)

Resultado:

[![potenruido3.png](https://i.postimg.cc/X7Qf7Ws1/potenruido3.png)](https://postimg.cc/Tp5LCzMn)

Con estos valores de potencia fue posible finalmente calcular el SNR de esta señal recuperada en la fuente 3 con respecto al ruido ambiente de este micrófono mediante la ecuación postulada al inicio de este reporte, con la siguiente línea de código que también permite visualizar en valor obtenido en la ventana con cuatro decimales.

[![snrrecuperado.png](https://i.postimg.cc/N07fBs45/snrrecuperado.png)](https://postimg.cc/gwjPKP1W)

Resultado: 

[![valorsnr-recuperado.png](https://i.postimg.cc/T1ZXnF9z/valorsnr-recuperado.png)](https://postimg.cc/jnQ9b8Bc)


De este SNR obtenido se aprecia que se encuentra con un valor positivo que indica que hay más información que ruido en este audio, y es superior a 10 dB lo cual como se ha postulado a lo largo del reporte significa que es válida utilizarla. 

## Conclusiones generales del laboratorio 

- **Análisis Temporal:** Todas las señales están centradas alrededor de cero y tienen variabilidad significativa en términos de amplitud. Las señales tienen una pequeña mediana, indicando que la mayoría de los valores están cerca del centro.
- **Análisis Espectral:** La energía en el dominio de la frecuencia es baja en promedio, pero hay algunas frecuencias dominantes con altas magnitudes. Las diferencias en el máximo espectral entre las fuentes indican variaciones en la intensidad de la señal y en el dominio de la frecuencia.
- Finalmente gracias a los valores de SNR obtenidos se puede identificar que si es positivo indica que hay más información que ruido en la señal del audio que está siendo analiza también gracias a los audios que fueron obtenidos a partir de la señal recuperada, adicionalmente que si su valor se encuentra por encima de 10 dB se considera como un audio útil y válido para poder trabajar con el.
- El ICA es una herramienta que por medio de descomposición de componentes independientes, y la transformación rápida de fourier dentro él, es posible obtener una única voz entre una sala con múltiples personas hablando al mismo tiempo mediante el uso de varios micrófonos, para este caso 3 en total.
- Los diagramas espectrales identifican el comportamiento de las frecuencias en el audio mientras que el temporal es una gráfica el cual permite visualizar la forma de onda del sonido en torno a la amplitud que tuvo en unidades de voltaje en función del tiempo durante el cual estuvo grabando, es decir que tan fuerte fue el sonido.
- Gracias a la comparación que se realiza por medio de las señal original, mezclada y recuperada se demuestra que la información original se mantiene en su mayor parte en la señal recuperada obtenida después del ICA.
- Mediante el diagrama espectral de cada una de las fuentes por separado, se puede denotar que las frecuencias de las voces se encuentran en un intervalo similar en las tres fuentes en su frecuencia, y la amplitud representada en voltaje representa que tan agudo fue.


