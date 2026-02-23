import serial
import json
import time
import threading
from flask import Flask, jsonify, render_template_string, request

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

# Puerto serie compartido entre hilos
arduino = None
serial_lock = threading.Lock()


def hilo_lectura_arduino():
    global datos, arduino
    print(f"📡 Iniciando comunicación con Arduino en {PORT}...")
    try:
        arduino = serial.Serial(PORT, BAUD, timeout=1)
        arduino.flush()
        while True:
            with serial_lock:
                if arduino.in_waiting > 0:
                    linea = arduino.readline().decode('utf-8', errors='ignore').strip()

                    if linea.startswith('{'):
                        try:
                            json_data = json.loads(linea)
                            datos.update(json_data)
                            datos["last_update"] = time.strftime("%H:%M:%S")
                        except json.JSONDecodeError:
                            pass
                    elif "---" not in linea and len(linea) > 2:
                        print(f"  [Arduino]: {linea}")
            time.sleep(0.01)
    except Exception as e:
        print(f"❌ Error en hilo serie: {e}")


@app.route('/api/data')
def get_data():
    return jsonify(datos)


@app.route('/api/cmd', methods=['POST'])
def send_cmd():
    """Envía un comando JSON al Arduino por el puerto serie."""
    body = request.get_json(silent=True)
    if not body or 'cmd' not in body:
        return jsonify({"ok": False, "error": "Falta el campo 'cmd'"}), 400

    cmd = body['cmd']
    if arduino is None or not arduino.is_open:
        return jsonify({"ok": False, "error": "Arduino no conectado"}), 503

    try:
        with serial_lock:
            mensaje = json.dumps({"cmd": cmd}) + "\n"
            arduino.write(mensaje.encode('utf-8'))
        return jsonify({"ok": True, "cmd": cmd})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


@app.route('/')
def dashboard():
    return render_template_string('''
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Dashboard Invernadero</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        :root { --p: #2d5a27; --s: #4a7c62; --bg: #f0f4f0; }
        body { font-family: "Segoe UI", sans-serif; background: var(--bg); margin: 0; padding: 20px; color: #333; }
        .container { max-width: 900px; margin: 0 auto; }
        .header { background: linear-gradient(135deg, var(--p), var(--s)); color: white; padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 20px; }
        .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
        .val { font-size: 2.5em; font-weight: bold; color: var(--p); margin: 10px 0; }
        .status { padding: 15px; border-radius: 10px; background: #fff; border-left: 5px solid var(--s); margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
        .badge { padding: 5px 12px; border-radius: 5px; font-weight: bold; font-size: 0.85em; }
        .on  { background: #dcfce7; color: #166534; }
        .off { background: #fee2e2; color: #991b1b; }

        /* Panel de control */
        .controls { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        .btn { padding: 12px 20px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 1em; transition: opacity 0.2s; }
        .btn:hover { opacity: 0.85; }
        .btn:active { opacity: 0.7; }
        .btn-auto   { background: #10b981; color: white; }
        .btn-manual { background: #3b82f6; color: white; }
        .btn-on     { background: #f59e0b; color: white; }
        .btn-off    { background: #6b7280; color: white; }
        .btn-row    { display: flex; gap: 10px; justify-content: center; margin-top: 12px; }
        .feedback   { font-size: 0.8em; color: #666; margin-top: 8px; min-height: 18px; }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>🌱 Invernadero Inteligente</h1>
        <p>Monitoreo y Control | Puerto: ''' + PORT + '''</p>
    </div>

    <!-- Sensores -->
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

    <!-- Estado del sistema -->
    <div class="status">
        <strong>Estado:</strong>&nbsp;
        Bomba: <span id="pump" class="badge">--</span>&nbsp;&nbsp;
        Modo: <span id="auto" class="badge">--</span>&nbsp;&nbsp;
        Última señal: <span id="time">--</span>
    </div>

    <!-- Panel de control -->
    <div class="controls">
        <div class="card">
            <h3>⚙️ Modo de operación</h3>
            <div class="btn-row">
                <button class="btn btn-auto"   onclick="cmd('mode_auto')">🤖 Automático</button>
                <button class="btn btn-manual" onclick="cmd('mode_man')">👆 Manual</button>
            </div>
            <div class="feedback" id="fb-mode"></div>
        </div>
        <div class="card">
            <h3>💦 Control de Bomba</h3>
            <p style="font-size:0.85em;color:#666;margin:0">(Solo disponible en modo Manual)</p>
            <div class="btn-row">
                <button class="btn btn-on"  onclick="cmd('pump_on')">Encender</button>
                <button class="btn btn-off" onclick="cmd('pump_off')">Apagar</button>
            </div>
            <div class="feedback" id="fb-pump"></div>
        </div>
    </div>
</div>

<script>
    function update() {
        fetch('/api/data')
            .then(r => r.json())
            .then(d => {
                document.getElementById('temp').innerText  = d.temp.toFixed(1) + "°C";
                document.getElementById('hum').innerText   = d.hum.toFixed(1) + "%";
                document.getElementById('soil').innerText  = d.soil + "%";

                const p = document.getElementById('pump');
                p.innerText   = d.pump ? "ENCENDIDA" : "APAGADA";
                p.className   = "badge " + (d.pump ? "on" : "off");

                const a = document.getElementById('auto');
                a.innerText   = d.auto ? "AUTOMÁTICO" : "MANUAL";
                a.className   = "badge " + (d.auto ? "on" : "off");

                document.getElementById('time').innerText = d.last_update;
            })
            .catch(() => {});
    }

    function cmd(command) {
        const fbEl = command.startsWith('pump') ? 'fb-pump' : 'fb-mode';
        document.getElementById(fbEl).innerText = "Enviando...";

        fetch('/api/cmd', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cmd: command })
        })
        .then(r => r.json())
        .then(data => {
            document.getElementById(fbEl).innerText = data.ok ? "✅ Enviado" : "❌ " + data.error;
            setTimeout(() => { document.getElementById(fbEl).innerText = ""; }, 2000);
        })
        .catch(() => {
            document.getElementById(fbEl).innerText = "❌ Error de red";
        });
    }

    setInterval(update, 1000);
    update();
</script>
</body>
</html>
''')


if __name__ == '__main__':
    t = threading.Thread(target=hilo_lectura_arduino, daemon=True)
    t.start()

    print("🚀 Dashboard disponible en: http://localhost:5000")
    app.run(port=5000, debug=False, use_reloader=False)
