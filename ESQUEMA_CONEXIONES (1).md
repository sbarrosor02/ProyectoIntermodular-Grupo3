# 🔌 ESQUEMA DE CONEXIONES DETALLADO
## Invernadero Inteligente ESP32

---

## 📐 DIAGRAMA COMPLETO DE PINES

```
                                ESP32 DEVKIT V1
                    ╔═══════════════════════════════╗
                    ║                               ║
                    ║  ┌─────────────────────────┐ ║
                    ║  │      MICRO USB         │  ║
                    ║  └─────────────────────────┘ ║
                    ║                               ║
    ┌───────────────╫───────────────────────────────╫───────────────┐
    │               ║                               ║               │
    │  3.3V  ●──────╫──┬─────────────────────┬─────╫──────●  GND   │
    │        │      ║  │                     │     ║      │         │
    │  EN    ●      ║  │   ┌──DHT11──┐      │     ║      ●  GPIO23 │
    │        │      ║  │   │         │      │     ║      │         │
    │  GPIO36●      ║  └───┤VCC      │      │     ║      ●  GPIO22 │
    │        │      ║      │         │      │     ║      │         │
    │  GPIO39●      ║  ┌───┤DATA     │      │     ║      ●  TX0    │
    │        │      ║  │   │         │      │     ║      │         │
    │  GPIO34●──────╫──┼───┤GND      │──────┼─────╫──┬───●  RX0    │
    │        │      ║  │   └─────────┘      │     ║  │   │         │
    │  GPIO35●      ║  │                    │     ║  │   ●  GPIO21 │
    │        │      ║  │   SENSOR SUELO     │     ║  │   │         │
    │  GPIO32●      ║  │   ┌─────────┐     │     ║  │   ●  GPIO19 │
    │        │      ║  │   │         │     │     ║  │   │         │
    │  GPIO33●      ║  └───┤VCC      │     │     ║  │   ●  GPIO18 │
    │        │      ║      │         │     │     ║  │   │         │
    │  GPIO25●      ║      │A0       │─────┘     ║  │   ●  GPIO5  │
    │        │      ║      │         │           ║  │   │         │
    │  GPIO26●──────╫──────┤GND      │───────────╫──┘   ●  GPIO17 │
    │        │      ║      └─────────┘           ║      │         │
    │  GPIO27●      ║                            ║      ●  GPIO16 │
    │        │      ║      MÓDULO RELÉ           ║      │         │
    │  GPIO14●      ║      ┌─────────┐           ║      ●  GPIO4  │
    │        │      ║      │         │           ║      │         │
    │  GPIO12●      ║  ┌───┤VCC      │           ║      ●  GPIO2  │
    │        │      ║  │   │         │           ║      │         │
    │  GPIO13●      ║  │   │IN1      │◄──────────╫──────●  GPIO15 │
    │        │      ║  │   │         │           ║               │
    │  GND   ●──────╫──┼───┤GND      │           ║      ●  GND    │
    │        │      ║  │   └─────────┘           ║      │         │
    │  VIN   ●──────╫──┘                         ║      ●  3.3V   │
    │               ║                            ║               │
    └───────────────╫────────────────────────────╫───────────────┘
                    ║                            ║
                    ║  ┌─────────────────────┐  ║
                    ║  │       BOOT          │  ║
                    ║  └─────────────────────┘  ║
                    ║                            ║
                    ╚════════════════════════════╝
```

---

## 📋 TABLA DE CONEXIONES

| Componente | Pin Componente | Pin ESP32 | Descripción |
|------------|----------------|-----------|-------------|
| **DHT11** | VCC | 3.3V | Alimentación positiva |
| | DATA | GPIO4 | Pin de datos (sensor) |
| | GND | GND | Tierra |
| **Sensor Suelo** | VCC | 3.3V | Alimentación positiva |
| | A0 | GPIO34 | Salida analógica |
| | GND | GND | Tierra |
| **Módulo Relé** | VCC | VIN (5V) | Alimentación positiva |
| | IN1 | GPIO26 | Señal de control |
| | GND | GND | Tierra |
| | COM | - Bomba | Común (polo negativo fuente) |
| | NO | - Bomba | Normalmente abierto (polo negativo bomba) |
| **Bomba** | + | + Fuente | Positivo de alimentación |
| | - | NO Relé | Negativo (pasa por relé) |

---

## 🔧 DETALLES DE CADA CONEXIÓN

### 1️⃣ SENSOR DHT11 (Temperatura y Humedad)

```
    DHT11                     ESP32
    ┌───┐                    ┌───┐
    │ 1 │ VCC  ──────────────│3.3V│
    │ 2 │ DATA ──────────────│ 4 │ GPIO4
    │ 3 │ NC   (sin conectar)│   │
    │ 4 │ GND  ──────────────│GND│
    └───┘                    └───┘
```

**Notas:**
- Algunos DHT11 tienen 3 pines (VCC, DATA, GND)
- Otros tienen 4 pines (el pin 3 no se usa)
- Algunos necesitan resistencia pull-up de 10kΩ entre DATA y VCC
- La mayoría de módulos DHT11 ya traen la resistencia integrada

**Código relacionado:**
```cpp
#define DHTPIN 4        // GPIO4
#define DHTTYPE DHT11
```

---

### 2️⃣ SENSOR DE HUMEDAD DEL SUELO

```
    SENSOR SUELO              ESP32
    ┌──────────┐             ┌───┐
    │ VCC/+    │ ────────────│3.3V│
    │ GND/-    │ ────────────│GND│
    │ A0/AOUT  │ ────────────│ 34│ GPIO34 (ADC1_CH6)
    └──────────┘             └───┘
```

**Notas:**
- Usa GPIO34 (pin analógico ADC1_CH6)
- Rango de lectura: 0-4095 (12 bits)
- NO uses GPIO35, 36, 39 si usas WiFi (interferencia)
- Algunos sensores tienen D0 (digital), no lo uses
- Calibra el sensor para tu tipo de tierra

**Código relacionado:**
```cpp
#define SOIL_SENSOR_PIN 34
int valorAnalogico = analogRead(SOIL_SENSOR_PIN);
```

**Calibración:**
```cpp
// Valores típicos (ajusta según tu sensor):
// Seco: 3500-4095
// Húmedo: 1000-1500
sensores.humedadSuelo = map(valorAnalogico, 4095, 1000, 0, 100);
```

---

### 3️⃣ MÓDULO RELÉ (Control de Bomba)

```
    RELÉ                      ESP32
    ┌──────┐                 ┌───┐
    │ VCC  │ ────────────────│VIN│ (5V)
    │ GND  │ ────────────────│GND│
    │ IN1  │ ────────────────│ 26│ GPIO26
    └──────┘                 └───┘
    
    Conexión de potencia:
    
    FUENTE        RELÉ         BOMBA
    ┌────┐       ┌────┐       ┌────┐
    │ +  │───────┼────┼───────│ +  │
    │    │       │COM │       │    │
    │ -  │───────│ NO │───────│ -  │
    └────┘       └────┘       └────┘
```

**Notas:**
- VCC del relé necesita 5V (conectar a VIN)
- Algunos relés son "activos en LOW" (se encienden con 0V)
- Otros son "activos en HIGH" (se encienden con 5V)
- COM = Común (siempre conectado)
- NO = Normalmente Abierto (se cierra al activar)
- NC = Normalmente Cerrado (no usar en este proyecto)

**Código relacionado:**
```cpp
#define RELAY_PIN 26
pinMode(RELAY_PIN, OUTPUT);
digitalWrite(RELAY_PIN, HIGH);  // Encender
digitalWrite(RELAY_PIN, LOW);   // Apagar
```

**Si tu relé no funciona, prueba invertir:**
```cpp
digitalWrite(RELAY_PIN, LOW);   // Encender
digitalWrite(RELAY_PIN, HIGH);  // Apagar
```

---

### 4️⃣ BOMBA DE AGUA

**Opción A: Bomba 5V (Mini bomba sumergible)**
```
    FUENTE 5V USB/Banco    RELÉ      BOMBA 5V
    ┌────────┐           ┌────┐     ┌────┐
    │   +    │───────────┤COM ├─────┤ +  │
    │        │           │    │     │    │
    │   -    │───────────┤ NO ├─────┤ -  │
    └────────┘           └────┘     └────┘
```

**Opción B: Bomba 12V (Bomba más potente)**
```
    FUENTE 12V           RELÉ      BOMBA 12V
    ┌────────┐         ┌────┐     ┌────┐
    │   +    │─────────┤COM ├─────┤ +  │
    │        │         │    │     │    │
    │   -    │─────────┤ NO ├─────┤ -  │
    └────────┘         └────┘     └────┘
         │                          
         └─────────┐                
                   │                
    ESP32         GND               
    ┌────┐         │                
    │GND │─────────┘                
    └────┘                          

IMPORTANTE: Conectar GND común entre ESP32 y fuente 12V
```

**Tipos de bombas:**
- **Mini bomba 3-5V:** 100-300 mA, para proyectos pequeños
- **Bomba 12V:** 1-2A, para riego real de invernadero

---

## ⚡ TABLA DE VOLTAJES Y CORRIENTES

| Componente | Voltaje | Corriente | Potencia |
|------------|---------|-----------|----------|
| ESP32 | 3.3V (lógica) / 5V (VIN) | 80-160mA | ~0.5W |
| DHT11 | 3.3V | 0.5-2.5mA | ~0.01W |
| Sensor Suelo | 3.3V | ~5mA | ~0.02W |
| Relé (bobina) | 5V | 15-20mA | ~0.1W |
| Bomba mini 5V | 5V | 100-300mA | 0.5-1.5W |
| Bomba 12V | 12V | 500-2000mA | 6-24W |

---

## 🛡️ CONSIDERACIONES DE SEGURIDAD

### ❗ IMPORTANTE - LEER ANTES DE CONECTAR

1. **Alimentación del ESP32:**
   - ✅ Usa USB 5V (máximo 500mA)
   - ✅ O fuente externa 5V en VIN (máximo 800mA)
   - ❌ NO conectes más de 5.5V a VIN
   - ❌ NO alimentes por 3.3V (pin de salida, no entrada)

2. **Pines GPIO:**
   - ✅ Voltaje máximo: 3.3V
   - ❌ NO conectes 5V directamente a GPIO
   - ❌ NO uses GPIO 6-11 (reservados para Flash)
   - ⚠️ GPIO 34-39 son solo INPUT (sin pull-up/down)

3. **Sensor de Humedad:**
   - ⚠️ NO dejes el sensor siempre encendido
   - ⚠️ Se oxida con el tiempo si está energizado
   - 💡 Solución: Conecta VCC a un GPIO y enciende solo al medir

4. **Módulo Relé:**
   - ✅ El relé aísla el circuito de potencia del ESP32
   - ✅ Puede manejar hasta 10A a 250V AC (según modelo)
   - ⚠️ Verifica la corriente máxima de tu relé
   - ❌ NO excedas la capacidad del relé

5. **Bomba de Agua:**
   - ✅ Si es 5V: puede alimentarse del USB
   - ⚠️ Si es 12V: necesita fuente externa
   - ⚠️ Conecta GND común entre ESP32 y fuente externa
   - ❌ NO alimentes bomba 12V desde el ESP32

6. **Protecciones Recomendadas:**
   - 💡 Diodo flyback (1N4007) en paralelo a la bomba
   - 💡 Condensador 100μF en VIN del ESP32
   - 💡 Fusible en serie con la bomba

---

## 🔍 VERIFICACIÓN DE CONEXIONES

### Checklist antes de conectar alimentación:

- [ ] DHT11 VCC → 3.3V (no 5V)
- [ ] DHT11 DATA → GPIO4
- [ ] DHT11 GND → GND
- [ ] Sensor Suelo VCC → 3.3V
- [ ] Sensor Suelo A0 → GPIO34
- [ ] Sensor Suelo GND → GND
- [ ] Relé VCC → VIN (5V)
- [ ] Relé IN1 → GPIO26
- [ ] Relé GND → GND
- [ ] Relé COM → negativo fuente bomba
- [ ] Relé NO → negativo bomba
- [ ] Bomba positivo → positivo fuente
- [ ] NO hay cortocircuitos
- [ ] Todos los GND están conectados entre sí

---

## 🎨 DIAGRAMA DE COLORES (Sugerencia)

Para facilitar el montaje, usa cables de colores:

| Color | Uso |
|-------|-----|
| 🔴 Rojo | VCC / Positivo (+) / 3.3V / 5V |
| ⚫ Negro | GND / Negativo (-) |
| 🟡 Amarillo | Señales GPIO (ej: GPIO4, GPIO26) |
| 🟢 Verde | Señales analógicas (ej: GPIO34) |
| 🔵 Azul | Señales I2C (SDA/SCL - futuro) |
| 🟠 Naranja | Señales UART (TX/RX - si usas) |

---

## 📸 FOTO DE REFERENCIA (Montaje sugerido)

```
Vista superior del montaje:

    ┌─────────────────────────────────────────┐
    │                                         │
    │    [DHT11]          [SENSOR SUELO]     │
    │      │                    │             │
    │      └─────┐       ┌──────┘             │
    │            │       │                    │
    │        ┌───┴───────┴────┐               │
    │        │                │               │
    │        │     ESP32      │──────────────┐│
    │        │                │              ││
    │        └────────────────┘              ││
    │              │                         ││
    │              │                         ││
    │        ┌─────┴─────┐                  ││
    │        │   RELÉ    │                  ││
    │        └─────┬─────┘                  ││
    │              │                        ││
    │        ┌─────┴─────┐                 ││
    │        │   BOMBA   │◄────────────────┘│
    │        └───────────┘                  │
    │                                        │
    └────────────────────────────────────────┘
```

---

## 📝 NOTAS FINALES

1. **Orden de conexión recomendado:**
   - Primero: Sensores (DHT11, Suelo)
   - Segundo: Módulo Relé
   - Tercero: Bomba al relé
   - Último: Alimentación del ESP32

2. **Prueba por etapas:**
   - Etapa 1: Solo sensores (sin relé ni bomba)
   - Etapa 2: Añadir relé (sin bomba)
   - Etapa 3: Añadir bomba

3. **Si algo no funciona:**
   - Desconecta alimentación
   - Revisa conexiones con un multímetro
   - Verifica continuidad de cables
   - Comprueba voltajes (3.3V, 5V, GND)

---

## ✅ ¡Todo listo!

Con este esquema deberías poder conectar todo correctamente.

**Recuerda:** ¡Siempre desconecta la alimentación antes de cambiar cables!

🌱 ¡Buena suerte con tu invernadero! 🤖
