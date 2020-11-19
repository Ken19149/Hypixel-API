from flask import Flask, redirect, url_for, render_template, request
import requests
import json
import os
import time

app = Flask(__name__)

key = ""
url = "http://api.hypixel.net/player?key="

def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)

@app.route("/", methods = ["POST", "GET"])
def home():
    context = {"server_time": format_server_time()}
    if request.method == "POST":
        username = request.form["username"]
        return redirect(url_for("stats", username=username))
    else:
        return render_template("index.html", context=context)

@app.route("/player/stats/<username>", methods = ["POST", "GET"])
def stats(username):
    context = {"server_time": format_server_time()}
    if request.method == "POST":
        username = request.form["username"]
        return redirect(url_for("stats", username=username))
    elif username != None:
        response = requests.get(url + key + "&name=" + username)
        player = {"displayname": response.json()["player"]["displayname"]}
        return render_template("stats.html", username=player, context=context)
    else:
        return redirect(url_for("home"))

if __name__ == "__main__":
#    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    app.run(debug=True)
