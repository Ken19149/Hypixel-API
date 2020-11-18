import requests
import json
import time

'''
json.dumps() — Python object -> string
json.loads() — json string -> python object
'''

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def api(api, bool):
    response = requests.get(api)

    if bool == True:
        jprint(response.json())

    print(response.status_code)
    print(api)

key = input("API Key: ")

while True:
    api_function = input("Choose function:\n0) Quit\n1) Get key data\n2) Get player data from username\n3) Get player from UUID\n4) Get friends UUID\n5) Get auction item data\n6) Get player auction data\n7) Get game count data\n8) Get player last seen\n9) Get player count online\n10) Get latest skyblock news\n")
    if api_function == "1":
        key_api_function = input("API Key: ")
        api_key = "http://api.hypixel.net/key?key=" + key_api_function
        api(api_key, True)
    elif api_function == "2":
        name = input("Username: ")
        api_name = "http://api.hypixel.net/player?key="+ key + "&name=" + name
        api(api_name, True)
    elif api_function == "3":
        uuid = input("UUID: ")
        api_uuid = "http://api.hypixel.net/player?key=" + key + "&uuid=" + uuid
        api(api_uuid, True)
    elif api_function == "4":
        uuid = input("UUID: ")
        api_friends = "http://api.hypixel.net/friends?key=" + key + "&uuid=" + uuid
        api(api_friends, True)
    elif api_function == "5":
        page = input("Auction pages: ")
        api_auction_total = "http://api.hypixel.net/skyblock/auctions?key=" + key + "&page=" + page
        api(api_auction_total, True)
    elif api_function == "6":
        uuid = input("UUID: ")
        api_auction_player = "http://api.hypixel.net/skyblock/auction?key=" + key + "&uuid=" + uuid
        api(api_auction_player, True)
    elif api_function == "7":
        api_gamecounts = "http://api.hypixel.net/gameCounts?key=" + key
        api(api_gamecounts, True)
    elif api_function == "8":
        name = input("Username: ")
        api_name = "http://api.hypixel.net/player?key=" + key + "&name=" + name
        response = requests.get(api_name)
        try:
            last_login = response.json()["player"]["lastLogin"]
            last_logout = response.json()["player"]["lastLogout"]
        except:
            print("Error")
            continue

        unix_timestamp_login = last_login / 1000
        unix_timestamp_logout = last_logout / 1000

        utc_time_login = time.gmtime(unix_timestamp_login)
        local_time_login = time.localtime(unix_timestamp_login)

        utc_time_logout = time.gmtime(unix_timestamp_logout)
        local_time_logout = time.localtime(unix_timestamp_logout)

        if unix_timestamp_login > unix_timestamp_logout:
            print(name, "is online.")
        elif unix_timestamp_login < unix_timestamp_logout:
            print("Last seen(local time): from " + time.strftime("%Y-%m-%d %H:%M:%S",
                                                             local_time_login) + " to " + time.strftime(
            "%Y-%m-%d %H:%M:%S", local_time_logout))
            print(
            "Last seen(UTC): from " + time.strftime("%Y-%m-%d %H:%M:%S (UTC)", utc_time_login) + " to " + time.strftime(
                "%Y-%m-%d %H:%M:%S (UTC)", utc_time_logout))

        if response.status_code == 200:
            print("Success")
        else:
            print("Error")
    elif api_function == "9":
        api_player_count = "http://api.hypixel.net/playerCount?key=" + key
        response = requests.get(api_player_count)
        print("Player: " + response.json()["playerCount"])
    elif api_function == "10":
        api_news = "http://api.hypixel.net/skyblock/news?key=" + key

        response = requests.get(api_news)

        print(response.json()["items"][0]["title"])
        print(response.json()["items"][0]["text"])
        print(response.json()["items"][0]["link"])
    elif api_function == "0":
        break
    else:
        print("ERROR")