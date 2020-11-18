from flask import Flask, redirect, url_for, render_template
import requests
import json

app = Flask(__name__)

key = ""
url = "http://api.hypixel.net/player?key="

@app.route("/")
def home(name):
    return render_template("index.html")

@app.route("/player/stats/<username>")
def stats(username):
    response = requests.get(url + key + "&name=" + username)
    DisplayName = response.json()["player"]["displayname"]
    return render_template("index.html", username=DisplayName)

if __name__ == "__main__":
    app.run()
