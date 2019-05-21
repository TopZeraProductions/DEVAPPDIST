from flask import Flask

from App.person import person_app

from Models.person_model import Person

Person.migrate_table()

app = Flask(__name__)

app.register_blueprint(person_app)

app.run(
    host='localhost',
    port=5081,
    debug=True
)
