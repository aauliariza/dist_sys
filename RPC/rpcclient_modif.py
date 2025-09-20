"""
JSON-RPC Client
Mengirim kalimat ke server lalu menampilkan jumlah vokal, konsonan, dan kata
"""

import requests
import json

# Fungsi RPC call
def call_rpc(method, params):
    url = "http://rpc-server:4000"  # gunakan nama service di docker-compose
    headers = {'content-type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1,
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    return response

# Helper print agar tidak error kalau server balas error
def safe_print(label, response):
    if "result" in response:
        print(f"{label}: {response['result']}")
    elif "error" in response:
        print(f"{label} -> ERROR: {response['error']}")
    else:
        print(f"{label} -> Unexpected response: {response}")

if __name__ == "__main__":
    # Input string dari user
    text = input("Enter a sentence: ")

    # Hitung jumlah vokal
    result_vowels = call_rpc("count_vowels", [text])
    safe_print("Number of vowels", result_vowels)

    # Hitung jumlah konsonan
    result_consonants = call_rpc("count_consonants", [text])
    safe_print("Number of consonants", result_consonants)

    # Hitung jumlah kata
    result_words = call_rpc("count_words", [text])
    safe_print("Number of words", result_words)