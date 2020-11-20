from flask import Flask, redirect, url_for, render_template, request, sessions
import requests
import json
import os
import time
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "123"
app.permanent_session_lifetime = timedelta(days=7)

key = ""
url = "http://api.hypixel.net/player?key="

def isPlayerExist(username):
    response = requests.get(url + key + "&name=" + username)
    if response.json()["success"] == True and response.json()["player"] == None:
        return False
    elif response.json()["success"] == True and response.json()["player"] != None:
        return True
    else:
        return False

def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)

@app.route("/", methods = ["POST", "GET"])
def home():
    context = {"server_time": format_server_time()}
    if request.method == "POST" and request.form["username"] != "" and isPlayerExist(request.form["username"]):
        username = request.form["username"]
        return redirect(url_for("stats", username=username))
    else:
        return render_template("index.html", context=context)

@app.route("/player/stats/<username>", methods = ["POST", "GET"])
def stats(username):
    context = {"server_time": format_server_time()}
    if request.method == "POST" and request.form["username"] != "" and isPlayerExist(request.form["username"]):
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
