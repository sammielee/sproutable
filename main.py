# Import Flask
from flask import Flask, render_template


# Create the Flask App object
app = Flask(__name__, template_folder='templates')

users = []

# When the default html page is requested
@app.route('/')
def root():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def add_user():
    un = request.form['un']
    user = {
    'un': un,
        'plants': []
    }
    users.append(user)


if __name__ == '__main__':
    app.run()
