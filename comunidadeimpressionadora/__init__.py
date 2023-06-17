from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SECRET_KEY'] = '6037c3d29cc427f4051a2521ea3adf25168c7b44057fa953'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)


from comunidadeimpressionadora import routes
