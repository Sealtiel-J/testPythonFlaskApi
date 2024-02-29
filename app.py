# app.py

from flask import render_template, send_from_directory
import connexion
import os

app = connexion.App(__name__, specification_dir=os.getcwd())
app.add_api("swagger.yml")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.getcwd(), 'favicon.png', mimetype='image/x-icon')


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
