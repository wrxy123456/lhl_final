import keys
import requests as rq
import json
import time
import csv

steam = keys.steam

# Get list of all games with their appids and names
url = "http://api.steampowered.com/ISteamApps/GetAppList/v0002/?key="
res = rq.get(url+steam+"&format=json")
games = res.json()['applist']['apps'][4:]


#error = 5440

# For each game, get description, categories, genres, and save in csv file called 'data.csv'

for i in range(error,len(games)):
    res = rq.get("https://store.steampowered.com/api/appdetails/?appids="+str(games[i]['appid']))
    error = i
    
    if(res.json()[str(games[i]['appid'])]['success']):
        dict = {}
        dict['id'] = games[i]['appid']
        dict['name'] = games[i]['name']
        dict['desc'] = res.json()[str(games[i]['appid'])]['data']['detailed_description']
        try:
            dict['categories'] = res.json()[str(games[i]['appid'])]['data']['categories']
        except KeyError:
            dict['categories'] = ""
        try:
            dict['genres'] = res.json()[str(games[i]['appid'])]['data']['genres']
        except KeyError:
            dict['genres'] = ""
            
        with open('data.csv','a') as file:
            writer = csv.writer(file)
            writer.writerow([dict['id'], dict['name'], dict['desc'], dict['categories'], dict['genres']])
    
    time.sleep(1.5)
    
