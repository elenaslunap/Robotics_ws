import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class VelocityTurtlePublisher(Node):

    def __init__(self):
        super().__init__('twist_publisher')
        # Publisher que manda mensajes de tipo Twist al tópico '/turtle1/cmd_vel con una cola de tamaño 10
        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )
        # Velocidad comienza en 0
        self.Vel = 0.0

        # Se llama a publish_twist cada 0.5 segundos
        self.timer_ = self.create_timer(
            0.5,
            self.publish_twist
        )
        

    def publish_twist(self):

        msg = Twist()
        
        msg.linear.x = self.Vel
        
        # Si la velocidad es menor o igual a 1.2, aumenta por 0.1
        if self.Vel <= 1.2:
            self.publisher_.publish(msg)
            self.Vel = round(self.Vel + 0.1, 1)
        # Si la velocidad es mayor a 1.2, se publica una velocidad de 0.0 para detener a la tortuga 
        else:
            msg.linear.x = 0.0
            self.publisher_.publish(msg)
            
        self.get_logger().info(
            f'Publicando: msg.linear.x = {msg.linear.x:.1f} m/s'
        )
            


def main(args=None):

    rclpy.init(args=args)

    node = VelocityTurtlePublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()

