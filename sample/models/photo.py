from sample.db import db
from pathlib import Path


class Photo(db.Model):

    __tablename__ = "photos"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256), nullable=False)
    # バイナリデータを保存する場合はLargeBinaryを使用する
    # PostgreSQLの場合、最大1GBまで
    photo  = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, filename, blob):
        ext =  Path(filename).suffix.lower()
        print(ext)
        if ext not in ['.jpg','.jpeg','.png','.gif']:
            raise Exception("許可された画像形式ではありません")
        self.filename = filename
        self.photo = blob