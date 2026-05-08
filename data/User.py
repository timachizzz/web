import sqlalchemy as sal
from data.db_session import SqlAlchemyBase
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class FamilyUser(SqlAlchemyBase, UserMixin):
    __tablename__ = "FamilyUser"

    id = sal.Column(sal.Integer, nullable=False, primary_key=True, autoincrement=True)
    surname = sal.Column(sal.String, nullable=False)
    password_hash = sal.Column(sal.String(200), nullable=False)
    family_size = sal.Column(sal.Integer, nullable=False)
    trees_alr_planted = sal.Column(sal.String)
    num_trees_alr_planted = sal.Column(sal.Integer)
    is_admin = sal.Column(sal.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)