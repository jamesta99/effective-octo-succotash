from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtform.validators import DataRequired

class MessageForm(FlaskForm):
   author = StringField('Author', validators=[DataRequired()])
   message = StringField('Message', validators=[DataRequired()])
   submit = SubmitField('Send')
