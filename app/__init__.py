from config import Config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy

from .models import Base

db = SQLAlchemy(model_class=Base)
migrate = Migrate()


def create_app():

    # Flaskアプリの作成
    app = Flask(__name__)
    CORS(app)

    # アプリケーションに設定を読み込む
    app.config.from_object(Config)

    # データベースを初期化
    db.init_app(app)
    migrate.init_app(app, db)

    return app
