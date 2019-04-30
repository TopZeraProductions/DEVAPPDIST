from controllers import TodoApi
from flask import Flask, jsonify, request, Response


app = Flask(__name__)
app.register_blueprint(TodoApi)


@app.route('/')
def index():
    res = Response("[\"hello\": \"hello\"]")
    res.headers.clear()
    res.headers.add("Content-Type", "aplication/json")

    return res, 200


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=5000,
        debug=True
    )
