from flask import Flask
from flask import escape, redirect, request, session, url_for
from shoperone import model

app = model._init_model(__name__)


@app.route("/")
def index():
    return _render_index()

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        print "got post"
        if _valid_login(request.form['email'],
                       request.form['password']):
            print "is valid login"
            return _log_user_in(request.form['email'])
        else:
            error = "Invalid username/password"
            return error
    else:
        return _render_login()

@app.route("/logout")
def logout(email):
    return "goodbye"

"""
  Actually logs the user in.
"""
def _log_user_in(email):
    session['email'] = email
    session['username'] = email
    if 'username' in session:
        return "Logged in as %s" % escape(session['username'])
    else:
        return "You are not logged in"

"""
  Returns true if the password hash matches that stored in the DB.
"""
def _valid_login(email, password):
    return True

"""
  Returns the HTML for the home page
"""
def _render_index():
  return """
    Hello world!
    <a href="login">login</a>
  """

"""
  Returns the HTML for the login page
"""
def _render_login():
    print "RENDERING LOGIN"
    return """
        login page!
        <form action="" method="post">
            <p>email<input type=text name=email>
            <p>password<input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    """


if __name__ == "__main__":
    # run() for localhost, run('0.0.0.0') to actually listen externally
    #app.run()  
    app.run('0.0.0.0')
