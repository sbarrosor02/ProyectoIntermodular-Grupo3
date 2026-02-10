# 🌱 Invernadero Inteligente IoT
## Sistema de Monitoreo y Control Automatizado con ESP32

![Estado](https://img.shields.io/badge/Estado-Funcional-success)
![Versión](https://img.shields.io/badge/Versión-1.0-blue)
![Plataforma](https://img.shields.io/badge/Plataforma-ESP32-orange)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

---

## 📖 Descripción del Proyecto

Sistema IoT completo para el monitoreo y control automatizado de un invernadero mediante ESP32, con dashboard web responsive accesible desde cualquier dispositivo móvil o PC conectado a la misma red WiFi.

### 🎯 Objetivos
- Monitorizar temperatura y humedad ambiental en tiempo real
- Controlar humedad del suelo de forma automática
- Activar riego mediante bomba de agua cuando sea necesario
- Proporcionar interfaz web para control manual y visualización de datos
- Generar alertas cuando los parámetros estén fuera de rango

---

## ✨ Características Principales

### 🌡️ Monitoreo de Sensores
- **Temperatura ambiente** (0-50°C con precisión ±2°C)
- **Humedad del aire** (20-90% con precisión ±5%)
- **Humedad del suelo** (0-100% calibrable)
- Actualización de datos cada 2 segundos

### 💧 Control de Riego
- **Modo Automático:** Activa riego cuando humedad del suelo < 30%
- **Modo Manual:** Control directo desde el dashboard
- Riego temporizado (3 segundos por ciclo, configurable)
- Protección contra activaciones consecutivas

### 📱 Dashboard Web Responsive
- **Diseño Mobile-First** optimizado para smartphones
- **Totalmente responsivo** para tablets y PC
- **Gráficos históricos** con Chart.js (últimas 24 horas)
- **Sistema de alertas** inteligente y contextual
- **Actualización en tiempo real** sin necesidad de recargar
- **Indicadores visuales** con barras de progreso animadas

### 🔄 Comunicación
- **Servidor web** integrado en el ESP32
- **API REST** con endpoints JSON
- **CORS habilitado** para acceso desde cualquier origen
- **WebSocket-ready** (preparado para futuras mejoras)

---

## 🛠️ Componentes Necesarios

### Hardware
| Componente | Cantidad | Precio Aprox. |
|------------|----------|---------------|
| ESP32 DevKit v1 | 1 | 8€ |
| Sensor DHT11 | 1 | 2€ |
| Sensor Humedad Suelo | 1 | 3€ |
| Módulo Relé 1 canal | 1 | 2€ |
| Bomba de agua 5V | 1 | 5€ |
| Cables Dupont | 20 | 3€ |
| Protoboard | 1 | 3€ |
| Fuente USB 5V | 1 | 5€ |
| **TOTAL** | - | **~30€** |

### Software
- Arduino IDE 2.x
- Librerías: DHT sensor library, ArduinoJson
- Navegador web moderno (Chrome, Firefox, Safari, Edge)

---

## 📦 Estructura del Proyecto

```
invernadero-inteligente/
│
├── ESP32_Invernadero_Completo.ino    # Código Arduino para ESP32
├── dashboard-esp32-final.html         # Dashboard web avanzado
├── GUIA_INSTALACION.md                # Guía completa paso a paso
├── ESQUEMA_CONEXIONES.md              # Diagramas de conexión
└── README.md                          # Este archivo
```

---

## 🚀 Instalación Rápida

### Paso 1: Preparar el Hardware
1. Conecta los componentes siguiendo el **ESQUEMA_CONEXIONES.md**
2. Verifica que todas las conexiones estén correctas
3. Conecta el ESP32 al PC mediante USB

### Paso 2: Configurar Arduino IDE
1. Instala Arduino IDE 2.x
2. Añade soporte para ESP32:
   - `Archivo → Preferencias → URLs adicionales`
   - Pega: `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
3. Instala la placa: `Herramientas → Gestor de tarjetas → ESP32`
4. Instala librerías: `Programa → Administrar librerías`
   - DHT sensor library (Adafruit)
   - ArduinoJson

### Paso 3: Configurar y Subir el Código
1. Abre `ESP32_Invernadero_Completo.ino`
2. **MODIFICA estas líneas:**
   ```cpp
   const char* ssid = "TU_NOMBRE_WIFI";
   const char* password = "TU_CONTRASEÑA_WIFI";
   ```
3. Selecciona la placa: `Herramientas → Placa → ESP32 Dev Module`
4. Selecciona el puerto: `Herramientas → Puerto → COMx`
5. Haz clic en **Subir** (→)

### Paso 4: Obtener la IP del ESP32
1. Abre el Monitor Serie (`Ctrl + Shift + M`)
2. Velocidad: 115200 baudios
3. Busca la línea: `📍 Dirección IP: 192.168.x.xxx`
4. **Copia esa IP**

### Paso 5: Conectar el Dashboard
1. Abre `dashboard-esp32-final.html` en tu navegador
2. Ingresa la IP que copiaste
3. Haz clic en **"Conectar al ESP32"**
4. ✅ ¡Listo! Ya puedes monitorear y controlar tu invernadero

---

## 💻 Uso del Sistema

### Dashboard Web

#### Panel de Sensores
- 🌡️ **Temperatura:** Muestra temperatura actual con barra de progreso
- 💧 **Humedad Aire:** Porcentaje de humedad ambiental
- 🌱 **Humedad Suelo:** Nivel de agua en el sustrato

#### Panel de Control
- **Bomba de Agua:** Switch para activar/desactivar manualmente
- **Modo Automático:** El ESP32 controla el riego según humedad
- **Modo Manual:** Control total desde el dashboard

#### Sistema de Alertas
- ⚠️ **Temperatura alta** (>30°C): Recomienda ventilación
- 💧 **Suelo seco** (<30%): Sugiere activar riego
- 💨 **Humedad alta** (>80%): Alerta de riesgo de hongos

#### Gráfico Histórico
- Visualización de las últimas 24 horas
- Tres líneas: Temperatura, Humedad Aire, Humedad Suelo
- Actualización automática cada 2 segundos

---

## 🔌 API REST

El ESP32 expone los siguientes endpoints:

### GET /data
Devuelve datos actuales de todos los sensores

**Respuesta:**
```json
{
  "temperature": 25.5,
  "humidity": 65.0,
  "soil": 45,
  "pumpActive": false,
  "mode": "auto",
  "timestamp": 123456789
}
```

### POST /control
Envía comandos de control

**Cambiar modo:**
```json
{
  "command": "mode",
  "value": "manual"
}
```

**Controlar bomba (solo en modo manual):**
```json
{
  "command": "pump",
  "value": true
}
```

### GET /
Sirve dashboard HTML básico embebido en el ESP32

---

## ⚙️ Configuración Avanzada

### Ajustar Umbral de Riego
En `ESP32_Invernadero_Completo.ino`, línea 31:
```cpp
const int UMBRAL_SECO = 30;  // Cambia este valor (0-100)
```

### Ajustar Tiempo de Riego
Línea 32:
```cpp
const int TIEMPO_RIEGO = 3000;  // Milisegundos (3000 = 3 seg)
```

### Calibrar Sensor de Suelo
Línea 116:
```cpp
// Reemplaza 4095 y 1000 con tus valores calibrados
sensores.humedadSuelo = map(valorAnalogico, 4095, 1000, 0, 100);
//                                          ^^^^  ^^^^
//                                          SECO  HÚMEDO
```

**Cómo calibrar:**
1. Sensor al aire = VALOR_SECO (ej: 3800)
2. Sensor en agua = VALOR_HÚMEDO (ej: 1200)
3. Reemplaza en la función `map()`

---

## 🔧 Solución de Problemas

### ❌ No conecta al WiFi
**Síntomas:** En Monitor Serie aparece "Failed to connect"

**Soluciones:**
- Verifica nombre y contraseña del WiFi
- Asegúrate de que sea WiFi 2.4GHz (NO 5GHz)
- Acércate al router
- Reinicia el ESP32

### ❌ Sensor DHT11 devuelve NaN
**Síntomas:** Dashboard muestra "--°C" o "NaN"

**Soluciones:**
- Revisa conexiones: VCC → 3.3V, DATA → GPIO4, GND → GND
- Espera 2 segundos tras encender (tiempo de estabilización)
- Prueba con otro sensor DHT11

### ❌ Sensor de suelo siempre marca 0%
**Síntomas:** Valor constante en 0

**Soluciones:**
- Verifica que A0 esté en GPIO34
- Calibra el sensor (ver sección Configuración Avanzada)
- Comprueba alimentación (VCC → 3.3V)

### ❌ Relé no hace "clic"
**Síntomas:** Bomba no se activa

**Soluciones:**
- VCC del relé debe estar en VIN (5V), no en 3.3V
- Verifica que IN1 esté en GPIO26
- Algunos relés son "activos en LOW", invierte la lógica:
  ```cpp
  digitalWrite(RELAY_PIN, LOW);  // Encender
  digitalWrite(RELAY_PIN, HIGH); // Apagar
  ```

### ❌ Dashboard no carga en el móvil
**Síntomas:** Página no se abre

**Soluciones:**
- Móvil y ESP32 deben estar en la misma WiFi
- Desactiva datos móviles
- Usa http:// no https://
- Verifica IP en Monitor Serie
- Prueba primero desde PC

---

## 📊 Especificaciones Técnicas

### Consumo de Energía
- ESP32: 80-160mA @ 5V
- DHT11: 0.5-2.5mA @ 3.3V
- Sensor Suelo: ~5mA @ 3.3V
- Relé: 15-20mA @ 5V
- Bomba mini 5V: 100-300mA
- **Total:** ~200-500mA @ 5V

### Rango de Medición
- Temperatura: 0-50°C (±2°C)
- Humedad Aire: 20-90% (±5%)
- Humedad Suelo: 0-100% (calibrable)

### Conectividad
- WiFi 802.11 b/g/n (2.4GHz)
- Servidor HTTP en puerto 80
- API REST JSON

---

## 🔐 Seguridad

### Recomendaciones
- ✅ Cambia credenciales WiFi predeterminadas
- ✅ Usa solo en red local (no exponer a Internet)
- ✅ Añade autenticación si es necesario
- ⚠️ No uses en redes públicas

### Mejoras Futuras
- [ ] Autenticación por usuario/contraseña
- [ ] Cifrado HTTPS
- [ ] Control de acceso por IP
- [ ] Registro de eventos (logs)

---

## 🚀 Mejoras Futuras

### Hardware
- [ ] Pantalla OLED para datos sin WiFi
- [ ] Sensor de luz (LDR) para iluminación
- [ ] Sensor de nivel de agua en depósito
- [ ] Panel solar para autonomía energética
- [ ] Múltiples zonas de riego (usar 2º relé)

### Software
- [ ] Base de datos para históricos (SQLite, InfluxDB)
- [ ] Notificaciones por Telegram
- [ ] Integración con MQTT
- [ ] Machine Learning para predicción de riego
- [ ] Exportación de datos CSV/JSON

### Dashboard
- [ ] PWA (Progressive Web App)
- [ ] Modo oscuro
- [ ] Múltiples idiomas
- [ ] Estadísticas avanzadas
- [ ] Calendario de riego

---

## 📝 Notas del Desarrollador

### Decisiones de Diseño

**¿Por qué ESP32 y no Arduino?**
- ESP32 tiene WiFi integrado
- Mayor memoria RAM (520KB vs 2KB)
- Más GPIOs disponibles
- Precio similar

**¿Por qué servidor web en ESP32 y no aplicación externa?**
- Funciona sin Internet (solo WiFi local)
- Sin costos de hosting
- Acceso instantáneo desde cualquier dispositivo
- Fácil de demostrar y presentar

**¿Por qué HTML + JavaScript y no app nativa?**
- Compatible con todos los dispositivos
- No requiere instalación
- Fácil de actualizar
- Desarrollo más rápido

---

## 👥 Créditos

### Proyecto desarrollado para:
- Asignatura: Robótica Educativa IoT
- Nivel: Educación Secundaria / FP
- Año: 2026

### Componentes de:
- Microlog.es (proveedor de componentes electrónicos)

### Tecnologías utilizadas:
- ESP32 (Espressif)
- Arduino Framework
- Chart.js (gráficos)
- Tailwind CSS (diseño)

---

## 📄 Licencia

MIT License - Uso libre para proyectos educativos

---

## 📞 Soporte

### Documentación
- [Arduino ESP32](https://docs.espressif.com/projects/arduino-esp32/)
- [Sensor DHT11](https://learn.adafruit.com/dht)
- [ArduinoJson](https://arduinojson.org/)

### Comunidades
- [ESP32 Forum](https://esp32.com/)
- [Arduino Forum](https://forum.arduino.cc/)
- [Reddit r/esp32](https://reddit.com/r/esp32)

---

## ✅ Checklist de Presentación

Antes de presentar tu proyecto, verifica:

### Hardware
- [ ] Todos los componentes conectados correctamente
- [ ] Cable USB conectado y alimentando el ESP32
- [ ] LED azul del ESP32 parpadeando (indica WiFi activo)
- [ ] Relé hace "clic" al activar bomba
- [ ] Bomba funciona correctamente

### Software
- [ ] ESP32 conectado al WiFi (verificar en Monitor Serie)
- [ ] IP del ESP32 anotada y accesible
- [ ] Dashboard HTML funciona en PC
- [ ] Dashboard accesible desde móvil
- [ ] Datos se actualizan en tiempo real
- [ ] Modo automático funciona
- [ ] Modo manual funciona
- [ ] Gráfico se actualiza

### Presentación
- [ ] Demo preparada (script de qué mostrar)
- [ ] Backup del código en USB
- [ ] Capturas de pantalla del dashboard
- [ ] Video de funcionamiento (opcional)
- [ ] Esquema de conexiones impreso
- [ ] Presupuesto detallado

---

## 🎉 ¡Proyecto Finalizado!

Tu **Invernadero Inteligente IoT** está completo y listo para funcionar en el mundo real.

**Características destacadas:**
- ✅ Monitoreo en tiempo real
- ✅ Control remoto desde móvil
- ✅ Riego automático inteligente
- ✅ Dashboard profesional responsive
- ✅ Alertas contextuales
- ✅ Gráficos históricos

**Presupuesto total:** ~30-35€  
**Tiempo de montaje:** 2-3 horas  
**Dificultad:** Media  

---

### 📸 Comparte tu Proyecto

Si construyes este proyecto, etiquétanos:
- GitHub: #InvernaderoIoT #ESP32 #Arduino
- Twitter/X: @TuUsuario
- Instagram: @TuUsuario

---

**Hecho con 💚 para la educación en IoT y robótica**

🌱 ¡Cultivando el futuro con tecnología! 🤖
