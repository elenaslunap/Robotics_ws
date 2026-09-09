import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class VelocityTurtleSubscriber(Node):

    # Se crea la subscripción al tópico turtle1/cmd_vel
    def __init__(self):
        super().__init__('twist_subscriber')
        self.subscription_ = self.create_subscription(Twist,'/turtle1/cmd_vel',self.twist_callback,10)

    # Se imprime en la consola la velocidad recibida
    def twist_callback(self, msg):
        linear_x = msg.linear.x
        self.get_logger().info(f'msg.linear.x = {linear_x:.1f} m/s')


def main(args = None):
    rclpy.init(args=args)
    node = VelocityTurtleSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

