from flask import Flask, render_template, session, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def root():
    print 'check for session...'
    if 'username' in session:
        print 'passed check for session, redirect to login'
        return redirect(url_for("login"))
    else:
        print 'passed check for session, redirect to welcome'
        return redirect(url_for("welcome"))
@app.route("/login")
def login():
    return render_template(form.html)

@app.route("/welcome")
def welcome():
    username = request.cookies.get('username')
    print username
    return render_template("welcome.html", username)

if __name__ == "__main__":
    app.debug = True
    app.run()
