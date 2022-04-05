from flask import Flask, render_template, redirect
from user import User
app = Flask(__name__)

# ROUTES
@app.route('/')
def index():
    return redirect('/user')

@app.route('/user')
def user():
    return render_template('user.html', people=User.get_all())



if __name__ == '__main__':
    app.run(debug=True)