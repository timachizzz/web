"""
Модуль flask-wtf для создания и обработки форм

Создадим форму, которая будет содержать:
+ текстовые поля для ввода логина и пароля;
+ чекбокс «Запомнить меня»;
+ кнопку отправки формы на сервер.

См. форму login.html
"""

from flask import Flask, render_template, redirect
#from flask_login import LoginManager
from app.loginform import LoginForm
from data import db_session
from data.User import FamilyUser
from app.auth import auth_bp
from app.trees import trees_bp
from app.admin import admin_bp


app = Flask(__name__)
app.register_blueprint(admin_bp)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
"""
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'  # Куда редиректить неавторизованных

@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(FamilyUser).get(int(user_id))

# Blueprint'ы
app.register_blueprint(auth_bp)
app.register_blueprint(trees_bp)
"""
@app.route('/')
@app.route('/index')
def index():
    """Корневая страница"""
    param = dict()
    param['username'] = 'Главное окно'
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


# URL http://localhost:8080/login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Заполнение формы"""
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    """Удачно"""
    param = dict()
    param['username'] = 'Вы в профиле!'
    return render_template('main.html', **param)

db_session.global_init("db/GV.db")

if __name__ == '__main__':

    app.run(host='localhost', port=8000)
