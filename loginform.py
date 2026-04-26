from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


"""
Из wtforms импортируем типы полей, которые нам пригодятся для создания формы:
+ StringField - текстовое поле
+ PasswordField - поле ввода пароля
+ BooleanField - булево поле (чекбокс)
+ SubmitField - кнопка отправки данных

Из wtforms.validators импортируем валидатор DataRequired,
который проверяет, введены ли данные в поле или нет.
"""


class LoginForm(FlaskForm):
    """Поля для формы"""
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
