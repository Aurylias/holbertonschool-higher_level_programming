from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def all_users():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json(force=True, silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 404
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
