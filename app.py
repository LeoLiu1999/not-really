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
    if not 'loggedin?' in session:
        session['loggedin?'] = True;
        return render_template('form.html', text = 'Please enter your login')
    if (session['loggedin?']):
        return redirect(url_for("welcome"))
    return redirect(url_for("login"))


@app.route("/login", methods = ["POST", "GET"])
def login():
    # already logged in?
    if session['loggedin?']:
        session['user'] = request.cookies.get("username")
        session['pass'] = request.cookies.get("password")
        redirect('/echo')
        return "no redirect"

    # check cookies
    if 'username' in session:
        if 'password' in session:
            if (request.cookies.get("username") == session["username"] and request.cookies.get("password") == session["password"]):
                session["loggedin?"] = True;
                redirect(url_for("welcome"))
        else:
            render_template('form.html', text = "wrong password")
    else:
        render_template('form.html', text = "wrong username")


    # default
    session["loggedin"] = True;
    return render_template('form.html', text = 'Please enter your login')

@app.route("/welcome")
def welcome():
    username = request.cookies.get('username')
    print username
    return render_template("welcome.html", username)

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
