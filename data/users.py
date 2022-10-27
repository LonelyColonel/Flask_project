import datetime
import sqlalchemy
import sqlalchemy.orm as orm
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.CHAR, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.CHAR, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.CHAR,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.CHAR, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    news = orm.relation("News", back_populates='user')
