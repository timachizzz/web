"""
Модуль flask-wtf для создания и обработки форм

Создадим форму, которая будет содержать:
+ текстовые поля для ввода логина и пароля;
+ чекбокс «Запомнить меня»;
+ кнопку отправки формы на сервер.

См. форму login.html
"""

from flask import Flask, render_template, redirect
from loginform import LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
