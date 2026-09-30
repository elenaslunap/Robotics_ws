// define la constante POT con el numero 15
#define POT 15

void setup() {
  // se inicia la comunicación serial a una velocidad de 115200 baudios
  Serial.begin(115200);
}

void loop() {
  // se lee el voltaje que recibe el pin POT y se guarda en valor
  int valor = analogRead(POT);
  // se manda el valor por la comunicación serial
  Serial.println(valor);
  // el programa espera 100 milisegundos
  delay(100);
}
