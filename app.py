
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", "/home")
def hello():
    return render_template("testing.html")

 ##HEAD##


if __name__ == "__main__":
    app.run(debug=True)
 34dda95fa73b298f7d8a0a83248ed416b6bdca9e
