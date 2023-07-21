import flask
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

users = []

@app.route("/")
def index():
    return render_template("index.html", users=users)

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def post_user():
    user = request.json
    users.append(user)
    return jsonify(user), 201

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    if id < len(users):
        user = users.pop(id)
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/users/<int:id>", methods=["PUT"])
def put_user(id):
    if id < len(users):
        user = request.json
        users[id] = user
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
