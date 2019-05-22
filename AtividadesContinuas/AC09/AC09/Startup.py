from flask import Flask

from App.names import name_app
from App.document import document_app
from App.cep import cep_app

from Models.names_model import Name
from Models.cep_model import Cep
from Models.document_model import Document

Name.migrate_table()
Document.migrate_table()
Cep.migrate_table()
app = Flask(__name__)

app.register_blueprint(name_app)
app.register_blueprint(document_app)
app.register_blueprint(cep_app)

app.run(
    host='localhost',
    port=5080,
    debug=True
)

