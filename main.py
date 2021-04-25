# Import Flask
from flask import Flask, render_template, request


# Create the Flask App object
app = Flask(__name__, template_folder='templates')

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


@app.route('/myplants', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return 'Oh no error uwu'
    if request.method == 'POST':
        form_data = request.form
        return render_template('myplants.html', form_data=form_data)


if __name__ == '__main__':
    app.run()
