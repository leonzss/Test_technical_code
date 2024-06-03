from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def triangle(number):
    number_str = str(number)
    result = []
    for i in range (len(number_str)):
        row = number_str[i] + '0'*i
        result.append(row)
    return '\n'.join(result)

def odd_number(max_number):
    max_number = int(max_number)
    result = [str(i) for i in range(1, max_number + 1) if i % 2 != 0]
    return ', '.join(result)

def prime_number(max_number):
    result = []
    for num in range(2, max_number + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            result.append(str(num))
    return ', '.join(result)


# @routes
@app.route('/generate_segitiga', methods=['POST'])
def triangle_route():
    data = request.json
    if 'number' not in data:
        return jsonify({'error': 'Missing required parameter: number'}), 400
    try:
        number = int(data['number'])
    except ValueError:
        return jsonify({'error': 'Invalid number format: must be an integer'}), 400
    result = triangle(number)
    return jsonify({'triangle': result}), 200

@app.route('/generate_ganjil', methods=['POST'])
def odd_number_route():
    data = request.json
    if 'number' not in data:
        return jsonify({'error': 'Missing required parameter: number'}), 400
    try:
        number = int(data['number'])
    except ValueError:
        return jsonify({'error': 'Invalid number format: must be an integer'}), 400
    result = odd_number(number)
    return jsonify({'odd_numbers': result}), 200

@app.route('/generate_prima', methods=['POST'])
def prime_number_route():
    data = request.json
    if 'number' not in data:
        return jsonify({'error': 'Missing required parameter: number'}), 400
    try:
        number = int(data['number'])
    except ValueError:
        return jsonify({'error': 'Invalid number format: must be an integer'}), 400
    result = prime_number(number)
    return jsonify({'prime_numbers': result}), 200

if __name__ == '__main__':
    app.run(debug=True)