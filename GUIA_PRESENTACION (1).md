# 🎤 GUÍA DE PRESENTACIÓN DEL PROYECTO
## Invernadero Inteligente IoT - Script para Exposición

---

## ⏱️ ESTRUCTURA DE LA PRESENTACIÓN (15-20 minutos)

### 1. INTRODUCCIÓN (2 minutos)
### 2. PROBLEMA Y SOLUCIÓN (3 minutos)
### 3. DEMOSTRACIÓN EN VIVO (8 minutos)
### 4. ASPECTOS TÉCNICOS (4 minutos)
### 5. CONCLUSIONES Y MEJORAS (3 minutos)

---

## 📝 GUIÓN DETALLADO

### 1️⃣ INTRODUCCIÓN (2 min)

**[DIAPOSITIVA 1: Título del Proyecto]**

"Buenos días/tardes. Hoy les voy a presentar nuestro proyecto de **Invernadero Inteligente IoT**, un sistema automatizado para el control y monitoreo de condiciones ambientales en un invernadero utilizando tecnología ESP32."

**Presentación del equipo:**
- "Mi nombre es [Tu Nombre]"
- "He desarrollado este proyecto para la asignatura de Robótica Educativa IoT"

**Contexto:**
- "El proyecto surge de la necesidad de optimizar el riego y cuidado de plantas"
- "Especialmente útil cuando no podemos estar presentes físicamente"
- "Combina hardware, programación y diseño web"

---

### 2️⃣ PROBLEMA Y SOLUCIÓN (3 min)

**[DIAPOSITIVA 2: El Problema]**

"**El problema que queremos resolver es:**"

❌ Riego manual requiere presencia constante  
❌ Difícil saber cuándo una planta necesita agua  
❌ Riesgo de sobre-riego o sub-riego  
❌ Falta de datos históricos sobre condiciones  
❌ No podemos controlar el invernadero remotamente  

**[DIAPOSITIVA 3: Nuestra Solución]**

"**Hemos desarrollado un sistema que:**"

✅ Monitorea temperatura, humedad ambiental y del suelo 24/7  
✅ Activa el riego automáticamente cuando es necesario  
✅ Permite control remoto desde móvil o PC  
✅ Genera alertas cuando algo va mal  
✅ Guarda histórico de datos en gráficos  

**[DIAPOSITIVA 4: Arquitectura del Sistema]**

"El sistema se compone de 3 elementos principales:"

1. **Hardware IoT:** ESP32 + Sensores + Relé + Bomba
2. **Software Embebido:** Código Arduino en el ESP32
3. **Dashboard Web:** Interfaz responsive para control

---

### 3️⃣ DEMOSTRACIÓN EN VIVO (8 min)

**[MOSTRAR EL HARDWARE FÍSICO]**

"Primero, déjenme mostrarles el hardware que hemos montado."

**Señala cada componente:**

🔵 **ESP32:** "Este es el cerebro del sistema. Un microcontrolador con WiFi integrado que cuesta unos 8€"

🌡️ **Sensor DHT11:** "Este sensor mide temperatura y humedad del aire"

🌱 **Sensor de Suelo:** "Este sensor se inserta en la tierra y mide la humedad del sustrato"

⚡ **Módulo Relé:** "Este relé actúa como un interruptor electrónico para controlar la bomba"

💧 **Bomba de Agua:** "Y esta bomba de 5V se encarga del riego"

---

**[ABRIR MONITOR SERIE]**

"Ahora voy a conectar el ESP32 y mostrarles cómo se conecta al WiFi."

[Conectar ESP32 al PC]

```
Monitor Serie muestra:
========================================
🌱 INVERNADERO INTELIGENTE - ESP32
========================================
✓ Sensor DHT11 inicializado
📡 Conectando a WiFi...
✓ WiFi conectado!
📍 Dirección IP: 192.168.1.100
✓ Servidor web iniciado
```

"Como pueden ver, el ESP32 se ha conectado exitosamente al WiFi y nos da una dirección IP: **192.168.1.100**"

"En el Monitor Serie también podemos ver las lecturas de los sensores en tiempo real:"

```
--- LECTURA DE SENSORES ---
🌡️  Temperatura: 24.5 °C
💧 Humedad Aire: 62.3 %
🌱 Humedad Suelo: 45 %
💦 Bomba: APAGADA
🤖 Modo: auto
```

---

**[ABRIR EL DASHBOARD EN EL MÓVIL]**

"Ahora, desde mi móvil, voy a acceder al dashboard web."

[Mostrar móvil a la cámara/audiencia]

1. "Abro el navegador"
2. "Ingreso la IP del ESP32: http://192.168.1.100"
3. "Y como pueden ver, tenemos nuestra interfaz funcionando"

**[IR RECORRIENDO EL DASHBOARD]**

📊 **Panel de Sensores:**
"Aquí arriba tenemos tres tarjetas que muestran los datos en tiempo real:"
- "Temperatura actual: 24.5°C - Estado: Óptimo"
- "Humedad del aire: 62% - Estado: Óptimo"
- "Humedad del suelo: 45% - Estado: Óptimo"

"Estas barras de progreso se actualizan automáticamente cada 2 segundos"

---

⚙️ **Panel de Control:**

"Aquí tenemos el panel de control con dos modos de operación:"

**a) Modo Automático:**
[Asegurarse de estar en modo auto]

"En modo automático, el ESP32 toma las decisiones. Si la humedad del suelo baja del 30%, el sistema activa la bomba automáticamente durante 3 segundos."

[Simular suelo seco: sacar el sensor de la tierra o secarlo]

"Voy a sacar el sensor de la tierra para simular un suelo seco..."

[Esperar a que baje < 30%]

"¡Miren! La humedad ha bajado a 28%... y... ¡el sistema ha activado la bomba automáticamente!"

[Se escucha el "clic" del relé y la bomba se enciende]

"Pueden escuchar el relé activándose y ver cómo la bomba funciona durante 3 segundos."

[Esperar 3 segundos]

"Y ahora se apaga automáticamente. Esto pasaría en un invernadero real cada vez que la tierra esté seca."

---

**b) Modo Manual:**
[Cambiar a modo manual]

"Ahora voy a cambiar a modo manual. En este modo, **yo tengo el control total** desde el dashboard."

[Hacer clic en el botón "Modo Manual"]

"Como pueden ver, el botón cambió de color indicando que estamos en modo manual."

[Activar la bomba manualmente]

"Ahora puedo activar la bomba con este switch..."

[Hacer clic en el switch de la bomba]

"¡Y funciona! La bomba se enciende a demanda."

[Desactivar la bomba]

"Y la apago cuando quiera."

"Esto es útil si quiero regar manualmente desde cualquier parte de mi casa o desde el jardín."

---

⚠️ **Sistema de Alertas:**

[Provocar una alerta: calentar el sensor DHT11 con las manos o una lámpara]

"El sistema también tiene alertas inteligentes. Si algún parámetro está fuera de rango, aparece una notificación."

[Esperar a que la temperatura suba >30°C]

"¡Miren! La temperatura ha subido a 31°C y apareció una alerta:"

"⚠️ **Temperatura Elevada** - 31°C - Se recomienda activar ventilación"

"Esto nos permite reaccionar rápidamente ante problemas."

---

📈 **Gráfico Histórico:**

[Hacer scroll hasta el gráfico]

"Por último, tenemos un gráfico que muestra la evolución de los tres parámetros en las últimas 24 horas."

"Esto es muy útil para:"
- "Ver patrones de comportamiento"
- "Detectar anomalías"
- "Tomar decisiones basadas en datos"

"Este gráfico se actualiza en tiempo real conforme el sistema recibe nuevas lecturas."

---

### 4️⃣ ASPECTOS TÉCNICOS (4 min)

**[DIAPOSITIVA 5: Componentes y Presupuesto]**

"Hablemos un poco de los aspectos técnicos del proyecto."

**Hardware Utilizado:**

| Componente | Precio |
|------------|--------|
| ESP32 DevKit | 8€ |
| Sensor DHT11 | 2€ |
| Sensor Humedad Suelo | 3€ |
| Módulo Relé | 2€ |
| Bomba 5V | 5€ |
| Cables y accesorios | 10€ |
| **TOTAL** | **30€** |

"Todo el proyecto cuesta aproximadamente **30 euros**, haciéndolo muy accesible."

---

**[DIAPOSITIVA 6: Conexiones]**

"Las conexiones son relativamente sencillas:"

```
ESP32          Componente
─────          ──────────
GPIO4    ───→  DHT11 (DATA)
GPIO34   ───→  Sensor Suelo (A0)
GPIO26   ───→  Relé (IN1)
3.3V     ───→  Sensores (VCC)
VIN      ───→  Relé (VCC)
GND      ───→  Todos (GND)
```

"He documentado todo en un diagrama detallado que está en el repositorio."

---

**[DIAPOSITIVA 7: Software]**

"En cuanto al software, el proyecto se divide en dos partes:"

**1. Código ESP32 (Arduino C++):**
- Lee sensores cada 2 segundos
- Controla el relé de la bomba
- Implementa lógica de riego automático
- Crea un servidor web HTTP
- Expone API REST en JSON

**2. Dashboard Web (HTML/CSS/JS):**
- Interfaz responsive (mobile-first)
- Consume API del ESP32 vía fetch()
- Gráficos con Chart.js
- Actualización en tiempo real
- Sin backend externo (todo local)

**Librerías utilizadas:**
- DHT sensor library (Adafruit)
- ArduinoJson
- Chart.js

---

**[DIAPOSITIVA 8: Arquitectura de Comunicación]**

"La comunicación funciona así:"

```
┌─────────┐     WiFi      ┌─────────┐
│Dashboard│ ◄──────────► │  ESP32  │
│  (Web)  │   HTTP/JSON   │ (Server)│
└─────────┘               └────┬────┘
                               │
                    ┌──────────┼──────────┐
                    │          │          │
                ┌───▼───┐  ┌───▼───┐  ┌───▼───┐
                │ DHT11 │  │ Suelo │  │ Relé  │
                └───────┘  └───────┘  └───┬───┘
                                          │
                                      ┌───▼───┐
                                      │ Bomba │
                                      └───────┘
```

**Endpoints de la API:**

1. `GET /data` → Devuelve datos de sensores
2. `POST /control` → Recibe comandos
3. `GET /` → Sirve dashboard HTML

---

### 5️⃣ CONCLUSIONES Y MEJORAS (3 min)

**[DIAPOSITIVA 9: Logros]**

"**¿Qué hemos conseguido?**"

✅ Sistema IoT funcional 100% operativo  
✅ Monitoreo en tiempo real desde cualquier dispositivo  
✅ Control remoto a través de WiFi  
✅ Riego automático inteligente  
✅ Dashboard profesional y responsive  
✅ Proyecto económico (~30€)  
✅ Documentación completa  

---

**[DIAPOSITIVA 10: Aprendizajes]**

"**¿Qué hemos aprendido?**"

📚 **Hardware:**
- Conexión y lectura de sensores analógicos y digitales
- Control de actuadores mediante relés
- Alimentación y gestión de energía

💻 **Programación:**
- Desarrollo en Arduino (C++)
- Creación de servidores web embebidos
- APIs REST y formato JSON
- JavaScript y manipulación del DOM

🌐 **Redes:**
- Protocolos HTTP
- Comunicación cliente-servidor
- Configuración de WiFi en ESP32

🎨 **Diseño:**
- Interfaces responsive
- UX/UI para dashboards
- Visualización de datos

---

**[DIAPOSITIVA 11: Mejoras Futuras]**

"**Posibles mejoras y ampliaciones:**"

🔮 **Hardware:**
- Pantalla OLED para datos sin WiFi
- Sensor de luz para iluminación automática
- Sensor de nivel de agua en depósito
- Panel solar para autonomía energética
- Múltiples zonas de riego

🔮 **Software:**
- Base de datos para históricos largos
- Notificaciones por Telegram/Email
- Integración con MQTT
- Machine Learning para predicción
- Control por voz (Alexa/Google)

🔮 **Dashboard:**
- Progressive Web App (PWA)
- Modo oscuro
- Múltiples idiomas
- Estadísticas avanzadas
- Exportación de datos

---

**[DIAPOSITIVA 12: Aplicaciones Reales]**

"**¿Dónde se puede usar esto?**"

🏡 **Hogar:**
- Jardines y huertos urbanos
- Cuidado de plantas de interior
- Invernaderos caseros

🏫 **Educación:**
- Proyectos de ciencias
- Aprendizaje de IoT
- Huertos escolares

🌾 **Agricultura:**
- Invernaderos profesionales (escalable)
- Cultivos hidropónicos
- Viveros

---

**[DIAPOSITIVA 13: Conclusión Final]**

"**Para concluir:**"

"Hemos desarrollado un sistema IoT completo que resuelve un problema real de forma eficiente y económica."

"El proyecto demuestra cómo la tecnología puede ayudarnos a optimizar tareas cotidianas y cuidar mejor de nuestras plantas."

"Todo el código y documentación está disponible y es open source, para que cualquiera pueda replicarlo o mejorarlo."

"**Presupuesto:** 30€  
**Tiempo:** 2-3 horas de montaje  
**Resultado:** Sistema profesional y funcional"

---

**"¿Tienen alguna pregunta?"**

---

## ❓ PREGUNTAS FRECUENTES Y RESPUESTAS

### P1: ¿Por qué elegiste ESP32 y no Arduino?
**R:** "El ESP32 tiene WiFi integrado, más memoria RAM (520KB vs 2KB del Arduino UNO), más pines GPIO y un precio similar. Esto lo hace ideal para proyectos IoT sin necesidad de módulos adicionales."

### P2: ¿Funciona sin Internet?
**R:** "Sí, solo necesita una red WiFi local. No requiere conexión a Internet. El ESP32 crea su propio servidor web y el móvil se conecta directamente a él."

### P3: ¿Cuánto tiempo puede funcionar desatendido?
**R:** "Con la configuración actual, puede funcionar indefinidamente mientras tenga alimentación. Lo único que limita es el depósito de agua. Con un depósito de 5 litros y riegos de 3 segundos cada vez que se necesita, podría durar semanas."

### P4: ¿Qué pasa si se va la luz?
**R:** "El sistema se apaga, pero al volver la luz, el ESP32 se reinicia automáticamente y vuelve a funcionar. No pierde la configuración. Como mejora futura, se podría añadir una batería de respaldo."

### P5: ¿Se pueden controlar varias zonas?
**R:** "Sí, el ESP32 tiene muchos pines GPIO. Con el hardware actual tenemos un relé, pero se pueden añadir hasta 5-6 relés más para controlar diferentes zonas, ventiladores, luces, etc."

### P6: ¿Los datos se pierden al reiniciar?
**R:** "Los datos en el gráfico sí se pierden al reiniciar el ESP32, ya que están en memoria RAM. Como mejora futura, se puede añadir una tarjeta SD o enviar datos a una base de datos externa."

### P7: ¿Es seguro dejarlo funcionando solo?
**R:** "Sí, pero con precauciones: usar fuentes de alimentación adecuadas, verificar que las conexiones estén bien aisladas, no dejar cables sueltos y tener un depósito de agua con flotador para evitar desbordamientos."

### P8: ¿Cuánto consume de electricidad?
**R:** "El consumo es muy bajo: aproximadamente 0.5W en reposo y 2-3W cuando activa la bomba. Funcionando 24/7 durante un mes, consumiría unos 0.36 kWh, lo que equivale a unos 6 céntimos de euro."

### P9: ¿Se puede adaptar para otros tipos de cultivos?
**R:** "Totalmente. Solo hay que ajustar el umbral de riego según el tipo de planta. Por ejemplo, cactus necesitan <20% humedad, mientras que helechos necesitan >60%. Se cambia en el código en 1 minuto."

### P10: ¿Qué has aprendido de este proyecto?
**R:** "He aprendido a integrar hardware y software, diseñar APIs, crear interfaces responsive, gestionar sensores, controlar actuadores y sobre todo, a resolver problemas reales con tecnología. También he mejorado mucho en debugging y documentación."

---

## 💡 TIPS PARA LA PRESENTACIÓN

### Antes de Presentar:
- [ ] Carga completamente el móvil
- [ ] Prueba todo el sistema 30 minutos antes
- [ ] Ten una red WiFi estable (idealmente un hotspot en tu móvil)
- [ ] Lleva cables USB de repaldo
- [ ] Ten capturas de pantalla por si algo falla
- [ ] Prepara un vídeo demo de respaldo
- [ ] Imprime el esquema de conexiones
- [ ] Lleva el código impreso (por si piden verlo)

### Durante la Presentación:
- ✅ Habla claro y pausado
- ✅ Mantén contacto visual con la audiencia
- ✅ Usa las manos para señalar componentes
- ✅ No leas las diapositivas, úsalas de apoyo
- ✅ Muestra entusiasmo por tu proyecto
- ✅ Si algo falla, mantén la calma
- ✅ Explica problemas que tuviste y cómo los resolviste

### Lenguaje Corporal:
- 👍 Postura erguida y relajada
- 👍 Manos visibles (no en bolsillos)
- 👍 Sonreír cuando corresponda
- 👍 Moverte por el espacio (no estático)
- 👍 Gestos naturales
- 👍 Respirar profundo si te pones nervioso

---

## 🎬 CHECKLIST FINAL DEL DÍA DE LA PRESENTACIÓN

### Material:
- [ ] ESP32 con código cargado
- [ ] Sensores conectados y funcionando
- [ ] Relé y bomba operativos
- [ ] Cable USB
- [ ] Móvil cargado con dashboard abierto
- [ ] PC portátil de respaldo
- [ ] Diapositivas listas
- [ ] Documentación impresa

### Configuración:
- [ ] WiFi configurado (hotspot si es necesario)
- [ ] IP del ESP32 anotada
- [ ] Dashboard funcionando
- [ ] Monitor Serie listo

### Prueba Final (10 min antes):
- [ ] Conectar ESP32
- [ ] Verificar conexión WiFi
- [ ] Abrir dashboard en móvil
- [ ] Probar modo automático
- [ ] Probar modo manual
- [ ] Verificar que sensores leen correctamente
- [ ] Comprobar que el relé funciona

---

## 🏆 CRITERIOS DE EVALUACIÓN TÍPICOS

| Criterio | Peso | Qué evalúa |
|----------|------|------------|
| **Funcionalidad** | 30% | ¿El proyecto funciona correctamente? |
| **Documentación** | 20% | ¿Está bien documentado? |
| **Presentación** | 20% | ¿Se explica claramente? |
| **Creatividad** | 15% | ¿Tiene elementos innovadores? |
| **Complejidad Técnica** | 15% | ¿Demuestra conocimientos avanzados? |

---

## 🎯 MENSAJES CLAVE PARA RECORDAR

1. **"Es un sistema IoT completo y funcional"**
2. **"Resuelve un problema real con tecnología accesible"**
3. **"Todo por solo 30 euros"**
4. **"Funciona desde cualquier dispositivo móvil"**
5. **"Es escalable y mejorable"**

---

## 📹 ESTRUCTURA DEL VÍDEO DEMO (Si lo grabas)

1. **Intro (10 seg):** Título y nombre
2. **Hardware (30 seg):** Mostrar componentes
3. **Conexión (20 seg):** ESP32 conectándose al WiFi
4. **Dashboard (60 seg):** Recorrer la interfaz
5. **Modo Auto (30 seg):** Demostrar riego automático
6. **Modo Manual (20 seg):** Control desde móvil
7. **Alertas (20 seg):** Mostrar notificación
8. **Gráfico (15 seg):** Histórico de datos
9. **Conclusión (15 seg):** Mensaje final

**Duración total:** ~3.5 minutos

---

## ✅ ¡ÉXITO EN TU PRESENTACIÓN!

Recuerda:
- Has hecho un **trabajo excelente**
- Tu proyecto es **profesional y funcional**
- Tienes todo **bien documentado**
- Conoces tu proyecto **de arriba a abajo**
- Estás **preparado para cualquier pregunta**

**¡MUCHA SUERTE! 🌱🤖**

---

*"La mejor manera de predecir el futuro es crearlo." - Alan Kay*
