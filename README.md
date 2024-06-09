# 2024年度 チーム開発演習サンプル

## 画像のアップロード機能について

PostgreSQL上で以下のSQL文を実行し、サンプル用のデータベースを作成してください。

```
CREATE DATABASE sample;
```

コマンドラインで以下のコマンドを実行し、データベースにテーブルを作成してください。

```
$ENV:FLASK_APP='run.py'
flask db init
flask db migration
flask db upgrade
```