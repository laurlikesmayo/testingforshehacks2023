
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("testing.html")

 ##HEAD##


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/aesthetic")
def aesthetic(): 
    return render_template("practice.html")

@app.route("/myform")
def myform(): 
    return render_template("form.html")

@app.route("/testwebsite")
def scrollwebsite() : 
    return render_template("testing.html")

@app.route("/menews")
def menews():
    return render_template("menews.html")

