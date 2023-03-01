from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", "/home")
def hello():
    return render_template("testing.html")

if __name__ == "__main__":
    app.run(debug=True)