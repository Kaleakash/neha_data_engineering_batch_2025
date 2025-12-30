from flask import Flask, jsonify, request

app = Flask(__name__)
# it hold data in memory
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
# http://localhost:5000/api/createUser
# fro client side or plugin we need to pass the data in json format 
@app.route('/api/createUser', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
    new_user = {
        "id": len(users) + 1,           # incremental id by 1
        "name": data["name"],
        "age": data["age"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Endpoint to update the user details in in-memory database
# http://localhost:5000/api/updateUser/1
# fro client side or plugin we need to pass the data in json format 
@app.route('/api/updateUser/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user["name"] = data.get("name", user["name"])
        user["age"] = data.get("age", user["age"])
        return jsonify(user)    
    return jsonify({"error": "User not found"}), 404

# Endpoint to delete the user details in in-memory database
# http://localhost:5000/api/deleteUser/1
# fro client side or plugin we need to pass the data in json format 
@app.route('/api/deleteUser/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        users.remove(user)
        return jsonify({"message": "User deleted successfully"})    
    return jsonify({"error": "User not found"}), 404



if __name__ == '__main__':
    app.run(debug=True)