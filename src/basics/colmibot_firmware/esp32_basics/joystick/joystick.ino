// define las constantes JOYSTICK_X y JOYSTICK_Y con los valores 34 y 35
#define JOYSTICK_X 34
#define JOYSTICK_Y 35

void setup() {

  Serial.begin(115200);

}


// loop infinito
// le el valor que recibe del ADC de coordenada x y y del joystick
// manda ambas coordenadas al buffer serial con el formato: x,y
void loop() {
  // put your main code here, to run repeatedly:
  int valor_x = analogRead(JOYSTICK_X);
  int valor_y = analogRead(JOYSTICK_Y);

  Serial.print(valor_x);
  Serial.print(",");
  Serial.println(valor_y);

  delay(20);
}

