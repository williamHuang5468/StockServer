from flask import Flask, jsonify, render_template
import uuid
import hashlib

app = Flask(__name__)
app.config.from_object('config')
 
@app.route("/")
def index():
    user = {'nickname': 'Guest'}
    return render_template('index.html', title="Home", user=user)

@app.route('/register/<string:username>/<string:password>')
def register(username, password):
    pass

@app.route('/login/<string:username>/<string:password>', methods=['GET', 'POST'])
def login(username, password):
    session = username
    d = {
	    'username':username,
	    'password':password,
	    'status'  :'login'
	}

    return jsonify(d)


@app.route('/logout/<string:username>')
def logout(username):
    session.pop('username', None)
    d = {
	    'username':username,
	    'status' :'logout'
	}
    return jsonify(d)

def create_salt():
    return uuid.uuid4().hex

def hash(word, salt):
    return (hashlib.md5((word + salt).encode()).hexdigest())

def check(hash_password, user_password, salt):
    return hash_password == md5(user_password + salt)

if __name__ == '__main__':
    app.run()
