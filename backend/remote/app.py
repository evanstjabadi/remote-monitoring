from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


# Init app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from random.models import db  # noqa isort:skip

db.init_app(app)

from random.views import api  # noqa isort:skip

app.register_blueprint(api)
