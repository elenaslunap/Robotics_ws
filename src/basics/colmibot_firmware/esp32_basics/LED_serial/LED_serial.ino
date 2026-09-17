// define la constante LED con el numero 2
#define LED 2

void setup() {
  // se configura el pin 2 (LED) como salida
  pinMode(LED, OUTPUT);

  // se inicia la comunicación serial a una velocidad de 115200 baudios
  Serial.begin(115200);
}

// loop continuo mientras la placa este prendida
void loop() {
  // si hay algun dato que leer el buffer seiral
  if (Serial.available() > 0) {
    
    // se lee el primer byte recibido y se guarda como char 
    char dato = Serial.read();
    
    // si el dato es '1', manda 3.3V a LED (pin 2)
    if (dato == '1') {
      digitalWrite(LED, HIGH);
    }
    
    // si el dato es '0', manda 0V a LED (pin 2)
    if (dato == '0') {
      digitalWrite(LED, LOW);
    }
  }
}
