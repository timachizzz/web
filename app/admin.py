from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from data import db_session
from data.notifications import Notification

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/api/admin/notifications')
@login_required
def get_notifications():
    if not current_user.is_admin:
        return jsonify({'success': False, 'error': 'Доступ запрещён'}), 403

    session = db_session.create_session()
    # Отдаём непрочитанные за последние 30 секунд (для polling'а)
    notifs = session.query(Notification).filter_by(is_read=False).order_by(
        Notification.created_at.desc()
    ).limit(20).all()

    result = []
    for n in notifs:
        result.append({
            'id': n.id,
            'tree_id': n.tree_id,
            'tree_name': n.tree_name,
            'tree_type': n.tree_type,
            'coordinates': n.coordinates,
            'user_surname': n.user_surname,
            'created_at': n.created_at.isoformat()
        })

    return jsonify({'success': True, 'notifications': result})


@admin_bp.route('/api/admin/notifications/read/<int:notif_id>', methods=['POST'])
@login_required
def mark_read(notif_id):
    if not current_user.is_admin:
        return jsonify({'success': False, 'error': 'Доступ запрещён'}), 403

    session = db_session.create_session()
    notif = session.query(Notification).get(notif_id)
    if notif:
        notif.is_read = True
        session.commit()

    return jsonify({'success': True})