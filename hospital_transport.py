
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for transport requests
transport_requests = []

@app.route('/')
def home():
    return render_template('soignant.html')

@app.route('/add_transport', methods=['POST'])
def add_transport():
    data = request.get_json()
    transport_requests.append(data)
    return jsonify({'message': 'Transport request added successfully', 'data': data}), 201

@app.route('/list_transports', methods=['GET'])
def list_transports():
    return jsonify({'transport_requests': transport_requests}), 200

@app.route('/update_transport/<int:request_id>', methods=['PUT'])
def update_transport(request_id):
    data = request.get_json()
    if request_id < len(transport_requests):
        transport_requests[request_id].update(data)
        return jsonify({'message': 'Transport request updated successfully', 'data': transport_requests[request_id]}), 200
    else:
        return jsonify({'message': 'Transport request not found'}), 404

@app.route('/delete_transport/<int:request_id>', methods=['DELETE'])
def delete_transport(request_id):
    if request_id < len(transport_requests):
        removed_request = transport_requests.pop(request_id)
        return jsonify({'message': 'Transport request deleted successfully', 'data': removed_request}), 200
    else:
        return jsonify({'message': 'Transport request not found'}), 404

@app.route('/regulation')
def regulation():
    return render_template('regulation.html')

@app.route('/list_historique_transports', methods=['GET'])
def list_historique_transports():
    historique_transports = [t for t in transport_requests if t['status'] == 'completed']
    return jsonify({'transport_requests': historique_transports}), 200

@app.route('/list_en_cours_transports', methods=['GET'])
def list_en_cours_transports():
    en_cours_transports = [t for t in transport_requests if t['status'] == 'in_progress']
    return jsonify({'transport_requests': en_cours_transports}), 200

@app.route('/list_futurs_transports', methods=['GET'])
def list_futurs_transports():
    futurs_transports = [t for t in transport_requests if t['status'] == 'pending']
    return jsonify({'transport_requests': futurs_transports}), 200

if __name__ == '__main__':
    app.run(port=5001)
