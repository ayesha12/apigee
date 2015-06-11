from flask import Flask, url_for, Response
import json

app = Flask(__name__)


@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'message'  : 'Hello World!'
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    #resp.headers['Link'] = 'http://luisrei.com'
    return resp

if __name__ == '__main__':
#    app.debug = True
    app.run(threaded=True, host='127.0.0.1', port=8080)

