from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from data import db_session
from data.User import FamilyUser

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/api/register', methods=['POST'])
def register():
    """Регистрация семьи"""
    data = request.get_json()

    if not data or 'surname' not in data or 'password' not in data:
        return jsonify({'success': False, 'error': 'Не заполнены обязательные поля'}), 400

    session = db_session.create_session()

    #Проверка на существование пользователя
    existing = session.query(FamilyUser).filter_by(surname=data['surname']).first()
    if existing:
        return jsonify({'success': False, 'error': 'Семья с такой фамилией уже зарегистрирована'}), 400

    # Создание пользователя
    user = FamilyUser()
    user.surname = data['surname']
    user.set_password(data['password'])
    user.family_size = data.get('family_size', 1)
    user.num_trees_alr_planted = 0

    session.add(user)
    session.commit()

    return jsonify({
        'success': True,
        'user': {
            'id': user.id,
            'surname': user.surname,
            'family_size': user.family_size
        }
    }), 201


@auth_bp.route('/api/login', methods=['POST'])
def login():
    """Вход в систему"""
    data = request.get_json()

    if not data or 'surname' not in data or 'password' not in data:
        return jsonify({'success': False, 'error': 'Не заполнены поля'}), 400

    session = db_session.create_session()
    user = session.query(FamilyUser).filter_by(surname=data['surname']).first()

    if not user or not user.check_password(data['password']):
        return jsonify({'success': False, 'error': 'Неверная фамилия или пароль'}), 401

    login_user(user, remember=data.get('remember_me', False))
    return jsonify({
        'success': True,
        'user': {
            'id': user.id,
            'surname': user.surname,
            'family_size': user.family_size,
            'num_trees_alr_planted': user.num_trees_alr_planted
        }
    })


@auth_bp.route('/api/logout')
@login_required
def logout():
    """Выход"""
    logout_user()
    return jsonify({'success': True})


@auth_bp.route('/api/user/me')
@login_required
def me():
    """Текущий пользователь"""
    return jsonify({
        'id': current_user.id,
        'surname': current_user.surname,
        'family_size': current_user.family_size,
        'num_trees_alr_planted': current_user.num_trees_alr_planted
    })