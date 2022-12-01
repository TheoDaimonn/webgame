from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField

class Form(FlaskForm):
    round = StringField("текст раунда")
    submit = SubmitField('раунд')

def check(text):
    arr = set(list('млцхдзгцеыпипатволж'))
    k = 0
    for i in text:
        if i in arr:
            k += 1
    if k / len(text) >=0.5:
        return True
    else:return False