
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

if __name__ == '__main__':
    app.run(port=5001)
