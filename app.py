# Leo Liu Charles Weng
# SoftDev1
# HW07 - Login
# 10-5-17

# this doesn't make sense :C - charles

from flask import Flask, render_template, session, url_for, redirect, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route("/")
def root():
    # check if logged in
    if not 'loggedin?' in session:
        session['loggedin?'] = True;
        return render_template('form.html', text = 'Please enter your login')
    # has session data already
    return redirect(url_for("login"))


@app.route("/login", methods = ["POST", "GET"])
def login():
    # default (you got here by accident)
    if not 'loggedin?' in session:
        session["loggedin?"] = True;
        return render_template('form.html', text = 'Please enter your login')

    # logged in means there's form data
    if session['loggedin?']:
        session['user'] = request.form.get("username")
        session['pass'] = request.form.get("password")

    # check credentials
    usercheck = False
    passcheck = False
    if 'username' in session:
        if (session["user"] == "mr brown"):
            usercheck = True
    if 'password' in session:
        if (session["pass"] == "13"):
            passcheck = True

    if (usercheck and passcheck):
        return redirect("/welcome")
    elif(usercheck and not passcheck):
        session['loggedin?'] = True
        return render_template('form.html', text = "wrong password")
    elif(not usercheck and passcheck):
        session['loggedin?'] = True
        return render_template('form.html', text = "wrong username")
    session['loggedin?'] = True
    return render_template('form.html', text = "wrong username and password")


@app.route("/welcome")
def welcome():
    user = session.get('user')
    return render_template("welcome.html", username = user)

@app.route("/signout")
def signout():
    session.pop("user")
    session.pop("pass")
    session['loggedin?'] = False
    return redirect("/")

def debug():
    print "\n\n\n"
    print "session:"
    print session
    print "app:"
    print app
    print "\nrequest.headers:"
    print request.headers
    print "\nrequest.method:"
    print request.method
    print "\nrequest.args:"
    print request.args
    print "\nrequest.form:"
    print request.form

if __name__ == "__main__":
    app.debug = True
    app.run()
