from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/hello')
def api_hello():
    return 'Hello World!\n'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
