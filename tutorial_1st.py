from flask import Flask, redirect, url_for
#initiallize flask
app=Flask(__name__)

#first page just on ip, route is /
@app.route("/")
def home():
    return "Hello! this is the main page <h1> Hello <h1>"

#/<name> on ip
@app.route("/<name>")
def user(name):
    return "hello {}".format(name)

#using redirect function , when access /admin it will redirect to "home" fucntion
@app.route("/admin/<name>")
def admin(name):
    return redirect(url_for("user",name=name))
#to access phone as well use ip of server computer
if __name__=="__main__":
    app.run(host='192.168.1.104')