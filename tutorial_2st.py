from flask import Flask, redirect, url_for, render_template
#initiallize flask
app=Flask(__name__)

#first page just on ip, route is '/' , used render_template, created a templates folder, with index.html
@app.route("/<name>")
def home(name):
    return render_template("index.html",content=name,l=["ali","ahmed","asim"])
    #use of dynamic content as variables to show on html code

#to access phone as well use ip of server computer
if __name__=="__main__":
    app.run(host='192.168.1.104')