# config.py
import os
from re import DEBUG

# データベース URI を環境変数から取得
base_dir = os.path.dirname(__file__)
DATABASE_URI = os.getenv('DATABASE_URI', f"sqlite:///{os.path.join(base_dir,'codesnap.db')}")


class Config:
    # デバッグモード
    DEBUG = True

    # オブジェクト変更に関連する警告メッセージの非表示
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # DB設定
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
