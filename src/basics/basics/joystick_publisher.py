import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import serial

class JoystickPublisher(Node):
    def __init__(self):
    
        super().__init__('joystick_publisher')
        
        self.publisher_ = self.create_publisher(
            Int32MultiArray,
            '/joystick',
            10
        )
        
        self.serial_ = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.get_logger().info('Se inicio la comunicacion serial')
        
        self.timer_ = self.create_timer(
            0.5,
            self.read_serial
        )
        self.get_logger().info('Publisher de joystick iniciado')

    def read_serial(self):
        
        while self.serial_.in_waiting > 0:
            linea = self.serial_.readline().decode().strip()
            valores = linea.split(',')
            if len(valores) < 2:
                return
            x = int(valores[0])
            y = int(valores[1])
            
            msg = Int32MultiArray()
            msg.data = [x,y]
            self.publisher_.publish(msg)
            
def main(args=None):
    rclpy.init(args=args)
    node = JoystickPublisher()
    rclpy.spin(node)
    node.serial_.close()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        
        
