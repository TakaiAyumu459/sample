from flask import Flask

from sample.db import init_db

from .models.photo import Photo

app = Flask(__name__)

app.config.from_object("sample.config")

init_db(app)

# その他の機能はオブジェクトをインポートする
from sample.views import index,photos

# 写真アップロード機能サンプル
app.register_blueprint(photos.photo, url_prefix="/photo")