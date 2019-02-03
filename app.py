from flask import Flask, flash, redirect, render_template, request, session, abort
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from quotes import get_quote

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

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

    if request.method == 'POST' and form.validate():
        name1=request.form['name1']
        email1=request.form['email1']
        name2=request.form['name2']
        email2=request.form['email2']
        print name1, " ", email1, " ", name2, " ", email2
        flash('Thanks for signing up for CloseAway, ' + name1)

    quote = get_quote() #Grab a random quote
    return render_template(
    'test.html',**locals())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1026)
