import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class VelocityTurtlePublisher(Node):

    def __init__(self):
        super().__init__('twist_publisher')

        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.Vel = 0.0

        self.timer_ = self.create_timer(
            0.5,
            self.publish_twist
        )
        

    def publish_twist(self):

        msg = Twist()

        msg.linear.x = self.Vel
        
        if self.Vel < 1.2:
            self.publisher_.publish(msg)
            self.Vel = round(self.Vel + 0.1, 1)
    
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

