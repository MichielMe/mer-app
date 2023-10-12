# Standard Library Imports
import os
import time

# Third-party Imports
from flask import Blueprint, render_template, redirect, session, url_for, request, flash, send_from_directory, send_file
from flask_login import login_required
from werkzeug.utils import secure_filename
import pandas as pd

# Local Application Imports
from .config import UPLOAD_FOLDER
from .pyscripts.forms import UploadForm, ExcelUploadForm, ColorForm
from .pyscripts.xlnaarpl import parse_excel_and_generate_playlist
from .helpers import convert_xls_to_xlsx_with_excel, apply_excel_styles, save_uploaded_file



main = Blueprint("main", __name__)

@main.route("/")
@login_required
def index():
    """Renders the main index page."""
    return render_template("index.html")

@main.route("/app_01", methods=["GET", "POST"])
@login_required
def app_01():
    """Handles operations for bulk edit"""
    form = UploadForm()
    material_data = session.get('material_data', {})
    show_modal = False

    if form.validate_on_submit():
        try:
            file = form.file.data
            df = pd.read_excel(file)
            material_ids = df.iloc[:, 0].values.tolist()
            material_data = {
                "ids": material_ids,
                "replace_text": form.replace_text.data,
                "suffix": form.suffix.data,
                "material_type": form.material_type.data
            }
            session['material_data'] = material_data
            show_modal = True
        except Exception as e:
            flash(f"Error processing data: {str(e)}", "error")

    return render_template("app1.html", form=form, material_data=material_data, show_modal=show_modal)



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


@main.route("/app_04", methods=["GET", "POST"])
@login_required
def app_04():
    file_uploaded = False  # or False based on your logic

    form = ColorForm()
    if form.validate_on_submit():
        # Hanlde the file upload
        if "file" not in request.files:
            return "No file part."
        file = request.files["file"]
        
        filepath = save_uploaded_file(file)
        
        print("Absolute path of the file to convert:", os.path.abspath(filepath))

        time.sleep(2)
        
        if filepath.endswith('.xls'):
            print("Converting .xls to .xlsx")
            filepath = convert_xls_to_xlsx_with_excel(filepath)
            
        time.sleep(2)
        
        form_data = {
            'programma': form.programma.data,
            'wrap': form.wrap.data,
            'ondertiteling': form.ondertiteling.data
        }

        apply_excel_styles(filepath, form_data)

        return redirect(url_for("main.download2", filename=os.path.basename(filepath)))
    return render_template("app4.html", form=form, file_uploaded=file_uploaded)

@main.route("/download/<filename>")
def download2(filename):
    filepath = os.path.join(os.getcwd(), "uploads", filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        return f"Error: File '{filename}' not found.", 404


@main.route("/app_05", methods=["GET", "POST"])
@login_required
def app_05():
    return render_template("app5.html")