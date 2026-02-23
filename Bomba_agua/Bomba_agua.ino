int pinRele = 8; // Pin donde conectamos el IN del relé

void setup() {
  pinMode(pinRele, OUTPUT); // Configuramos el pin como salida
}

void loop() {
  digitalWrite(pinRele, LOW);  // En muchos relés, LOW activa el paso de corriente
  delay(5000);                 // Espera 5 segundos
  
  digitalWrite(pinRele, HIGH); // HIGH apaga el relé
  delay(5000);                 // Espera 5 segundos
}