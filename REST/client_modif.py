"""
REST Client untuk mengakses operasi matematika sederhana
"""

import requests
import argparse
import sys

BASE = 'http://rest-server:5252'

def call(endpoint, a, b):
    try:
        r = requests.get(f"{BASE}/{endpoint}", params={'a': a, 'b': b}, timeout=5)
        if r.status_code == 200:
            data = r.json()
            print(f"[{data['operation'].upper()}] {data['a']} dan {data['b']} -> {data['result']}")
        else:
            print(f"[{endpoint.upper()}] error {r.status_code}: {r.text}")
    except Exception as e:
        print(f"[{endpoint.upper()}] exception: {e}")

def main():
    parser = argparse.ArgumentParser(description="REST client untuk operasi matematika")
    parser.add_argument('--op', choices=['add', 'sub', 'mul', 'div', 'all'], default='all', help='Operation to invoke')
    parser.add_argument('-a', type=int, default=8, help='Operand A (default=8)')
    parser.add_argument('-b', type=int, default=4, help='Operand B (default=4)')
    args = parser.parse_args()

    ops = [args.op] if args.op != 'all' else ['add', 'sub', 'mul', 'div']
    for op in ops:
        call(op, args.a, args.b)

if __name__ == '__main__':
    sys.exit(main())