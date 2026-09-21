Elena Sofía Luna Palacio - 201041

## Actividad 1: Publicador y subscritor de velocidad

En esta actividad creamos nuestro primer paquete de ROS2 con un publisher, un nodo que publicara mensajes de velocidad, y un subscriber, un nodo que esperara estos mensajes.

Los dos nodos creados fueron:

- velocity_publisher.py
- velocity_subscriber.py

El primer nodo publica mensajes de tipo Float32 a través de un tópico llamado "velocity" con una cola de tamaño 10.

El segundo nodo se susbcribe al tópico "velocity" y manda a llamar a la función "velocity_callback" siempre que reciba un mensaje i.e. el segundo nodo se mantiene escuchando el tópico de velocidad en espera de nuevos mensajes. 

Además, se añadieron entry_points en setup.py para poder ejecutar los programas de ambos nodos como parte del paquete de basics. También modificamos el package.xml con la información de nuestro nuevo paquete.

Los comandos utilizados para la ejecución fueron:
- colcon build: para crear ("build") nuestro nuevo paquete basics
- ros2 run basics velocity_publisher: para correr el nodo velocity_publisher, que publicará velocidades en el tópico "velocity".
- ros2 run basics velocity_subscriber: en una segunda terminal, escuchará las velocidades publicadas en el tópico "velocity" y las imprime en la terminal.

El úncio problema que tuvimos fue que la terminal no reconocía los comandos porque no sabía qué path seguir. Para solucionarlo añadimos source /opt/ros/jazzy/setup.bash y 
source /home/parallels/robotics_ws/install/setup.bash como comandos de source.

Link video: https://drive.google.com/file/d/1XQLXccRVZ-kMWbbudjkbdo5Yb84sMIXH/view?usp=sharing

## Actividad 2: Publicador y subscritor de velocidad Turtlesim

En esta actividad se modificaron los scripts de velocity_publisher.py y velocity_subscriber.py para adaptarlos a la simualación de Turtlesim y permitir que la tortuga se traslade (a través de mensajes con velocidad de traslación).

En este caso el nodo velocity_turtle_pub (twist_publisher) se encargó de publicar mensajes de tipo "Twist" en el tópico "/turtle1/cmd_vel" cambiando la velocidad lineal del eje x (i.e. linear.x). El nodo velocity_turtle_subscriber (twist_subscriber) se subscribió al tópico "/turtle1/cmd_vel", esperando mensajes de velocidad para desplegar en la terminal.

Se modificó la lógica del if-else original para que la velocidad aumentara de 0.0 a 1.2 (en incrementos de 0.1) y despúes detener a la tortuga. 

La creación de ambos nodos se verificó con el comando **ros2 node list**. También se verificó la existencia del tópico en uso "/turtle1/cmd_vel" con el comando **ros2 topic list**.

<img width="679" height="224" alt="image" src="https://github.com/user-attachments/assets/638b0029-8d7b-4ddf-a824-a19c2505a082" />


Para la ejecución de los nodos se corrió en una terminal la simulación de la tortuga con el comando **ros2 run turtlesim turtlesim_node**. En una segunda terminal se mando a llamar al nodo velocity_turtle_pub (twist_publisher) a través del comando r**os2 run basics velocity_turtle_pub** y en una tercera terminal se llamó al nodo velocity_turtle_subscriber (twist_subscriber) con **ros2 run basics velocity_turtle_subscriber**.

Además, con el comando **ros2 run rqt_graph rqt_graph** se generó un gráfico que muestra la interacción entre los nodos a través de los mensajes enviados en los tópicos.

<img width="2506" height="1608" alt="image" src="https://github.com/user-attachments/assets/82403ff7-b364-48cd-81fd-d2e1fc97d7f6" />

Observamos que el mensaje del publisher llega también al nodo turtlesim, lo que permite que se vea su movimiento en la interfaz.

En este caso no hubo problemas con la ejecución de la actividad.

Link video: https://drive.google.com/file/d/1fjcIPTSw56PD0bqnGVxEW6cvgy9sYlKF/view?usp=sharing

## Actividad 3.1: Ejemplo del LED

El objetivo de este ejercicio fue prender y apagar el led de la placa ESP32.

Primero, se comprobó el funcionamiento de los cables y la placa corriendo el código de LED_serial.ino dentro del IDE de Arduino. Este código primero define al pin 2 (LED) como un output y luego, a través de un loop infinito, lee el valor que encuentre dentro del buffer de la comunicación serial. Si es un 1, manda un "HIGH" al output i.e. 3.3V y, si es un 0, manda 0V o un "LOW". 

Una vez comprobado el funcionamiento de este código, se crearon dos nodos en ROS2. Primero, el nodo "led_blink", que se encarga de publicar mensajes de tipo Int32 a través del tópico "/led_command". Cada segundo este código aplica un XOR lógico al atributo de "estado" de la clase y lo publica como mensaje. Segundo, se creó el nodo "serial_bridge" el cual se suscribe a los mensajes del tópico "led_command" y abre un puerto de comunicación serial '/dev/ttyUSB0' con una velocidad de 115200 baudios. Cada que recibe un mensaje, llama a la función "led_callback", la cual manda el valor del mensaje recibido (0 o 1) al buffer de la comunicación serial utilizando "serial.write(b'{valor}\n')".

En setup.py se incluyeron los entrypoints para ambos nodos:
- 'led_blink = basics.led_blink:main'
- 'serial_bridge = basics.serial_bridge:main'

Además, para que se reconociera el puerto '/dev/ttyUSB0', se tuvieron que correr los comandos "ls /dev/ttyUSB*" y "sudo chmod 777 /dev/ttyUSB0".

<img width="1206" height="588" alt="image" src="https://github.com/user-attachments/assets/7fe716e7-55cc-4315-bea2-ad3044783fc0" />

Link video: https://drive.google.com/file/d/1jnQ6Hkx0JnRXBd5Oytrx7ZafQxCj-8HG/view?usp=sharing

## Actividad 3.2: Ejemplo con el potenciómetro

El objetivo de este ejercicio fue mostrar el voltaje de salida del potenciómetro a través del analog-digital-converter (ADC).

Primero, se cargó el programa de ADC_POT.ino en el IDE de Arduino. Este código primero define un puerto (en este caso POT 15), luego, en un loop infinito, lee el valor del voltaje que recibe de forma análoga a través del potenciómetro (que funciona como divisor del voltaje) y lo convierte a un valor numérico utilizando ADC. Como la placa ESP32 cuenta con 12 bits, el valor del voltaje se encontrará entre 0 y 4095 i.e de \$`2^0`\$ a (\$`2^{12}-1`\$).

Luego se crearon dos nodos: "analog_serial_pub" y "analog_subs". El primero se encarga de publicar mensajes de tipo Int32 en el tópico "/analog". Además, crea una conexión con un puerto ('/dev/ttyUSB0') de comunicación serial y cada 0.01 segundos llama a la función "read_serial" la cual lee lo que encuentre en el buffer (una línea, para cuando encuentra \n), lo convierte a texto y elimina espacios, lo guarda en una variable "linea" y envía el contenido de esta variable al topico "/analog". 

El nodo "analog_subs" crea una subscripción al mismo tópico y, siempre que reciba un mensaje, manda a llamar a la función "analog_callback". Esta extrae el dato del mensaje y lo imprime en la consola 'ADC = {valor}'. 

Link video: https://drive.google.com/file/d/1ldWNZiT1IJUy6tfld0qSlxnq1lR88lr2/view?usp=sharing

## Actividad 4: Joystick - Turtle Controller

En esta actividad se utilizó el joystick para poder controlar el movimiento de la tortuga de turtlesim (movimiento lineal x y angular z)

Primero se creó el archivo joystick.ino en el cual se definieron los puertos para la lectura de los valores x y y del ADC, lo cuales se encontraban en el rango 0 a 4095. Aquí también se pudo identificar el "centro" del joystick: 1850 en x y 1750 en y, es decir, los valores que aparecían cuando el joystick no estaba en movimiento. Tenían una variabilidad de aproximiadamente +-50, por lo que se consideró el valor de 100 para la zona muerte (para tener un pequeño "extra" en ambas direcciones).

Despúes, se creó el nodo joystick_publisher, el cual leía los valores de la comunicación serial y los mandaba a través del tópico "/joystick" como un arreglo de Int32. Se comprobó su funcionamiento con el comando "ros2 topic echo /joystick" para observar los mensajes enviados por el tópico. Posteriormente se creó el tópico turtle_controller, el cual se suscribe al tópico "/joystick" y procesa los valores de las coordenadas x y y. Las normaliza con el centro que se encontró en el IDE del arduino, considerando si están adelante o atrás del centro para obtener valores entre 1 y -1. Asismismo, este nodo publica en el tópico "/turtle1/cmd_vel" mensajes de tipo Twist, multiplicando el valor normalizado por la velocidad máxima y mandandolos como valores de linear.x y angular.z para poder obtener una velocidad proporcional. Se eligió como velocidad máxima 5.0 (se empezó con 2.0, pero las vueltas se sentían lentas).

Uno de los problemas a los que se enfentró fue que los movimientos estuvieran volteados y se solucionó incluyendo un menos uno al momento de multiplicar el valor normalizado por la velocidad máxima. Además, al principio se tardaba mucho en reflejar el movimiento del joystick en los valores numéricos de la consola. Para arreglarlo se redujo el delay del código del arduino y se leyó el último valor agregado al buffer serial en el joystick_publisher.

Para comprobar la existencia de los topicos, los nodos y de las conexiones entre ellos se utilizaron los comandos: ros2 topic list, ros2 node list y os2 run rqt_graph rqt_graph.

Link video: https://drive.google.com/file/d/1FGn5c-VW1rkncqe_SYZ-htDWKuNvRAt5/view?usp=sharing
\
Link video pt 2: https://drive.google.com/file/d/1VsNhr2AJOEGM_aN-j5KvuljnaPUv3I12/view?usp=sharing

