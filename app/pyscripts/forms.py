from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class UploadForm(FlaskForm):
    file = FileField(
        "Upload Excel bestand met WP-nummers",
        validators=[
            FileRequired(),
            FileAllowed(["xlsx", "xls"], message="Enkel Excel bestanden!")]
        )
    
    suffix = StringField(
        "Wat wil je toevoegen aan de titel?", validators=[DataRequired()]
    )
    
    replace_text = StringField("Te vervangen tekst: (laat leeg als je alleen iets wilt toevoegen aan de tekst.)")
    
    material_type = SelectField(
        "Material Type",
        choices=[
            ("COMMERCIAL", "COMMERCIAL"),
            ("JUNCTION", "JUNCTION"),
            ("PROGRAMME", "PROGRAMME"),
            ("LIVE RECORD", "LIVE RECORD"),
        ],
        validators=[DataRequired()],
    )
    
    submit = SubmitField("GO")



class ExcelUploadForm(FlaskForm):
    file = FileField('Excel File', validators=[
        FileRequired(),
        FileAllowed(['xlsx'], 'Excel files only!')
    ])
    submit = SubmitField('Upload and Generate')