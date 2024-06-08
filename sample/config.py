import os

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.getenv('DB_USR','postgres')}:{os.getenv('DB_PASSWORD','himitu')}@{os.getenv('DB_HOST','localhost:5432')}/sample"
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'secret_key'
DEBUG = True