# Import Flask
from flask import Flask, render_template


# Create the Flask App object
app = Flask(__name__, template_folder='templates')


# When the default html page is requested
@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()