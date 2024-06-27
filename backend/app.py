from flask import Flask, request, jsonify
from flask_cors import CORS
from github_api import get_user_commits

app = Flask(__name__)
CORS(app)

users = []

@app.route('/api/users', methods=['GET', 'POST', 'DELETE'])
def manage_users():
    global users
    if request.method == 'GET':
        user_data = [get_user_commits(user) for user in users]
        return jsonify(user_data)
    elif request.method == 'POST':
        new_user = request.json['username']
        if new_user not in users:
            users.append(new_user)
        return jsonify({"message": "User added successfully"})
    elif request.method == 'DELETE':
        user_to_remove = request.json['username']
        if user_to_remove in users:
            users.remove(user_to_remove)
        return jsonify({"message": "User removed successfully"})

if __name__ == '__main__':
    app.run(debug=True)
