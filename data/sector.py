import sqlalchemy as sal
from db_session import SqlAlchemyBase


class TreeSector(SqlAlchemyBase):
    __tablename__ = 'Сектора'
    id = sal.Column(sal.Integer, nullable=False, autoincrement=True, primary_key=True)
    type = sal.Column(sal.String)
    is_full = sal.Column(sal.Boolean)
