"""
Client untuk multi-client TCP server kuadrat angka
"""

import socket

def client_program():
    client_socket = socket.socket()
    client_socket.connect(("reqresp-server", 4444))

    print("Ketik angka untuk dihitung kuadratnya (bisa lebih dari satu, pisahkan dengan koma).")
    print("Ketik 'exit' untuk keluar.")
    message = input("Masukkan angka: ")

    while message.lower().strip() != "exit":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        # tampilkan hanya hasil respon server di sisi client
        print(f"[HASIL SERVER] {data}")

        message = input("Masukkan angka: ")

    client_socket.send("exit".encode())
    client_socket.close()
    print("Koneksi ditutup.")

if __name__ == "__main__":
    client_program()