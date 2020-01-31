from flask import Flask, redirect, url_for, render_template,request,session
from datetime import timedelta
#initiallize flask
app=Flask(__name__)
app.secret_key="H3!!0"
app.permanent_session_lifetime=timedelta(minutes=2)
#first page just on ip, route is '/' , used render_template, created a templates folder, with index.html
@app.route("/")
def home():
    return render_template("index.html")
    #use of dynamic content as variables to show on html code

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent=True
        user=request.form['nm']
        session["user"]=user
        return redirect(url_for("user",usr=user))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user=session["user"]
        return render_template("user.html",user=user)
    else:
        return redirect(url_for("login"))

@app.route("/test")
def test():
    return render_template("new.html")

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))
#to access phone as well use ip of server computer
if __name__=="__main__":
    app.run(host='192.168.1.104',debug=True)