import sqlalchemy as sal
from db_session import SqlAlchemyBase


class FamilyUser(SqlAlchemyBase):
    __tablename__ = "Семейный пользователь"
    id = sal.Column(sal.Integer, nullable=False, primary_key=True, autoincrement=True)
    surname = sal.Column(sal.String, Nullable = False)
    family_size = sal.Column(sal.Integer, Nullable = False)
    trees_alr_planted = sal.Column(sal.String)
    num_trees_alr_planted = sal.Column(sal.Integer)

