# Import Flask
from flask import Flask, render_template, request
from data import greentips


# Create the Flask App object
app = Flask(__name__, template_folder='templates', static_folder='public')

users = []

# When the default html page is requested
@app.route('/')
@app.route('/login')
def root():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def add_user():
    un = request.form['un']
    user = {
        'un': un,
        'plants': [],
        'water_times': []
    }
    users.append(user)


@app.route('/home', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return 'Oh no error uwu'
    if request.method == 'POST':
        form_data = request.form

        tip = greentips.get_random_tip()

        return render_template('home.html',
            form_data=form_data,
            tip_header=tip['header'],
            tip_body=tip['body']
        )


if __name__ == '__main__':
    app.run()
