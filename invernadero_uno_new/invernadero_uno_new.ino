#include <DHT.h>
#include <ArduinoJson.h>

// ========== PINES DE HARDWARE ==========
#define DHTPIN 2
#define DHTTYPE DHT11
#define SOIL_SENSOR_PIN A0
#define RELAY_PIN 8

// ========== CONFIGURACIÓN ==========
const int UMBRAL_SECO = 30;
const unsigned long INTERVALO_LECTURA = 2000;
const int BOMBA_ENCENDIDA = LOW;
const int BOMBA_APAGADA = HIGH;

// ========== VARIABLES ==========
DHT dht(DHTPIN, DHTTYPE);

struct SensorData {
  float temperatura;
  float humedad;
  int humedadSuelo;
  unsigned long ultimaLectura;
} sensores;

struct SystemState {
  bool bombaActiva;
  bool modoAutomatico;
} sistema;

void setup() {
  Serial.begin(9600);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, BOMBA_APAGADA);
  dht.begin();
  sistema.bombaActiva = false;
  sistema.modoAutomatico = false;
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    StaticJsonDocument<100> doc;
    DeserializationError error = deserializeJson(doc, input);
    
    if (!error && doc.containsKey("cmd")) {
      String cmd = doc["cmd"];
      if (cmd == "pump_on" && !sistema.modoAutomatico) encenderBomba();
      if (cmd == "pump_off" && !sistema.modoAutomatico) apagarBomba();
      if (cmd == "mode_auto") sistema.modoAutomatico = true;
      if (cmd == "mode_man") sistema.modoAutomatico = false;
    }
  }

  if (millis() - sensores.ultimaLectura >= INTERVALO_LECTURA) {
    float t = dht.readTemperature();
    float h = dht.readHumidity();
    
    if (!isnan(t) && !isnan(h)) {
      sensores.temperatura = t;
      sensores.humedad = h;
    }
    
    int valor = analogRead(SOIL_SENSOR_PIN);
    sensores.humedadSuelo = map(valor, 1023, 200, 0, 100);
    sensores.humedadSuelo = constrain(sensores.humedadSuelo, 0, 100);
    sensores.ultimaLectura = millis();
    enviarDatosSerial();
  }

  if (sistema.modoAutomatico) {
    if (sensores.humedadSuelo < UMBRAL_SECO && !sistema.bombaActiva) {
      encenderBomba();
    } else if (sensores.humedadSuelo > (UMBRAL_SECO + 10) && sistema.bombaActiva) {
      apagarBomba();
    }
  }
}

// Nota: Asegúrate de tener estas funciones definidas al final de tu código
void encenderBomba() {
  digitalWrite(RELAY_PIN, BOMBA_ENCENDIDA);
  sistema.bombaActiva = true;
}

void apagarBomba() {
  digitalWrite(RELAY_PIN, BOMBA_APAGADA);
  sistema.bombaActiva = false;
}

void enviarDatosSerial() {
  StaticJsonDocument<200> doc;
  doc["temp"] = sensores.temperatura;
  doc["hum"] = sensores.humedad;
  doc["soil"] = sensores.humedadSuelo;
  doc["pump"] = sistema.bombaActiva;
  doc["auto"] = sistema.modoAutomatico;
  serializeJson(doc, Serial);
  Serial.println();
}