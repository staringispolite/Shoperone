from flask import Flask
app = Flask(__name__)

# Debug mode allows arbitrary execution of code. Never run on prod
app.debug = False

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login")
def login():
    return "login page!"

@app.route("/logout")
def logout():
    return "goodbye"

if __name__ == "__main__":
    # run() for localhost, run('0.0.0.0') to actually listen externally
    #app.run()  
    app.run('0.0.0.0')
