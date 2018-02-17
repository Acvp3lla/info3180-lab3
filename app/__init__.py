from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['SECRET_KEY'] = 'kingacvp3lla'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''

mail = Mail(app)
mail.init_app(app)
from app import views