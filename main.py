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

def api(api):
    response = requests.get(api)

    jprint(response.json())
    print(response.status_code)
    print(api)

'''
name = ""
uuid = ""
page = ""

api_key = "http://api.hypixel.net/key?key=" + key
api_name = "http://api.hypixel.net/player?key="+ key + "&name=" + name
api_uuid = "http://api.hypixel.net/player?key="+ key + "&uuid=" + uuid
api_friends = "http://api.hypixel.net/friends?key="+ key + "&uuid=" + uuid
api_auction_total = "http://api.hypixel.net/skyblock/auctions?key="+ key + "&page=" + page
api_auction_player = "http://api.hypixel.net/skyblock/auction?key="+ key + "&uuid=" + uuid
api_gamecounts = "http://api.hypixel.net/gameCounts?key="+ key
'''
key = input("API Key: ")
while True:

    api_function = input("Choose function:\n0) Quit\n1) Get key data\n2) Get player data from username\n3) Get player from UUID\n4) Get friends UUID\n5) Get auction item data\n6) Get player auction data\n7) Get game count data\n")
    if api_function == "1":
        key_api_function = input("API Key: ")
        api_key = "http://api.hypixel.net/key?key=" + key_api_function
        api(api_key)
    elif api_function == "2":
        name = input("Username: ")
        api_name = "http://api.hypixel.net/player?key="+ key + "&name=" + name
        api(api_name)
    elif api_function == "3":
        uuid = input("UUID: ")
        api_uuid = "http://api.hypixel.net/player?key=" + key + "&uuid=" + uuid
        api(api_uuid)
    elif api_function == "4":
        uuid = input("UUID: ")
        api_friends = "http://api.hypixel.net/friends?key=" + key + "&uuid=" + uuid
        api(api_friends)
    elif api_function == "5":
        page = input("Auction pages: ")
        api_auction_total = "http://api.hypixel.net/skyblock/auctions?key=" + key + "&page=" + page
        api(api_auction_total)
    elif api_function == "6":
        uuid = input("UUID: ")
        api_auction_player = "http://api.hypixel.net/skyblock/auction?key=" + key + "&uuid=" + uuid
        api(api_auction_player)
    elif api_function == "7":
        api_gamecounts = "http://api.hypixel.net/gameCounts?key=" + key
        api(api_gamecounts)
    elif api_function == "0":
        break
    else:
        print("API number not found.")