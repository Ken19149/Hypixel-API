import requests
import json

'''
json.dumps() — Python object -> string
json.loads() — json string -> python object
'''

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


key = "" #Put hypixel api key here

name = "Ken980"
uuid = "d9f7aa7d-4a0c-48db-a3d8-1cc03fdaaa6d"
page = "1"

api_key = "http://api.hypixel.net/key?key="+ key
api_name = "http://api.hypixel.net/player?key="+ key + "&name=" + name
api_uuid = "http://api.hypixel.net/player?key="+ key + "&uuid=" + uuid
api_friends = "http://api.hypixel.net/friends?key="+ key + "&uuid=" + uuid
api_auction_total = "http://api.hypixel.net/skyblock/auctions?key="+ key + "&page=" + page
api_auction_player = "http://api.hypixel.net/skyblock/auction?key="+ key + "&uuid=" + uuid
api_gamecounts = "http://api.hypixel.net/gameCounts?key="+ key

def api(api):
    response = requests.get(api)

    jprint(response.json())
    print(response.status_code)
    print(api)

api(api_key)