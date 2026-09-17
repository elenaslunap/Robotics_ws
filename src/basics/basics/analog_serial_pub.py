import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial


class AnalogSerialPublisher(Node):
    def __init__(self):
        super().__init__('analog_serial_pub')
        # Se crea un nodo publisher que manda mensajes de tipo Int32 a través del topico "analog" con una cola de 10 mensajes.
        self.publisher_ = self.create_publisher(Int32,'/analog', 10)
        # Se define una comunicación serial a través del puerto '/dev/ttyUSB0' con una velocidad de 115200 baudios
        self.serial_ = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        # Se manda a llamar la función read_serial cada 0.01 segundos
        self.timer_ = self.create_timer(0.01, self.read_serial)
        # Se imprime en la terminal un mensaje de confirmación de la comunicación serial establecida
        self.get_logger().info('ESP32 conectada')

    def read_serial(self):
        # Si hay bytes en el buffer, se leen hasta encontrar un salto de línea
        # Lo convierte a texto y elimina espacios y saltos de línea extra
        # Se guarda el resultado en la variable linea
        if self.serial_.in_waiting > 0:
            linea = self.serial_.readline().decode().strip()
            
            # Si linea es un digito se convierte en int.
            # Se crea un msg de tipo Int32 y se guarda el valor de linea 
            # El nodo public el mensaje.
            if linea.isdigit():
                valor = int(linea)
                msg = Int32()
                msg.data = valor
                self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = AnalogSerialPublisher()
    rclpy.spin(node)
    node.serial_.close()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
