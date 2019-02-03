#TODO: Include preference for duration
#TODO: Include txt preference
#TODO: Upload everything to google platform somewhere

from flask import Flask, flash, redirect, render_template, request, session, abort
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from flask_mail import Mail,  Message
import logging
import get_prompt
import os
import emoji

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
mail=Mail(app)
app.config.update(
DEBUG = True,
MAIL_SERVER = 'smtp.gmail.com',
MAIL_PORT = 587,
MAIL_USE_TLS = True,
MAIL_USE_SSL = False,
MAIL_USERNAME = 'closest.away@gmail.com',
MAIL_PASSWORD = 'choomahMaster')
mail = Mail(app)

class ReusableForm(Form):
    name1 = TextField('What is your name?:',
        validators=[validators.required(), validators.Length(min=3, max=35)])
    email1 = TextField('Email?:',
        validators=[validators.DataRequired(), validators.Email(), validators.required()])
    name2 = TextField("'What is your friend's name?:'",
        validators=[validators.required(), validators.Length(min=3, max=35)])
    email2 = TextField("'What is your friend's email?:'",
        validators=[validators.DataRequired(), validators.Email(), validators.required()])

@app.route("/", methods = ['GET', 'POST'])
def index():
    form = ReusableForm(request.form)
    print(form.errors)

    dropdownOptions = ['Email','Text']

    if request.method == 'POST' and form.validate():
        name1=request.form['name1']
        email1=request.form['email1']
        name2=request.form['name2']
        email2=request.form['email2']
        comm = request.form["communication"]
        flash('Thanks for signing up for CloseAway, ' + name1)

        if (comm == "Email"):
            FROM =  'closest.away@gmail.com'
            SUBJECT = "Your daily CloseAway prompt"
            TEXT = get_prompt.pick_prompt()
            message = 'This is your daily CloseAway prompt\nIt is being sent to %s and %s\n\n%s\nMade with :heart:, from your friends at CloseAway' % (email1, email2, TEXT)

            msg = Message('Your Daily CloseAway Prompt', sender = FROM, recipients = [email1, email2])
            msg.body = emoji.emojize(message, use_aliases=True)
            mail.send(msg)

    else:
        flash('All form fields are required. ')

    return render_template(
    'test.html',**locals())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1026)
