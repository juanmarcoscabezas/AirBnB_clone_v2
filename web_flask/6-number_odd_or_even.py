#!/usr/bin/python3
# render template
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Print Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    """Print HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Print 'c <text>' text will be replace with
       whatever word
    """
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_txt(text='is cool'):
    """Print python something
    """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """verify and print <n> is a number
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """render n if is a number in 5-number.html
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """render n if is a odd or even in 6-number_odd_or_even.html
    """
    test = "{} is odd".format(n)
    if n % 2 == 0:
        test = "{} is even".format(n)
    return render_template('6-number_odd_or_even.html', test=test)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
