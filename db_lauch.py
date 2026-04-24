from data.db_session import global_init, create_session
from data.User import FamilyUser
from data.sector import TreeSector
from data.Tree import Tree


global_init('GV.db')

session = create_session()

"""
Неким образом вводиятся данные пользователя, занимаемое им дерево и соответствующий сектор
"""

#session.add(new_user)
session.commit()

