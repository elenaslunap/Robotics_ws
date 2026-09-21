import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from geometry_msgs.msg import Twist

# Se define el "centro" del joystic, i.e. los valores que manda el joystick cuando no se esta moviento
CENTRO_X = 1850
CENTRO_Y = 1750


class TurtleController(Node):


    def __init__(self):
    
        # se crea la subscripción al topico /joystick y recibirá mensajes de tipo Int32MultiArray
        super().__init__('turtle_controller')
        self.subscription_ = self.create_subscription(
            Int32MultiArray, 
            '/joystick',
            self.joystick_callback,
            10
        )
        # también se define como nodo publisher del topico /turtle1/cmd_vel y manda mensajes de tipo Twist
        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )
        
        self.get_logger().info("Se inicio la suscripcion de joystick y el publisher de analog")
            
    def normalizar(self, valor, centro):
        # define la distancia del valor al ventro del joystick
        # si la distancia es menor a 100 (dead zone): regresa 0.0
        # sino, define si es un valor mayor o menor al centro
        # normaliza el valor con respecto al centro y obtiene valores entre -1 y 1
        
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
        # lee los valores de x y y que recibe del arreglo
        # los normaliza con relación al centro del joystick
        # escribe en la consola el valor real y el valor normalizado
        # multiplica los valores normalizados por la velocidad máxima (5.0)
        # publica los valores en los componentes linear.x y angular.z como mensajes de tipo Twist
        
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
        twist.linear.x = -y * 5.0
        twist.angular.z = -x * 5.0
        self.publisher_.publish(twist)
        
def main(args = None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

        
        
            
