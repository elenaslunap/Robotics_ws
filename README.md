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

## Actividad 3: Ejemplo del LED

El objetivo de esta práctica fue prender y apagar el led de la placa ESP32.

Primero, se comprobó el funcionamiento de los cables y la placa corriendo el código de LED_serial.ino dentro del IDE de Arduino. Este código primero define al pin 2 (LED) como un output y luego, a través de un loop infinito, lee el valor que encuentre dentro del buffer de la comunicación serial. Si es un 1, manda un "HIGH" al output i.e. 3.3V y, si es un 0, manda 0V o un "LOW". 

Una vez comprobado el funcionamiento de este código, se crearon dos nodos en ROS2. Primero, el nodo "led_blink", que se encarga de publicar mensajes de tipo Int32 a través del tópico "/led_command". Cada segundo este código aplica un XOR lógico al atributo de "estado" de la clase y lo publica como mensaje. Segundo, se creó el nodo "serial_bridge" el cual se suscribe a los mensajes del tópico "led_command" y abre un puerto de comunicación serial '/dev/ttyUSB0' con una velocidad de 115200 baudios. Cada que recibe un mensaje, llama a la función "led_callback", la cual manda el valor del mensaje recibido (0 o 1) al buffer de la comunicación serial utilizando "serial.write(b'{valor}\n')".

En setup.py se incluyeron los entrypoints para ambos nodos:
- 'led_blink = basics.led_blink:main'
- 'serial_bridge = basics.serial_bridge:main'

Además, para que se reconociera el puerto '/dev/ttyUSB0', se tuvieron que correr los comandos "ls /dev/ttyUSB*" y "sudo chmod 777 /dev/ttyUSB0".

<img width="1206" height="588" alt="image" src="https://github.com/user-attachments/assets/7fe716e7-55cc-4315-bea2-ad3044783fc0" />

