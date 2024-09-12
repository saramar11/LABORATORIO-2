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

