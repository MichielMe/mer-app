from flask import Blueprint, render_template, redirect, session, url_for, request, flash, jsonify, send_from_directory, send_file, current_app
from flask_login import login_user, logout_user, login_required, UserMixin, current_user
from app import login_manager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from .pyscripts.forms import UploadForm, ExcelUploadForm
from .pyscripts.xlnaarpl import parse_excel_and_generate_playlist
import pandas as pd
from .models import Material
import os
from werkzeug.utils import secure_filename

main = Blueprint("main", __name__)

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'xlsx'}

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

@main.route("/testing")
def testing():
    return render_template("testing.html")


# APPS -------------------------------------------------------------

@main.route("/app_01", methods=["GET", "POST"])
@login_required
def app_01():
    form = UploadForm()
    material_tests = session.get('material_tests', None)
    # Get material_tests from session
    if form.validate_on_submit():
        # 1. Read the uploaded Excel file
        file = form.file.data
        df = pd.read_excel(file)
        material_ids = df.iloc[:, 0].values.tolist()  # Als de ID's in de eerste column staan.
     
        # # 2. Filter the database based on MATERIAL IDs
        # materials_to_update = Material.query.filter(
        #     Material.material_id.in_(material_ids)
        # ).all()

        # 3. Modify the title and material type columns
        replace_text = form.replace_text.data
        suffix = form.suffix.data
        material_type = form.material_type.data

        # for material in materials_to_update:
        #     if replace_text:
        #         material.title = material.title.replace(replace_text, suffix)
        #     else:
        #         material.title += " " + suffix

        #     material.material_type = material_type
        material_tests = [
            material_ids,
            replace_text,
            suffix,
            material_type
        ]
        session['material_tests'] = material_tests  # Store material_tests in session
        # 4. Commit changes to the database
        # db.session.commit()
        # materials = Material.query.all()
        print(session['material_tests'])
        
        flash("Database updated successfully!", "success")
        
        return render_template("app1.html", form=form, material_tests=material_tests)
        
    return render_template("app1.html", form=form, material_tests=material_tests)



@main.route("/app_02", methods=["GET", "POST"])
@login_required
def app_02():
    return render_template("app2.html")

@main.route("/app_03", methods=["GET", "POST"])
@login_required
def app_03():
    form = ExcelUploadForm()
    download_link = None  # Link to download the generated .sch file

    if form.validate_on_submit():
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        file = form.file.data
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # Process the file using the refactored script
        output_filepath = parse_excel_and_generate_playlist(filepath)
        
        if output_filepath:
            # File processed successfully, generate a download link
            download_link = url_for('main.download', filename=output_filepath.name)  # Using the name attribute of PurePath
            flash('File processed successfully!', 'success')
        else:
            # There was an error processing the file
            flash('An error occurred while processing the file. Please try again.', 'error')

    return render_template("app3.html", form=form, download_link=download_link)

@main.route('/uploads/<path:filename>', methods=["GET", "POST"])
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)



# @app.route("/uploads/<path:name>")
#     def download_file(name):
#         return send_from_directory(
#             app.config['UPLOAD_FOLDER'], name, as_attachment=True
#         )


# TOGGLE THEME -------------------------------------------------------------

@main.get("/toggle_theme")
def toggle_theme():
    current_theme = session.get('theme', 'emerald')
    new_theme = 'business' if current_theme == 'emerald' else 'emerald'
    session['theme'] = new_theme
    return redirect(request.args.get("current_page"))
