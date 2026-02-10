# 🌱 GUÍA DE INSTALACIÓN COMPLETA
## Invernadero Inteligente con ESP32

---

## 📦 MATERIALES NECESARIOS

### Hardware:
- ✅ ESP32 DevKit v1 (o similar)
- ✅ Sensor DHT11 (Temperatura y Humedad)
- ✅ Sensor de Humedad de Suelo (Capacitivo o Resistivo)
- ✅ Módulo Relé de 1 canal (5V)
- ✅ Bomba de agua sumergible 5V/12V
- ✅ Cables Dupont (Macho-Macho y Macho-Hembra)
- ✅ Protoboard (opcional, para pruebas)
- ✅ Fuente de alimentación externa para la bomba (si usa 12V)
- ✅ Cable micro-USB para programar el ESP32

### Software:
- ✅ Arduino IDE 2.x
- ✅ Librerías necesarias (se instalarán después)

---

## 🔌 DIAGRAMA DE CONEXIONES

```
╔═══════════════════════════════════════════════════════════════╗
║                    ESP32 DEVKIT V1                            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  [3.3V] ────┬────────────────┐                              ║
║             │                │                              ║
║             │        DHT11   │   SENSOR SUELO               ║
║             │       ┌─────┐  │    ┌─────┐                  ║
║             └───────┤ VCC │  └────┤ VCC │                  ║
║                     │     │       │     │                  ║
║  [GPIO4] ───────────┤DATA │       │     │                  ║
║                     │     │       │ A0  │───┐              ║
║  [GPIO34]───────────┼─────┼───────┤     │   │              ║
║                     │     │       └─────┘   │              ║
║  [GND] ─────────────┤ GND │───────┐         │              ║
║                     └─────┘       │         │              ║
║                                   │         │              ║
║                                   │         │              ║
║  [GPIO26]────────────────────┐    │         │              ║
║                              │    │         │              ║
║                       RELÉ   │    │         │              ║
║                      ┌────┐  │    │         │              ║
║  [VIN 5V]────────────┤VCC │  │    │         │              ║
║                      │    │  │    │         │              ║
║                      │IN1 │◄─┘    │         │              ║
║                      │    │       │         │              ║
║  [GND]───────────────┤GND │───────┴─────────┘              ║
║                      └──┬─┘                                ║
║                         │                                  ║
║                         │  [COM]──┐                        ║
║                         │  [NO]───┤ BOMBA                  ║
║                         │         └── +                    ║
║                         │                                  ║
║                         └─────────────── -                 ║
║                                                             ║
╚═══════════════════════════════════════════════════════════════╝

NOTAS IMPORTANTES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. DHT11:
   • VCC  → 3.3V del ESP32
   • DATA → GPIO4 del ESP32
   • GND  → GND del ESP32

2. SENSOR DE HUMEDAD DEL SUELO:
   • VCC → 3.3V del ESP32
   • A0  → GPIO34 del ESP32 (pin analógico)
   • GND → GND del ESP32

3. MÓDULO RELÉ:
   • VCC → VIN (5V) del ESP32
   • IN1 → GPIO26 del ESP32
   • GND → GND del ESP32
   • COM → Cable negativo (-) de la fuente de la bomba
   • NO  → Cable negativo (-) de la bomba
   • El positivo (+) de la fuente va directo al (+) de la bomba

4. ALIMENTACIÓN:
   • Si la bomba es de 5V: puedes usar el USB del ESP32
   • Si la bomba es de 12V: necesitas una fuente externa
     (y conectar GND de la fuente con GND del ESP32)
```

---

## ⚙️ PASO 1: INSTALAR ARDUINO IDE

1. **Descargar Arduino IDE 2.x:**
   - Ve a: https://www.arduino.cc/en/software
   - Descarga la versión 2.x para tu sistema operativo
   - Instala el programa

2. **Configurar soporte para ESP32:**
   - Abre Arduino IDE
   - Ve a: `Archivo → Preferencias`
   - En "Gestor de URLs Adicionales de Tarjetas" pega:
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
     ```
   - Haz clic en `OK`

3. **Instalar tarjeta ESP32:**
   - Ve a: `Herramientas → Placa → Gestor de tarjetas...`
   - Busca: `ESP32`
   - Instala: `esp32 by Espressif Systems` (versión 2.x o superior)
   - Espera a que termine la instalación

---

## 📚 PASO 2: INSTALAR LIBRERÍAS

### Método 1: Gestor de Librerías (Recomendado)

1. Ve a: `Programa → Incluir Librería → Administrar librerías...`

2. Instala estas librerías (busca y haz clic en "Instalar"):

   **a) DHT sensor library**
   - Busca: `DHT sensor library`
   - Autor: Adafruit
   - Instala también: `Adafruit Unified Sensor` (se pedirá automáticamente)

   **b) ArduinoJson**
   - Busca: `ArduinoJson`
   - Autor: Benoit Blanchon
   - Versión: 6.x o superior

### Método 2: Manual (si falla el método 1)

1. Descarga las librerías:
   - DHT: https://github.com/adafruit/DHT-sensor-library
   - ArduinoJson: https://github.com/bblanchon/ArduinoJson

2. Ve a: `Programa → Incluir Librería → Añadir biblioteca .ZIP`

3. Selecciona los archivos ZIP descargados

---

## 🔧 PASO 3: CONFIGURAR EL CÓDIGO

1. **Abre el archivo:** `ESP32_Invernadero_Completo.ino`

2. **Configura tu WiFi** (líneas 22-23):
   ```cpp
   const char* ssid = "TU_NOMBRE_WIFI";           // 👈 Cambia esto
   const char* password = "TU_CONTRASEÑA_WIFI";   // 👈 Cambia esto
   ```

3. **Verifica los pines** (líneas 25-28):
   ```cpp
   #define DHTPIN 4              // GPIO4 -> DHT11
   #define SOIL_SENSOR_PIN 34    // GPIO34 -> Sensor Suelo
   #define RELAY_PIN 26          // GPIO26 -> Relé
   ```

4. **Ajusta el umbral de riego** (línea 31):
   ```cpp
   const int UMBRAL_SECO = 30;   // Porcentaje mínimo (ajusta según tu planta)
   ```

5. **Configura tiempo de riego** (línea 32):
   ```cpp
   const int TIEMPO_RIEGO = 3000;  // 3 segundos (3000 ms)
   ```

---

## 📤 PASO 4: SUBIR EL CÓDIGO AL ESP32

1. **Conecta el ESP32** al PC con cable micro-USB

2. **Selecciona la placa:**
   - Ve a: `Herramientas → Placa → ESP32 Arduino → ESP32 Dev Module`

3. **Selecciona el puerto:**
   - Ve a: `Herramientas → Puerto → COM X` (Windows) o `/dev/ttyUSB0` (Linux/Mac)
   - Si no aparece ningún puerto:
     * Windows: Instala drivers CP2102 o CH340
     * Mac/Linux: Puede que no necesites drivers

4. **Configura parámetros:**
   - Upload Speed: `921600`
   - Flash Frequency: `80MHz`
   - Partition Scheme: `Default 4MB with spiffs`

5. **Sube el código:**
   - Haz clic en el botón ➜ (Subir) o presiona `Ctrl + U`
   - **Si da error "Failed to connect":**
     * Mantén presionado el botón `BOOT` del ESP32
     * Haz clic en ➜ (Subir)
     * Suelta `BOOT` cuando aparezca "Connecting..."

6. **Espera** hasta ver "Hard resetting via RTS pin..."

---

## 🖥️ PASO 5: VERIFICAR FUNCIONAMIENTO

1. **Abre el Monitor Serie:**
   - Ve a: `Herramientas → Monitor Serie`
   - Velocidad: `115200 baudios`

2. **Deberías ver:**
   ```
   ========================================
   🌱 INVERNADERO INTELIGENTE - ESP32
   ========================================

   ✓ Sensor DHT11 inicializado
   📡 Conectando a WiFi: TuWiFi
   ✓ WiFi conectado exitosamente!
   📍 Dirección IP: 192.168.1.100
   ✓ Servidor web iniciado

   ========================================
   📱 DASHBOARD LISTO
   ========================================
   🌐 Accede desde tu móvil a: http://192.168.1.100
   ========================================
   ```

3. **¡Importante!** Copia la dirección IP que aparece

---

## 📱 PASO 6: ACCEDER AL DASHBOARD

### Opción A: Dashboard Embebido (Desde el ESP32)

1. **Desde tu móvil o PC:**
   - Conecta a la misma WiFi que el ESP32
   - Abre el navegador
   - Ve a: `http://192.168.1.100` (usa la IP que te dio el ESP32)

2. **Verás el dashboard básico** con datos en tiempo real

### Opción B: Dashboard Avanzado (Archivo HTML Externo)

1. **Abre el archivo:** `dashboard-esp32-final.html`

2. **Haz clic en:** "Conectar al ESP32"

3. **Ingresa la IP:** `192.168.1.100` (la IP que te dio el ESP32)

4. **Haz clic en:** "🔌 Conectar al ESP32"

5. **¡Listo!** Verás el dashboard completo con gráficos y alertas

---

## 🧪 PASO 7: CALIBRACIÓN DE SENSORES

### Sensor de Humedad del Suelo:

1. **Prueba en seco:**
   - Deja el sensor al aire libre (sin tocar nada)
   - Anota el valor que aparece en el Monitor Serie
   - Este será tu valor "seco" (ej: 3500-4095)

2. **Prueba en agua:**
   - Sumerge solo las puntas del sensor en agua
   - Anota el valor (ej: 1000-1500)

3. **Ajusta el código** (línea 116):
   ```cpp
   // Valores originales
   sensores.humedadSuelo = map(valorAnalogico, 4095, 1000, 0, 100);
   
   // Reemplaza 4095 y 1000 con tus valores calibrados
   sensores.humedadSuelo = map(valorAnalogico, TU_VALOR_SECO, TU_VALOR_HUMEDO, 0, 100);
   ```

4. **Vuelve a subir el código**

---

## 🔍 PASO 8: PRUEBAS DEL SISTEMA

### Test 1: Lectura de Sensores
- ✅ Verifica que la temperatura sea realista (15-40°C)
- ✅ Verifica que la humedad esté en 0-100%
- ✅ Toca el sensor de suelo con los dedos húmedos, el valor debe subir

### Test 2: Control Manual
1. En el dashboard, cambia a "Modo Manual"
2. Activa la bomba
3. ✅ Deberías escuchar el relé hacer "clic"
4. ✅ La bomba debería encenderse
5. Desactiva la bomba
6. ✅ La bomba debería apagarse

### Test 3: Modo Automático
1. Cambia a "Modo Automático"
2. Saca el sensor de suelo de la tierra (simular sequía)
3. ✅ Cuando llegue a < 30%, la bomba se activará 3 segundos
4. ✅ Se apagará automáticamente

---

## ❗ SOLUCIÓN DE PROBLEMAS

### ❌ No se conecta al WiFi
```
Solución:
1. Verifica el nombre y contraseña del WiFi
2. Asegúrate de que sea WiFi de 2.4GHz (no 5GHz)
3. Acércate más al router
4. Reinicia el ESP32
```

### ❌ El sensor DHT11 da valores NaN o 0
```
Solución:
1. Revisa las conexiones (VCC, DATA, GND)
2. Asegúrate de que DATA esté en GPIO4
3. El DHT11 tarda 2 segundos en estabilizarse
4. Prueba con otro sensor DHT11
```

### ❌ El sensor de suelo siempre marca 0% o 100%
```
Solución:
1. Verifica que A0 del sensor esté en GPIO34
2. Calibra el sensor (ver PASO 7)
3. Algunos sensores tienen un potenciómetro, ajústalo
```

### ❌ El relé no hace "clic"
```
Solución:
1. Verifica que VCC del relé esté en VIN (5V)
2. Verifica que IN1 esté en GPIO26
3. Prueba cambiando LOW por HIGH en la línea 77:
   digitalWrite(RELAY_PIN, HIGH);  // Algunos relés son activos en LOW
```

### ❌ No puedo ver el dashboard en el móvil
```
Solución:
1. Asegúrate de estar en la misma WiFi
2. Desactiva datos móviles
3. Prueba con http:// (no https://)
4. Verifica la IP en el Monitor Serie
5. Prueba primero desde el PC
```

---

## 📊 DATOS TÉCNICOS

### Consumo Eléctrico:
- ESP32: ~80-160mA (depende del uso de WiFi)
- DHT11: ~0.5-2.5mA
- Sensor Suelo: ~5mA
- Relé: ~15-20mA
- Bomba 5V: ~100-300mA
- **Total aprox:** 200-500mA a 5V

### Rango de Sensores:
- DHT11 Temperatura: 0-50°C (±2°C precisión)
- DHT11 Humedad: 20-90% (±5% precisión)
- Sensor Suelo: 0-100% (depende de calibración)

---

## 🎓 PRÓXIMOS PASOS

Una vez que todo funcione, puedes:

1. **Añadir más sensores:**
   - Sensor de luz (LDR)
   - Sensor de nivel de agua
   - Sensor de pH

2. **Mejoras de software:**
   - Base de datos para históricos
   - Notificaciones por Telegram
   - Integración con MQTT

3. **Mejoras de hardware:**
   - Panel solar para alimentación
   - Pantalla OLED local
   - Múltiples zonas de riego

---

## 📞 SOPORTE

Si tienes problemas:
1. Revisa el Monitor Serie (115200 baudios)
2. Verifica las conexiones físicas
3. Comprueba que las librerías estén instaladas
4. Asegúrate de que el WiFi sea de 2.4GHz

---

## ✅ CHECKLIST FINAL

Antes de la presentación, verifica:

- [ ] ESP32 conectado y funcionando
- [ ] WiFi configurado correctamente
- [ ] Sensores leyendo valores realistas
- [ ] Bomba se activa/desactiva correctamente
- [ ] Dashboard accesible desde móvil
- [ ] Modo automático funciona
- [ ] Modo manual funciona
- [ ] Gráfico histórico se actualiza
- [ ] Alertas aparecen cuando corresponde
- [ ] Monitor Serie muestra datos sin errores

---

## 🎉 ¡FELICIDADES!

Tu Invernadero Inteligente está listo para funcionar.

**Presupuesto total:** ~53€
**Tiempo de montaje:** 2-3 horas
**Dificultad:** Media

¡Éxito en tu presentación! 🌱🤖
