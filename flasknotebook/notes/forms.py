from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class NoteForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    content = TextAreaField('Treść', validators=[DataRequired()])
    submit = SubmitField('Zapisz')
