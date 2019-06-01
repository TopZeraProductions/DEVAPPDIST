from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return "<h1>Aplicaçao Flask Aqui oh!!!</h1>", 200


app.run(
    host='localhost',
    port=5300,
    debug=True
)