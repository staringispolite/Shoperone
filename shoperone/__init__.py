from flask import Flask
from flask import escape, redirect, render_template, request, session, url_for
from shoperone import model
from shoperone import lib

app = model._init_model(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if _valid_login(request.form['email'],
                       request.form['password']):
            return _log_user_in(request.form['email'])
        else:
            error = "Invalid username/password"
            return error
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


"""
  Actually logs the user in.
"""
def _log_user_in(email):
    user = model.User.query.filter_by(email=email).first()
    if user:
        session['user'] = user
        return redirect(url_for('index'))
    else:
        return "You are not logged in"


"""
  Returns true if the password hash matches that stored in the DB.
"""
def _valid_login(email, password):
    user = model.User.query.filter_by(email=email).first()
    password_hash = lib._hash_password(password) 
    return user.password_hash == password_hash


if __name__ == "__main__":
    # run() for localhost, run('0.0.0.0') to actually listen externally
    #app.run()  
    app.run('0.0.0.0')
