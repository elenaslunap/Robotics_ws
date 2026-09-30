import serial
import time

# Se define el puerto y la velocidad
PORT = '/dev/ttyUSB0'
BAUDRATE = 115200

# Se establece la conexion serial 
esp32 = serial.Serial(PORT, BAUDRATE, timeout=1)

# Se detiene la ejecucion por dos segundos
time.sleep(2)

# Loop infinito
while True:
    
    # Se recibe la cadena de dato con input
    dato = input("Escribe 1 para encender, 0 para apagar, q para salir: ")

    # Si el dato es igual a 1, envía un 1 por el canal de comunicación serial
    if dato == '1':
        esp32.write(b'1\n')
    # Si el dato es igual a 0, envía un 0 por el canal de comunicación serial
    elif dato == '0':
        esp32.write(b'0\n')
    # Si el dato es igual a q, sale del ciclo. 
    elif dato == 'q':   
        break

esp32.close()

