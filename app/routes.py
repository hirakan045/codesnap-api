from app import db
from app.models import Snippet, User
from flask import Blueprint, jsonify, request

# Blueprintの作成
auth_bp = Blueprint('auth', __name__)


# 新規ユーザー登録
@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User(username=username, password=password)

    # ユーザー登録
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "ユーザー登録に成功しました。"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# # ログイン認証
# @auth_bp.route('/api/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')

#     # 仮のユーザー認証
#     if username == 'testuser' and password == 'testpassword':
#         return jsonify({"message": "ログイン成功"}), 200
#     else:
#         return jsonify({"message": "ログインに失敗しました"}), 401

# snippets_bp = Blueprint('snippets', __name__, url_prefix='/api')

# @snippets_bp.route('/snippets', methods=['GET'])
# def get_snippets():
#     snippets = db.session.query(Snippet).all()
#     snippet_list = [{
#         'id': snippet.id,
#         'title': snippet.title,
#         'code': snippet.code,
#         'language': snippet.language,
#         'created_at': snippet.created_at
#     } for snippet in snippets]
#     return jsonify(snippet_list)
