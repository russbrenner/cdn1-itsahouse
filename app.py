from flask import Flask, request, jsonify, Response, make_response
from functools import wraps
import time

app = Flask(__name__)

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    return Response('Login required', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/dynamic/')
def dynamic():
    return f"Dynamic content. Your IP: {request.remote_addr}"

@app.route('/api/')
def api():
    return jsonify({"time": time.time(), "message": "API response"})

@app.route('/error/404')
def error_404():
    return "Simulated 404 error", 404

@app.route('/error/500')
def error_500():
    return "Simulated 500 error", 500

@app.route('/slow')
def slow():
    time.sleep(5)
    return "Slow response"

@app.route('/custom-headers')
def custom_headers():
    resp = make_response("Custom headers response")
    resp.headers['X-Custom-Header'] = 'Fastly-Test-Server'
    return resp

@app.route('/auth')
@requires_auth
def auth():
    return "Protected area accessed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
