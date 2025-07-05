import subprocess
import time
import requests

# Lista de MACs conocidas
macs_conocidas = ['AA:BB:CC:DD:EE:FF', '11:22:33:44:55:66']
TOKEN = 'TU_TOKEN_TELEGRAM'
CHAT_ID = 'TU_CHAT_ID'

def escanear_dispositivos():
    resultado = subprocess.getoutput("hcitool scan")
    encontrados = []
    for mac in macs_conocidas:
        if mac in resultado:
            encontrados.append(mac)
    return encontrados

def enviar_mensaje(mac):
    mensaje = f"🔔 Dispositivo detectado: {mac}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mensaje}"
    requests.get(url)

if __name__ == "__main__":
    print("🟢 Iniciando escaneo Bluetooth...")
    while True:
        encontrados = escanear_dispositivos()
        for mac in encontrados:
            enviar_mensaje(mac)
        time.sleep(60)  # Esperar 1 minuto entre escaneos
