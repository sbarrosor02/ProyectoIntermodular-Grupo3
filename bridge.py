import serial
import json
import time
import threading
from flask import Flask, jsonify, render_template_string

# --- CONFIGURACIÓN ---
PORT = 'COM3'  # 👈 CAMBIA ESTO por tu puerto
BAUD = 9600
app = Flask(__name__)

# Almacén de datos global
datos = {
    "temp": 0.0,
    "hum": 0.0,
    "soil": 0,
    "pump": False,
    "auto": True,
    "last_update": "Esperando datos..."
}

def hilo_lectura_arduino():
    global datos
    print(f"📡 Iniciando comunicación con Arduino en {PORT}...")
    try:
        with serial.Serial(PORT, BAUD, timeout=1) as ser:
            # Limpiar buffer inicial
            ser.flush()
            while True:
                if ser.in_waiting > 0:
                    linea = ser.readline().decode('utf-8', errors='ignore').strip()
                    
                    # Si es JSON, actualizamos el diccionario global
                    if linea.startswith('{'):
                        try:
                            json_data = json.loads(linea)
                            datos.update(json_data)
                            datos["last_update"] = time.strftime("%H:%M:%S")
                        except json.JSONDecodeError:
                            pass
                    # Si es texto, lo mostramos en la consola de Python (debug)
                    elif "---" not in linea and len(linea) > 2:
                        print(f"  [Arduino]: {linea}")
                time.sleep(0.01)
    except Exception as e:
        print(f"❌ Error en hilo serie: {e}")

@app.route('/api/data')
def get_data():
    return jsonify(datos)

@app.route('/')
def dashboard():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard Invernadero</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        :root { --p: #2d5a27; --s: #4a7c62; --bg: #f0f4f0; }
        body { font-family: 'Segoe UI', sans-serif; background: var(--bg); margin: 0; padding: 20px; color: #333; }
        .container { max-width: 800px; margin: 0 auto; }
        .header { background: var(--p); color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }
        .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
        .val { font-size: 2.5em; font-weight: bold; color: var(--p); margin: 10px 0; }
        .status { margin-top: 20px; padding: 15px; border-radius: 10px; background: #fff; border-left: 5px solid var(--s); }
        .badge { padding: 5px 10px; border-radius: 5px; font-weight: bold; font-size: 0.8em; }
        .on { background: #dcfce7; color: #166534; }
        .off { background: #fee2e2; color: #991b1b; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌱 Invernadero Inteligente</h1>
            <p>Monitoreo vía Python Bridge | Puerto: ''' + PORT + '''</p>
        </div>
        
        <div class="grid">
            <div class="card">
                <div>🌡️ Temperatura</div>
                <div class="val" id="temp">--°C</div>
            </div>
            <div class="card">
                <div>💧 Humedad Aire</div>
                <div class="val" id="hum">--%</div>
            </div>
            <div class="card">
                <div>🌱 Humedad Suelo</div>
                <div class="val" id="soil">--%</div>
            </div>
        </div>

        <div class="status">
            <strong>Estado del Sistema:</strong><br><br>
            Bomba: <span id="pump" class="badge">--</span> | 
            Modo: <span id="auto" class="badge">--</span> | 
            Última señal: <span id="time">--</span>
        </div>
    </div>

    <script>
        function update() {
            fetch('/api/data')
                .then(res => res.json())
                .then(d => {
                    document.getElementById('temp').innerText = d.temp.toFixed(1) + "°C";
                    document.getElementById('hum').innerText = d.hum.toFixed(1) + "%";
                    document.getElementById('soil').innerText = d.soil + "%";
                    
                    const p = document.getElementById('pump');
                    p.innerText = d.pump ? "ENCENDIDA" : "APAGADA";
                    p.className = "badge " + (d.pump ? "on" : "off");
                    
                    const a = document.getElementById('auto');
                    a.innerText = d.auto ? "AUTOMÁTICO" : "MANUAL";
                    a.className = "badge " + (d.auto ? "on" : "off");
                    
                    document.getElementById('time').innerText = d.last_update;
                });
        }
        setInterval(update, 1000);
        update();
    </script>
</body>
</html>
''')

if __name__ == '__main__':
    # Lanzar hilo de lectura serie
    t = threading.Thread(target=hilo_lectura_arduino, daemon=True)
    t.start()
    
    # Lanzar servidor Flask
    print("🚀 Dashboard disponible en: http://localhost:5000")
    app.run(port=5000, debug=False, use_reloader=False)
