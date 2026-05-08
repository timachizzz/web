import sqlalchemy as sal
from sqlalchemy import orm
import datetime as dt
from data.db_session import SqlAlchemyBase


class Notification(SqlAlchemyBase):
    __tablename__ = 'Notification'

    id = sal.Column(sal.Integer, primary_key=True, autoincrement=True)
    tree_id = sal.Column(sal.Integer, sal.ForeignKey('Tree.id'))
    tree_name = sal.Column(sal.String)
    tree_type = sal.Column(sal.String)
    coordinates = sal.Column(sal.String)
    user_surname = sal.Column(sal.String)
    user_id = sal.Column(sal.Integer, sal.ForeignKey('FamilyUser.id'))
    created_at = sal.Column(sal.DateTime, default=dt.datetime.now)
    is_read = sal.Column(sal.Boolean, default=False)

    user = sal.orm.relationship('FamilyUser')
    tree = sal.orm.relationship('Tree')