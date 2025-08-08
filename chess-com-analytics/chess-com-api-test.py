import requests
import json




import requests
import json

username = "psyborg01"
email_adress= "fabi.c.fischer@gmail.com"
url = f"https://api.chess.com/pub/player/{username}/stats"

headers = {
    f"User-Agent": "MyChessGames ({email_adress})" 
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    stats = response.json()
    print(json.dumps(stats, indent=2))
else:
    print(f"Failed to fetch stats. Status code: {response.status_code}")
