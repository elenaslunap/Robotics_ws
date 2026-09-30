import serial

# Se define el puerto y la velocidad
PORT = '/dev/ttyUSB0'
BAUDRATE = 115200

# Se establece la conexion serial 
esp32 = serial.Serial(PORT, BAUDRATE, timeout=1)

# Loop infinito que lee los mensajes dentro del buffer
# Lee lo que encuentre en el buffer (hasta un salto de linea)
# La linea de bytes la convierte en un string (con deocode)
# Elimina espacios extra con strip
while True:
    linea = esp32.readline().decode().strip()
    # Imprime la linea en la consola
    if linea:
        print(f'ADC = {linea}')

