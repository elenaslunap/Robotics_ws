Elena Sofía Luna Palacio - 201041

En esta actividad creamos nuestro primer paquete de ROS2 con un publisher, un nodo que publicara mensajes de velocidad, y un subscriber, un nodo que esperara estos mensajes.

Los dos nodos creados fueron:

- velocity_publsiher.py
- velocity_subscriber.py

El primer nodo publica mensajes de tipo Float32 a través de un tópico llamado "velocity" con una cola de tamaño 10.

El segundo nodo se susbcribe al tópico "velocity" y manda a llamar a la función velocity_callback siempre que reciba un mensaje i.e. el segundo nodo se mantiene escuchando el tópico de velocidad en espera de nuevos mensajes. 

Además, se añadieron entry_points en setup.py para poder ejecutar los programas de ambos nodos como parte del paquete de basics. Tambipen modificamos el package.xml con la información de nuestro nuevo paquete.

Los comandos utilizados para la ejecución fueron 

- colcon build: para crear ("build") nuestro nuevo paquete basics
- ros2 run basics velocity_publisher: para correr el nodo velocity_publisher, que publicará velocidades en el tópico "velocity".
- ros2 run basics velocity_subscriber: en una segunda terminal, escuchará las velocidades publicadas en el tópico "velocity" y las imprime en la terminal.

El úncio problema que tuvimos fue que la terminal no reconocía los comandos porque no sabía qué path seguir. Para solucionarlo añadimos source /opt/ros/jazzy/setup.bash y 
source /home/parallels/robotics_ws/install/setup.bash como comandos de source.

