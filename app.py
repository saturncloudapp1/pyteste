from flask import Flask, jsonify

app = Flask(__name)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)
