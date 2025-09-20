"""
REST Server untuk operasi matematika sederhana
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

def get_params():
    """Helper untuk mengambil parameter a dan b dari query string"""
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        return a, b
    except (TypeError, ValueError):
        return None, None

@app.route('/add', methods=['GET'])
def add_numbers():
    a, b = get_params()
    if a is None or b is None:
        return jsonify({'error': 'Invalid input'}), 400
    return jsonify({'operation': 'add', 'a': a, 'b': b, 'result': a + b})

@app.route('/sub', methods=['GET'])
def sub_numbers():
    a, b = get_params()
    if a is None or b is None:
        return jsonify({'error': 'Invalid input'}), 400
    return jsonify({'operation': 'sub', 'a': a, 'b': b, 'result': a - b})

@app.route('/mul', methods=['GET'])
def mul_numbers():
    a, b = get_params()
    if a is None or b is None:
        return jsonify({'error': 'Invalid input'}), 400
    return jsonify({'operation': 'mul', 'a': a, 'b': b, 'result': a * b})

@app.route('/div', methods=['GET'])
def div_numbers():
    a, b = get_params()
    if a is None or b is None:
        return jsonify({'error': 'Invalid input'}), 400
    if b == 0:
        return jsonify({'error': 'Division by zero'}), 400
    return jsonify({'operation': 'div', 'a': a, 'b': b, 'result': a / b})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5252)
