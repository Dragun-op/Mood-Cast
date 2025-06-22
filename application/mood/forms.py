from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

class MoodForm(FlaskForm):
    mood = SelectField('Mood', choices=[
        ('Happy', 'Happy'), ('Sad', 'Sad'), ('Anxious', 'Anxious'),
        ('Angry', 'Angry'), ('Excited', 'Excited'), ('Calm', 'Calm'),
        ('Tired', 'Tired'), ('Frustrated', 'Frustrated')
    ], validators=[DataRequired()])

    intensity = IntegerField('Intensity (1-10)', validators=[
        Optional(), NumberRange(min=1, max=10)
    ])
    tags = StringField('Tags (comma-separated)', validators=[Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])
    submit = SubmitField('Log Mood')