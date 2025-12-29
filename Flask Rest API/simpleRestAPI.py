from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Welcome to Simple Rest API!")

if __name__ == '__main__':
    app.run(debug=True)