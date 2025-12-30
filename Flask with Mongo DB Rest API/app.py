from flask import Flask, jsonify, request
from mongoengine import connect,IntField,StringField,Document


app = Flask(__name__)


db = connect(
    db="neha_db",
    host="localhost",
    port=27017
)

class User(Document):
    name = StringField(required=True)
    age = IntField(required=True)

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,  
            "age": self.age
        }


# create the user 
# http://localhost:5000/api/createUser
@app.route('/api/createUser', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(
        name=data['name'],  
        age =data['age']
    )
    user.save()

    return jsonify(user.to_json()), 201


# create the user 
# http://localhost:5000/api/findUsers
@app.route('/api/findUsers', methods=['GET'])
def find_users():
    users = User.objects()  #   LOAD THE DATA FROM MONGO DB     
    users_json = [user.to_json() for user in users] # CONVERT EACH USER TO JSON
    return jsonify(users_json), 200         # RETURN ALL DATA AS JSON


if __name__ == '__main__':
    app.run(debug=True)