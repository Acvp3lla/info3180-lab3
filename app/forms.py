from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, SelectField

from wtforms import validators, ValidationError

class ContactForm(Form):
   name = TextField("Name",[validators.Required("(Required)")])
   
   email = TextField("Email",[validators.Required("(Required)"), validators.Email("(Required)")])
   
   subject = TextField("Subject",[validators.Required("(Required)")])
   
   message = TextAreaField("Message",[validators.Required("(Required)")])
   
   submit = SubmitField("Send")