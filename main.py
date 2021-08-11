"""Personal web based name card

A web application that creates a web based name card
using a personalized HTML, CSS and JS template from HTML5 Up.

This script requires that 'flask' be installed within the Python
environment you are running this script in.

"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def run_website():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)