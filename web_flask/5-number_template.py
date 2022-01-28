#!/usr/bin/python3
"""Script that starts a Flask web application
"""
from flask import Flask, escape, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def displayHelloHBNB():
    """Display 'Hello HBNB!'

    Returns:
        [string]: Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', methods=['GET'])
def displayHBNB():
    """Display “HBNB”

    Returns:
        [string]: HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', methods=['GET'])
def displayC_text(text):
    """Display “C” followed by the value of the text variable
    (replace underscore _ symbols with a space )

    Returns:
        [string]: “C” followed by the value of the text variable
    """
    return 'C {}'.format(escape(text)).replace('_', ' ')


@app.route('/python', defaults={'text': "is cool"})
@app.route('/python/<text>')
def displayPython_text(text):
    """Display “Python” followed by the value of the text variable
    (replace underscore _ symbols with a space )

    Returns:
        [string]: “Python” followed by the value of the text variable.
        The default value of text is “is cool”
    """
    return 'Python {}'.format(escape(text)).replace('_', ' ')


@app.route('/number/<int:n>')
def display_n_is_a_number(n):
    """Display “n is a number” only if n is an integer

    Returns:
        [string]: “n is a number” only if n is an integer
    """
    return '{} is a number'.format(escape(n))


@app.route('/number_template/<int:n>')
def display_HTML(n: int):
    """Display a HTML page only if n is an integer.
    H1 tag: “Number: n” inside the tag BODY

    Returns:
        [string]: a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
