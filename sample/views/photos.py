"""
ファイルアップロードサンプル

参考)
https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/patterns/fileuploads.html

"""
import mimetypes # ファイル種別 MIME-Typeを拡張子から判別するために必要

from flask import render_template, request, url_for, redirect, flash, Blueprint,make_response
from werkzeug.utils import secure_filename

from sample.models.photo import Photo


from sample.db import db

photo = Blueprint('photo', __name__)

@photo.route('/')
def index():
    """
    画像一覧とアップロードフォームを表示
    """
    # 画像データのidとfilenameだけを取得する
    photos = Photo.query.with_entities(Photo.id,Photo.filename).all()
    return render_template('photos/index.html',photos = photos)

@photo.route('/<int:id>/src')
def src(id):
    """
    指定されたidの画像データ本体をレスポンスする
    """
    photo = Photo.query.get(id)
    response = make_response(photo.photo)
    response.headers.set('Content-Type', mimetypes.guess_type(photo.filename))
    return response

@photo.route('upload',methods=["POST"])
def upload():
    """
    アップロードフォームからのPOSTリクエストによって画像をデータベースに保存する
    """
    if 'file' not in request.files:
        flash('ファイルがアップロードされませんでした','error')
        return redirect(url_for('photo.index'))
    file = request.files['file']
    if file.filename == '':
        flash('ファイルが選択されていません','error')
        return redirect(url_for('photo.index'))
    if file :
        filename = secure_filename(file.filename)
        photo = Photo(filename,file.stream.read())
        db.session.add(photo)
        db.session.commit()
        flash("画像を保存しました","success")
    return redirect(url_for('photo.index'))

@photo.route('/<int:id>/delete')
def delete(id):
    """
    指定されたidの画像ファイルを削除する
    """
    photo = Photo.query.get(id)
    db.session.delete(photo)
    db.session.commit()
    return redirect(url_for('photo.index'))
