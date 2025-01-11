

from flask import Flask, request, jsonify

app = Flask(__name__)

data = [
    {"id": 1, "name": "Sanika", "role": "Junior AI Trainee"},
    {"id": 2, "name": "John", "role": "Software Engineer"}
]

@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    new_user["id"] = len(data) + 1
    data.append(new_user)
    return jsonify(new_user), 201

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(data)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((item for item in data if item["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((item for item in data if item["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    updates = request.get_json()
    user.update(updates)
    return jsonify(user)

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global data
    data = [item for item in data if item["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
