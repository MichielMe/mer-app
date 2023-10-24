from flask import Blueprint, render_template, redirect, session, url_for, flash
from flask_login import login_user, logout_user, login_required, UserMixin
from app import login_manager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

auth_blueprint = Blueprint("auth", __name__)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "mer" and form.password.data == "eindregie":
            user = User(id=1)
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form) # type: ignore

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login')) # type: ignore
