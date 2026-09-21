import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from geometry_msgs.msg import Twist

CENTRO_X = 1850
CENTRO_Y = 1750

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.subscription_ = self.create_subscription(
            Int32MultiArray, 
            '/joystick',
            self.joystick_callback,
            10
        )
        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )
        
        self.get_logger().info("Se inicio la suscripcion de joystick y el publisher de analog")
            
    def normalizar(self, valor, centro):
        distancia = valor - centro
        
        if abs(distancia) < 100:
            return 0.0
        # de que lado está nos dice como normalizar para obtener valores entre -1 y 1
        # del lado positivo
        if distancia > 0:
            return distancia / (4059 - centro)
        # del lado negativo
        else:
            return distancia / centro
        
            
            
    def joystick_callback(self, msg):
        if len(msg.data) < 2:
            return
            
        valor_x = msg.data[0]
        valor_y = msg.data[1]
        
        # Normalizamos para hacer el control proporcional
        # Obtenemos valores entre -1 y 1
        x = self.normalizar(valor_x, CENTRO_X) 
        y = self.normalizar(valor_y, CENTRO_Y)
        
        self.get_logger().info(f"Valores reales: x: {valor_x}, y: {valor_y} - Valores normalizados: x: {x}, y: {y}")
        
        twist = Twist()
        twist.linear.x = -y * 2.0
        twist.angular.z = -x * 2.0
        self.publisher_.publish(twist)
        
def main(args = None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

        
        
            
