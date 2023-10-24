from typing import Optional
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
    
    go_submit = SubmitField("GO")

## Form from Bitbucket
# class VullingenForm(FlaskForm):
#     title = StringField('Vul hier de titel in', validators=[Optional()])
#     submit = SubmitField('Zoek')
#     newtitle = StringField('Vul hier de nieuwe titel in', validators=[Optional()])
#     material_types = [("COMMERCIAL", "COMMERCIAL"), ("PROGRAMME", "PROGRAMME"), ("JUNCTION", "JUNCTION"), ("LIVE RECORD", "LIVE RECORD")]
#     material_type = SelectField(u'Material type', choices=material_types, validators=[Optional()])
#     update = SubmitField('Update')


class ExcelUploadForm(FlaskForm):
    file = FileField('Excel File', validators=[
        FileRequired(),
        FileAllowed(['xlsx'], 'Excel files only!')
    ])
    submit = SubmitField('Upload and Generate')
    
    
class ColorForm(FlaskForm):
    programma = SelectField(
        "Programma Kleur",
        choices=[
            ("yellow", "GEEL"),
            ("red", "ROOD"),
            ("blue", "BLAUW"),
            ("orange", "ORANJE"),
        ],
    )
    wrap = SelectField(
        "Wrap Kleur",
        choices=[
            ("yellow", "GEEL"),
            ("red", "ROOD"),
            ("blue", "BLAUW"),
            ("orange", "ORANJE"),
        ],
    )
    ondertiteling = SelectField(
        "Ondertiteling Kleur",
        choices=[
            ("yellow", "GEEL"),
            ("red", "ROOD"),
            ("blue", "BLAUW"),
            ("orange", "ORANJE"),
        ],
    )
    submit = SubmitField("GO")