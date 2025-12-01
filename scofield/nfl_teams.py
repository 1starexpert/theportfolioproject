import requests

url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLPlayerList"

headers = {
	"x-rapidapi-key": "4be5895297mshed28dc514b382c8p196083jsn19a5395f1322",
	"x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
