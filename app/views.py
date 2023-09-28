from flask import Blueprint, render_template, redirect, session, url_for, request, flash
from flask_login import login_user, logout_user, login_required, UserMixin, current_user
from app import login_manager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


main = Blueprint("main", __name__)

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

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "mer" and form.password.data == "eindregie":
            user = User(id=1)
            login_user(user)
            print("Form data:", form.data)
            print("Form errors:", form.errors)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password')
            
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route("/")
@login_required
def index():
    return render_template("index.html")

@main.route("/app_01", methods=["GET", "POST"])
@login_required
def app_01():
    return render_template("app1.html")

# TOGGLE THEME -------------------------------------------------------------

@main.get("/toggle_theme")
def toggle_theme():
    current_theme = session.get('theme', 'emerald')
    new_theme = 'business' if current_theme == 'emerald' else 'emerald'
    session['theme'] = new_theme
    return redirect(request.args.get("current_page"))
