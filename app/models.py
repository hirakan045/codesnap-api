from datetime import datetime, timedelta, timezone

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String, Text)
from sqlalchemy.orm import DeclarativeBase, relationship

# 日本時間のタイムゾーン（UTC+9）
japan_tz = timezone(timedelta(hours=9))


class Base(DeclarativeBase):
    created_at = Column(DateTime, default=datetime.now(japan_tz))
    updated_at = Column(DateTime, default=datetime.now(japan_tz))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    # リレーション: ユーザーとスニペットの多対多関係を定義
    snippets = relationship('UserSnippet', back_populates='user')


class Snippet(Base):
    __tablename__ = 'snippets'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    code = Column(Text, nullable=False)
    language = Column(String)

    # Userとのリレーション
    user = relationship('UserSnippet', back_populates='snippet')


# 中間テーブル（user_snippets）
class UserSnippet(Base):
    __tablename__ = 'user_snippets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    snippet_id = Column(Integer, ForeignKey('snippets.id'), nullable=False)

    # リレーション: 中間テーブルとユーザー
    user = relationship('User', back_populates='snippets')
    # リレーション: 中間テーブルとスニペット
    snippet = relationship('Snippet', back_populates='users')
