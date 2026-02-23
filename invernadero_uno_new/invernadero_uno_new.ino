/*
 * ========================================
 * INVERNADERO INTELIGENTE - ARDUINO UNO
 * ========================================
 * 
 * Este código lee los sensores y permite control manual/automático.
 * La comunicación con la web se realizará vía Serial (JSON).
 */

#include <DHT.h>
#include <ArduinoJson.h>

// ========== PINES DE HARDWARE ==========
#define DHTPIN 2              // Pin Digital 2 -> Sensor DHT11
#define DHTTYPE DHT11         
#define SOIL_SENSOR_PIN A0    // Pin Analógico A0 -> Sensor Humedad Suelo
#define RELAY_PIN 3           // Pin Digital 3 -> Módulo Relé

// ========== CONFIGURACIÓN ==========
const int UMBRAL_SECO = 30;           // % mínimo para riego automático
const int TIEMPO_RIEGO = 3000;        // 3 segundos de riego
const unsigned long INTERVALO_LECTURA = 2000; 

// ========== VARIABLES GLOBALES ==========
DHT dht(DHTPIN, DHTTYPE);

struct SensorData {
    float temperatura;
    float humedad;
    int humedadSuelo;
    unsigned long ultimaLectura;
} sensores;

struct SystemState {
    bool bombaActiva;
    bool modoAutomatico; // true = auto, false = manual
    unsigned long tiempoInicioRiego;
    bool riegoEnProceso;
} sistema;

void setup() {
    Serial.begin(9600); // Velocidad estándar para Arduino Uno
    
    pinMode(RELAY_PIN, OUTPUT);
    digitalWrite(RELAY_PIN, LOW); // Apagado por defecto
    
    dht.begin();
    
    // Estado inicial
    sistema.bombaActiva = false;
    sistema.modoAutomatico = true;
    sistema.riegoEnProceso = false;
}

void loop() {
    // 1. Leer comandos desde el puerto serie (vía Python/Web)
    verificarComandosSerial();

    // 2. Leer sensores cada intervalo
    if (millis() - sensores.ultimaLectura >= INTERVALO_LECTURA) {
        leerSensores();
        
        // Enviamos ambos formatos
        enviarDatosSerial();   // Formato JSON para Python/Web
        mostrarDatosConsola(); // Formato Texto para humanos
        
        sensores.ultimaLectura = millis();
    }

    // 3. Lógica de Riego
    if (sistema.modoAutomatico) {
        controlarRiegoAutomatico();
    }

    // 4. Control de tiempo de la bomba
    if (sistema.riegoEnProceso) {
        if (millis() - sistema.tiempoInicioRiego >= TIEMPO_RIEGO) {
            apagarBomba();
        }
    }
}

void leerSensores() {
    // El DHT11 es lento, le damos un momento antes de pedir datos
    delay(50); 
    
    float t = dht.readTemperature();
    float h = dht.readHumidity();
    
    // FILTRO DE SEGURIDAD: 
    // Si la lectura es NaN o un valor imposible (como 80°C o -20°C en interior), la ignoramos
    if (!isnan(t) && !isnan(h) && t > 0 && t < 60) {
        sensores.temperatura = t;
        sensores.humedad = h;
    } else {
        Serial.println(F("⚠️ Error: Lectura de DHT11 no válida (revisa cables)"));
    }
    
    int valorAnalogico = analogRead(SOIL_SENSOR_PIN);
    // Calibración: 1023 es seco, ~200 es muy húmedo
    sensores.humedadSuelo = map(valorAnalogico, 1023, 200, 0, 100);
    sensores.humedadSuelo = constrain(sensores.humedadSuelo, 0, 100);
}

void mostrarDatosConsola() {
    Serial.println(F("\n--- ESTADO INVERNADERO ---"));
    Serial.print(F("🌡️ Temp: ")); Serial.print(sensores.temperatura); Serial.println(F(" °C"));
    Serial.print(F("💧 Hum: ")); Serial.print(sensores.humedad); Serial.println(F(" %"));
    Serial.print(F("🌱 Suelo: ")); Serial.print(sensores.humedadSuelo); Serial.println(F(" %"));
    Serial.print(F("💦 Bomba: ")); Serial.println(sistema.bombaActiva ? F("ENCENDIDA") : F("APAGADA"));
    Serial.print(F("🤖 Modo: ")); Serial.println(sistema.modoAutomatico ? F("Automático") : F("Manual"));
    Serial.println(F("--------------------------"));
}

void controlarRiegoAutomatico() {
    if (sensores.humedadSuelo < UMBRAL_SECO && !sistema.bombaActiva && !sistema.riegoEnProceso) {
        Serial.println(F("! Alerta: Suelo seco. Iniciando riego..."));
        encenderBomba();
    }
}

void encenderBomba() {
    digitalWrite(RELAY_PIN, HIGH);
    sistema.bombaActiva = true;
    sistema.riegoEnProceso = true;
    sistema.tiempoInicioRiego = millis();
}

void apagarBomba() {
    digitalWrite(RELAY_PIN, LOW);
    sistema.bombaActiva = false;
    sistema.riegoEnProceso = false;
}

// Envía los datos en formato JSON para que la web los procese
void enviarDatosSerial() {
    StaticJsonDocument<200> doc;
    doc["temp"] = sensores.temperatura;
    doc["hum"] = sensores.humedad;
    doc["soil"] = sensores.humedadSuelo;
    doc["pump"] = sistema.bombaActiva;
    doc["auto"] = sistema.modoAutomatico;
    
    serializeJson(doc, Serial);
    Serial.println(); // Nueva línea para separar paquetes
}

// Recibe comandos desde la web/PC
void verificarComandosSerial() {
    if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');
        StaticJsonDocument<100> doc;
        DeserializationError error = deserializeJson(doc, input);
        
        if (!error) {
            if (doc.containsKey("cmd")) {
                String cmd = doc["cmd"];
                if (cmd == "pump_on" && !sistema.modoAutomatico) encenderBomba();
                if (cmd == "pump_off" && !sistema.modoAutomatico) apagarBomba();
                if (cmd == "mode_auto") sistema.modoAutomatico = true;
                if (cmd == "mode_man") sistema.modoAutomatico = false;
            }
        }
    }
}
