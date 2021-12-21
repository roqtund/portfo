from flask import Flask, render_template, request, redirect
import csv
import smtplib
from mailer import Mailer
app = Flask(__name__)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(
            f'\n email: {email}, subject: {subject}, message: {message} ')


def send_email(email):
    try:
        msg = '''Thanks for contacting me.I\'ll be in touch with you shortly'''
        mail = Mailer(email='hello.roqeeb@gmail.com', password='FcidKiwas@12!')
        mail.send(receiver=f'{email}', subject='Acknowledgement', message=f'{msg}')

        print('Email sent.')
    except Exception as e:
        print(e)

    



def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

   


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<endpoint>')
def render(endpoint=None):
    return render_template(endpoint)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()

            write_to_csv(data)

            send_email(data['email'])


            return redirect('/thank_you.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again'


