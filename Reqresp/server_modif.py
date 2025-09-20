"""
Multi-client TCP server untuk menghitung kuadrat angka
"""

import socket
import threading

def handle_client(conn, addr):
    print(f"[TERHUBUNG] Client {addr} berhasil terhubung")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if data.lower().strip() == "exit":
            print(f"[PUTUS] Client {addr} keluar")
            break

        try:
            # bisa menerima banyak angka sekaligus, dipisahkan koma
            numbers = [int(x.strip()) for x in data.split(",")]
            results = [f"{n}^2={n*n}" for n in numbers]
            response = " | ".join(results)
        except ValueError:
            response = "Input tidak valid, masukkan angka atau angka-angka dipisahkan koma"

        # tampilkan hasil di sisi server
        print(f"[SERVER LOG] Dari {addr}: {data} -> {response}")

        # kirim hasil ke client
        conn.send(response.encode())

    conn.close()

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 4444))
    server_socket.listen(5)
    print("[SERVER AKTIF] Menunggu client di port 4444...")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    server_program()