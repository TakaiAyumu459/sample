from flask import Flask

from sample.db import init_db

from .models.photo import Photo

app = Flask(__name__)

app.config.from_object("sample.config")

init_db(app)

import sample.views.index