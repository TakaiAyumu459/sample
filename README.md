# 2024年度 チーム開発演習サンプル

## 実装している機能

* テキストより単純なフォルダ構成
* ページごとにスタイルが変更可能なレイアウトテンプレート
* 画像をアップロードしてデータベースに保存する機能
* 画像をデータベースから取り出してレスポンスする機能

## 画像のアップロード機能について

PostgreSQL上で以下のSQL文を実行し、サンプル用のデータベースを作成してください。

```
CREATE DATABASE sample;
```

ターミナルで以下のコマンドを実行し、データベースにテーブルを作成してください。

```
$ENV:FLASK_APP='run.py'
flask db init
flask db migration
flask db upgrade
```
