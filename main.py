# Import Flask
from flask import Flask, render_template, request
from data import greentips
import data.db as db


# Create the Flask App object
app = Flask(__name__, template_folder='templates', static_folder='public')


# When the default html page is requested
@app.route('/')
@app.route('/login')
def root():
    return render_template('login.html')


# /login will send the form to this URL
@app.route('/home', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return 'Oh no error uwu. You must log in at /login :)'

    if request.method == 'POST':
        form_data = request.form

        # Create new user account
        if not db.data.has_account_by_name(form_data['acctname']):
            acct = db.Account(form_data['acctname'])
            db.data.add_account(acct)
            db.data.write_file()

        tip = greentips.get_random_tip()

        return render_template('home.html',
            form_data=form_data,
            tip_header=tip['header'],
            tip_body=tip['body']
        )




if __name__ == '__main__':
    try:
        db.data.read_file()
    except:
        db.data.write_file()
    app.run()
