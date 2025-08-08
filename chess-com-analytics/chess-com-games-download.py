import requests
from datetime import datetime
from pathlib import Path

#--------insert info---------
username = "example_username"
email_adress= "example_email@adress"
#----------------------------

headers = {
    f"User-Agent": "MyChessGames ({email_adress})" 
}

output_dir = Path("chess_games")
output_dir.mkdir(exist_ok=True)

#date range
start_date = datetime(2023, 1, 1)
end_date = datetime.today()

current = start_date
while current <= end_date:
    year = current.year
    month = current.month
    formatted_month = f"{month:02}"
    
    url = f"https://api.chess.com/pub/player/{username}/games/{year}/{formatted_month}/pgn"
    print(f"Downloading: {url}")
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200 and response.text.strip():
        filename = output_dir / f"games_{year}_{formatted_month}.pgn"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Saved to {filename}")
    else:
        print(f"No games found or error for {year}-{formatted_month}")
    
    # Increment month
    if month == 12:
        current = current.replace(year=year + 1, month=1)
    else:
        current = current.replace(month=month + 1)
