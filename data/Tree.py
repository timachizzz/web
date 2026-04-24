import sqlalchemy as sal
import datetime as dt
from db_session import SqlAlchemyBase


class Tree(SqlAlchemyBase):
    __tablename__ = "Дерево"
    id = sal.Column(sal.Integer, nullable=False, autoincrement=True, primary_key=True)
    name = sal.Column(sal.String, nullable=False)
    coordinates = sal.Column(sal.String)
    planted_by = sal.Column(sal.String)
    taken_at = sal.Column(sal.DateTime, default=dt.datetime.now())
    age = sal.Column(sal.DateTime, default=0)
    is_able_to_plant = sal.Column(sal.Boolean, default=True)