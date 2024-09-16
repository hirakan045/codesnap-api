from config import Config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy

from .models import Base

db = SQLAlchemy(model_class=Base)
migrate = Migrate()


def create_app():
    from .routes import auth_bp

    # Flaskアプリの作成
    app = Flask(__name__)
    CORS(app)

    # アプリケーションの設定
    app.config.from_object(Config)

    # データベースの初期化
    db.init_app(app)
    migrate.init_app(app, db)

    # BluePrintの登録
    app.register_blueprint(auth_bp)

    return app
