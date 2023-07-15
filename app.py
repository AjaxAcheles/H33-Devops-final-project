from flask import Flask, render_template, url_for

app = Flask(__name__)
secret_key = "╚É4£1↨E4465╚456123►65╚4848bnjfk♦♦54"

@app.route("/")
def home():
    return render_template("index.html")
