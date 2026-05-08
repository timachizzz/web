from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from data import db_session
from data.Tree import Tree
from data.notifications import Notification

trees_bp = Blueprint('trees', __name__)


@trees_bp.route('/api/trees')
def get_trees():
    """Вернуть JSON со всеми деревьями и их статусами"""
    session = db_session.create_session()
    trees = session.query(Tree).all()

    result = []
    for tree in trees:
        result.append({
            'id': tree.id,
            'name': tree.name,
            'type': tree.tree_type,
            'sector_id': tree.sector_id,
            'coordinates': tree.coordinates,
            'planted_by': tree.planted_by,
            'is_able_to_plant': tree.is_able_to_plant,
            'age': tree.age
        })

    return jsonify({'success': True, 'trees': result})


@trees_bp.route('/api/trees/book/<int:tree_id>', methods=['POST'])
@login_required
def book_tree(tree_id):
    session = db_session.create_session()
    tree = session.query(Tree).get(tree_id)

    if not tree:
        return jsonify({'success': False, 'error': 'Дерево не найдено'}), 404
    if not tree.is_able_to_plant:
        return jsonify({'success': False, 'error': 'Это дерево уже занято'}), 409

    tree.is_able_to_plant = False
    tree.planted_by = current_user.surname
    current_user.num_trees_alr_planted += 1

    #уведомление для админа
    notif = Notification(
        tree_id=tree.id,
        tree_name=tree.name,
        tree_type=tree.tree_type,
        coordinates=tree.coordinates,
        user_surname=current_user.surname,
        user_id=current_user.id
    )
    session.add(notif)
    session.commit()

    return jsonify({
        'success': True,
        'tree': {
            'id': tree.id,
            'name': tree.name,
            'planted_by': tree.planted_by,
            'is_able_to_plant': tree.is_able_to_plant
        }
    })