
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("testing.html")

 ##HEAD##




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


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get('name')
        
    return render_template("form.html")
    

if __name__ == "__main__":
    app.run(debug=True)

