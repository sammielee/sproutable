# Import Flask
from collections import defaultdict
from flask import Flask, render_template, request
from data import greentips
import data.db as db
import data.logging as lg
import datetime


ERROR_MESSAGE = 'Oh no error uwu. You must log in at /login :)'


# Temporary: keep track of users and their addresses
logs = {}


# Create the Flask App object
app = Flask(__name__, template_folder='templates', static_folder='public')


# When the default html page is requested
@app.route('/')
@app.route('/login.html')
def root():
    return render_template('login.html')


# /login will send the form to this URL
@app.route('/home.html', methods=['POST', 'GET'])
def login():
    # Generate green tip
    tip = greentips.get_random_tip()

    if request.method == 'GET':
        if request.remote_addr in logs:
            # If timed out remove from logs
            if logs[request.remote_addr].is_overdue():
                del logs[request.remote_addr]
                return

            addr = request.remote_addr
            logs[addr].log_time()
            
            return render_template('home.html',
                form_data={'acctname' : logs[addr].get_username()},
                tip_header=tip['header'],
                tip_body=tip['body']
            )

        return ERROR_MESSAGE

    if request.method == 'POST':
        form_data = request.form

        # Create new user account
        if not db.data.has_account_by_name(form_data['acctname']):
            acct = db.Account(form_data['acctname'])
            db.data.add_account(acct)
            db.data.write_file()

        # Log the ip address
        if request.remote_addr not in logs:
            logs[request.remote_addr] = lg.Entry(form_data['acctname'])

        return render_template('home.html',
            form_data=form_data,
            tip_header=tip['header'],
            tip_body=tip['body']
        )


# Explore page from home
@app.route('/explore.html')
def explore():
    if request.remote_addr not in logs:
        return ERROR_MESSAGE

    logs[request.remote_addr].log_time()
    
    if logs[request.remote_addr].is_overdue():
        return root()

    return render_template('explore.html')



if __name__ == '__main__':
    try:
        db.data.read_file()
    except:
        db.data.write_file()
    app.run(host='0.0.0.0')
