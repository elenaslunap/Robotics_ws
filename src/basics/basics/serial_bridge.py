import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial


class SerialBridge(Node):
    def __init__(self):
        # Crea un nodo subscriber "serial_bridge" que recibe mensajes de tipo Int32 a través del tópico "led_command" con una cola de 10 mensajes
        # Llama a la funcion led_callback siempre que recibe un mensaje
        super().__init__('serial_bridge')
        self.subscription_ = self.create_subscription(Int32, '/led_command', self.led_callback,10)
        # Se abre una conexión serial a través del arduino conectado al puerto "/dev/ttyUSB0" con una comunicación serial con velocidad de 115200 baudios.
        self.serial_ = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        # Se imprime en la consola
        self.get_logger().info('Esperando mensajes')

    def led_callback(self, msg):
        # si el valor del mensaje es 1, manda un 1 por la comunicación serial
        if msg.data == 1:
            self.serial_.write(b'1\n')
            # Imprime en la consola el mensaje que envía al serial
            self.get_logger().info('ROS 2 -> Serial: 1')

        # si el valor del mensaje es 0, manda un 0 por la comunicación serial
        elif msg.data == 0:
            self.serial_.write(b'0\n')
            self.get_logger().info('ROS 2 -> Serial: 0')


def main(args=None):
    rclpy.init(args=args)
    node = SerialBridge()
    rclpy.spin(node)
    node.serial_.close()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
