"""
Subscriber MQTT - Data GPS
Menerima koordinat GPS dari publisher
"""

import paho.mqtt.client as mqtt
import sys

# Konfigurasi broker
BROKER = "mqtt-broker"
PORT = 1883
TOPIC = "sister/gps"

# Callback koneksi
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[Subscriber] Terhubung ke broker MQTT {BROKER}")
        client.subscribe(TOPIC)
        print(f"[Subscriber] Berlangganan topik: {TOPIC}")
    else:
        print(f"[Subscriber] Gagal terhubung, kode error: {rc}")
        sys.exit(1)

# Callback pesan
def on_message(client, userdata, message, properties=None):
    print(f"[Subscriber] Koordinat diterima: {message.payload.decode()} (Topik: {message.topic})")

def main():
    # Inisialisasi klien
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message

    # Hubungkan ke broker
    try:
        print(f"Menghubungkan ke {BROKER}...")
        client.connect(BROKER, PORT, keepalive=60)
    except Exception as e:
        print(f"Gagal menghubungkan ke broker: {e}")
        sys.exit(1)

    # Jalankan loop menunggu pesan
    try:
        print("[Subscriber] Menunggu koordinat... (Ctrl+C untuk keluar)")
        client.loop_forever()
    except KeyboardInterrupt:
        print("\n[Subscriber] Dihentikan.")
        client.disconnect()

if __name__ == "__main__":
    main()