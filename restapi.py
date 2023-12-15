from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Beispiel Data
data = [
    {'id': 1, 'name': 'John'},
    {'id': 2, 'name': 'Jane'},
    {'id': 3, 'name': 'Doe'}
]

# Route um alle Daten zu erhalten
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'data': data})

@app.route('/api/singledata', methods=['GET'])
def get_singledata():
    return jsonify({'data': data[0]})

if __name__ == '__main__':
    app.run(debug=True, port=5001)



def get_single_data():
    if len(data) > 0:
        return jsonify({'single_data': data[0]})
    else:
        return jsonify({'message': 'No data available'})