from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

# ROUTES
@app.route('/')
def index():
    return redirect('/user')

@app.route('/user')
def user():
    return render_template('user.html', people=User.get_all())

@app.route('/user/new')
def new():
    return render_template("index.html")

@app.route('/user/add', methods=['POST'])
def add():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.create_user(data)
    return redirect('/user')

@app.route('/user/<int:id>')
def show_user(id):
    data = {
        'id': id
    }
    User.show_user(data)
    return render_template('show_user.html', user = User.show_user(data))

@app.route('/user/<int:id>/update')
def view_page(id):
    data = {
        'id': id
    }
    return render_template('edit.html', user=User.show_user(data))

@app.route('/user/<int:id>/update', methods=["POST"])
def edit(id):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    User.edit_user(data)
    return redirect('/user')



@app.route('/user/<int:id>/destroy')
def destroy(id):
    data = {
        'id': id
    }
    User.delete_user(data)
    return redirect('/user')
    






if __name__ == '__main__':
    app.run(debug=True)