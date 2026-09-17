import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

# Se confirmó el funcionamiento del ejemplo del LED.

# Define al nodo publisher "led_blink" 
class LedBlink(Node):
    def __init__(self):
        super().__init__('led_blink')
        #E s un nodo  publisher que envía mensajes de tipo Int32 a través del tópico led_command con una cola de tamaño 10.
        self.publisher_ = self.create_publisher(Int32, '/led_command', 10)
        # Define el atributo estado con un valor inicial de 1
        self.estado = 1
        # Llama a la función blink_callback cada 1 segundo
        self.timer_ = self.create_timer(1.0, self.blink_callback)
        # Imprime en la consola mensaje de nodo iniciado
        self.get_logger().info('Nodo iniciado')
        # Llama a la funcion publicar_estado
        self.publicar_estado()

    def blink_callback(self):
        # XOR lógico para cambiar el valor de estado
        if self.estado == 1:
            self.estado = 0
        else:
            self.estado = 1
        # llama a la función publicar_estado
        self.publicar_estado()

    def publicar_estado(self):
        # Define msg como un int32
        msg = Int32()
        # Define el contenido del msg igual al valor del estado
        msg.data = self.estado

        # el publisher publica el mensaje msg (Int 32) con el valor del estado
        self.publisher_.publish(msg)
        # imprime en la consola el valor publicado.
        self.get_logger().info(f'Publicando: {self.estado}')

def main(args=None):
    rclpy.init(args=args)
    node = LedBlink()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
