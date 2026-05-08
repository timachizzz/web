import sqlalchemy as sal
import datetime as dt
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm


class Tree(SqlAlchemyBase):
    __tablename__ = "Tree"
    id = sal.Column(sal.Integer, nullable=False, autoincrement=True, primary_key=True)
    name = sal.Column(sal.String, nullable=False)
    tree_type = sal.Column(sal.String)
    sector_id = sal.Column(sal.Integer, sal.ForeignKey('Sector.id'))
    sector = orm.relationship('TreeSector', backref='trees')
    coordinates = sal.Column(sal.String)
    planted_by = sal.Column(sal.String)
    taken_at = sal.Column(sal.DateTime, default=dt.datetime.now)
    age = sal.Column(sal.Integer, default=0)
    is_able_to_plant = sal.Column(sal.Boolean, default=True)

