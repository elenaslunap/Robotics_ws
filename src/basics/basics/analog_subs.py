import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class AnalogSubscriber(Node):
    def __init__(self):
        super().__init__('analog_subscriber')
        # Se crea un nodo subscriber que reciba mensajes de tipo Int32 a través del tópico /analog' y llama la función analog_callback siempre que reciba un nuevo mensaje. Tiene una cola de 10 mensajes.
        self.subscription_ = self.create_subscription(Int32, '/analog', self.analog_callback, 10)
        # Imprime en la consola un mensaje
        self.get_logger().info('Esperando datos')

    def analog_callback(self, msg):
        # Guarda el valor de tipo Int32 en la variable valor
        valor = msg.data
        # Imprime el valor del mensaje ADC
        # analog to digital converter (12 bits --> 0 a 4095 para representar de 0V a 3.3V)
        # Aqui el potenciometro funciona como divisor de voltaje
        self.get_logger().info(f'ADC = {valor}')

def main(args=None):
    rclpy.init(args=args)
    node = AnalogSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
