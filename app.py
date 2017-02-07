from flask import Flask, render_template
from forms import LoginForm
from forms import RegistrationForm

app = Flask(__name__)
app.config.from_object('config')
 
@app.route("/")
def index():
	user = {'nickname': 'william'}  # fake user
	return render_template('index.html', title="Home", user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', 
			title='Sign In',
			form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	return render_template('Registration.html',
			title='Register',
			form=form)



if __name__ == '__main__':
    app.run()
