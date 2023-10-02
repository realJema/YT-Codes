'''
Name: Create a basic flask api 
Author: @realJema 
Date: 08/2023
'''

from flask import Flask 
from flask import jsonify

app = Flask(__name__)

# these are routes which run functions to return data to user 
@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/api/v1/users")
def get_users():
    users = [
        {
            "id": 1, 
            "name": "John Smith",
            "email": "john@gmail.com"
        }, 
        {
            "id": 2, 
            "name": "Juliet Bourne", 
            "email": "juliet@gmail.com"
        }
    ]
    return jsonify(users)

@app.route("/api/v1/fun")
def get_fun():
    return "This is fun"

if __name__ == "__main__":
    app.run(debug=True)