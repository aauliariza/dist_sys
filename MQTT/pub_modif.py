"""
Publisher MQTT - Data GPS
Mengirim koordinat GPS (latitude, longitude) setiap 2 detik
"""

import paho.mqtt.client as mqtt
import time
import sys

# Konfigurasi broker
BROKER = "mqtt-broker"
PORT = 1883
TOPIC = "sister/gps"

# Callback ketika terkoneksi ke broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[Publisher] Terhubung ke broker MQTT {BROKER}")
    else:
        print(f"[Publisher] Gagal terhubung, kode error: {rc}")
        sys.exit(1)

def main():
    # Inisialisasi klien
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect

    # Hubungkan ke broker
    try:
        print(f"Menghubungkan ke {BROKER}...")
        client.connect(BROKER, PORT, keepalive=60)
    except Exception as e:
        print(f"Gagal menghubungkan ke broker: {e}")
        sys.exit(1)

    # Simulasi koordinat GPS (bergerak ke timur)
    latitude = -6.2000   # Contoh: Jakarta
    longitude = 106.8166

    try:
        while True:
            message = f"Lat: {latitude:.4f}, Lon: {longitude:.4f}"
            client.publish(TOPIC, message)
            print(f"[Publisher] Published: {message}")

            # Update koordinat simulasi (bergerak ke timur +0.0005)
            longitude += 0.0005
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[Publisher] Dihentikan.")
        client.disconnect()

if __name__ == "__main__":
    main()