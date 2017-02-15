from flask import jsonify, render_template, request, Response, session
from stockserver import app
import uuid
import hashlib
import sqlcommand as sql

# register done
# login
# logout

@app.route("/")
def index():
    user = {'nickname': 'Guest'}
    return render_template('index.html', title="Home", user=user)

# repeat user not yet process
@app.route('/register', methods=['GET'])
def register():
    data = {
        'status'  : 'register',
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp

@app.route('/api/register', methods=['POST'])
def api_register():
    username = request.form['username']
    password = request.form['password']
    salt = create_salt()
    hash_password = hash(password, salt)
    sql.create_user(username, hash_password, salt)
    message = {
        'username':username,
        'password':hash_password,
        'status': True
    }
    return jsonify(message)

@app.route('/api/login', methods=['POST'])
def api_login():
    username = request.form['username']
    hash_password, salt = sql.filter(username)
    password = request.form['password']

    session['username'] = username

    if check(hash_password, password, salt):
        status = True
    else:
        status = False

    message = {
        'session':session['username'],
        'login status':status
    }

    return jsonify(message)

@app.route('/login', methods=['GET'])
def login():
    data = {
        'status'  : 'login',
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp

@app.route('/logout/<string:username>', methods=['GET'])
def logout(username):
    message = {
	    'username':username,
	    'status' :'logout'
	}
    resp = jsonify(message)
    resp.status_code = 200

    return resp

@app.route('/api/logout', methods=['POST'])
def api_logout():
    session.pop('username', None)
    message = {
        'session':'pop username',
	    'status' :'logout'
	}
    resp = jsonify(message)
    resp.status_code = 200

    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

def create_salt():
    return uuid.uuid4().hex

def hash(word, salt):
    return (hashlib.md5((word + salt).encode()).hexdigest())

def check(hash_password, user_password, salt):
    return hash_password == hash(user_password, salt)

# test
def test_hash():
    salt = "c33d6b6f45864925bb86cbba04a308b9"
    hash_password = "6569880915e9ec7cbebf80b6fba4bbeb"
    assert check(hash_password, "123", salt)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
