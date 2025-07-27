from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Welcome</title>
            </head>
            <body>
                <h1>Welcome to the Index Page!</h1>
                <p>This is a simple Flask application.</p>
                <ul>
                    <li><a href="https://flask.palletsprojects.com/">Flask Documentation</a></li>
                    <li><a href="https://github.com/pallets/flask">Flask on GitHub</a></li>
                </ul>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)