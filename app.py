import os
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def run():
    app.run(host='0.0.0.0',
            port=os.getenv('PORT', 8080))


def debug():
    app.run(host='0.0.0.0',
            port=4000)


if __name__ == '__main__':
    run()
