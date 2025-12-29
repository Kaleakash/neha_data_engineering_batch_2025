from flask import Flask, jsonify, request
app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice","age":30},
    {"id": 2, "name": "Bob","age":25},
    {"id": 3, "name": "Charlie","age":35}
]

# Endpoint to return a welcome message
# http://localhost:5000/api/user/hello
@app.route('/api/user/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Welcome to Simple User REST API with In-Memory Database!")

# Endpoint to return all users
# http://localhost:5000/api/users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Endpoint to search particular user by ID
# http://localhost:5000/api/user/1
# http://localhost:5000/api/user/10

@app.route('/api/user/<int:user_id>', methods=['GET'])
def find_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Endpoint to store the user details in in-memory database
# http://localhost:5000/api/user

@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "age": data["age"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)