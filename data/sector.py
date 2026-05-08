import sqlalchemy as sal
from data.db_session import SqlAlchemyBase


class TreeSector(SqlAlchemyBase):
    __tablename__ = 'Sector'
    id = sal.Column(sal.Integer, nullable=False, autoincrement=True, primary_key=True)
    type = sal.Column(sal.String)
    is_full = sal.Column(sal.Boolean)
