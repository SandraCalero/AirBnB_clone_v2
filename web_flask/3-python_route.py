#!/usr/bin/python3
"""Script that starts a Flask web application
"""
from flask import Flask, escape
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
