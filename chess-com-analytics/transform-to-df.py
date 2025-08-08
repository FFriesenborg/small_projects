import pandas as pd
from pathlib import Path
import re

# Set path to PGN files
my_username = "Psyborg01"
pgn_folder = Path("chess_games")
pgn_files = list(pgn_folder.glob("*.pgn"))

# Store all parsed games
all_games = []

# Regular expression to match tags like [White "Player"]
tag_pattern = re.compile(r'^\[(\w+)\s+"(.*?)"\]')


for pgn_file in pgn_files:
    print(f"Reading {pgn_file.name}")
    with open(pgn_file, "r", encoding="utf-8") as file:
        content = file.read()

        raw_games = content.strip().split("\n\n\n")
        
        for game_pgn in raw_games:
            lines = game_pgn.strip().split("\n")
            game_data = {}

            for line in lines:
                match = tag_pattern.match(line)
                if match:
                    tag, value = match.groups()
                    game_data[tag] = value
                elif line.startswith("1."):
                    game_data["Moves"] = line.strip()
                    break

            # Only insert if not already present
            if "Player Color Me" not in game_data:
                white_player = game_data.get("White", "").lower()
                black_player = game_data.get("Black", "").lower()

                if my_username.lower() == white_player:
                    game_data["Player Color Me"] = "White"
                elif my_username.lower() == black_player:
                    game_data["Player Color Me"] = "Black"
                else:
                    game_data["Player Color Me"] = "Unknown"  # optional fallback

            if game_data:
                all_games.append(game_data)




# Convert to DataFrame
df = pd.DataFrame(all_games)

#create a my result column
def get_my_result(result, my_color):
    if result == "1-0":
        if my_color == "White":
            return "Win"
        elif my_color == "Black":
            return "Loss"
    elif result == "0-1":
        if my_color == "White":
            return "Loss"
        elif my_color == "Black":
            return "Win"
    elif result == "1/2-1/2":
        return "Draw"
    return "Unknown"  # Fallback if data is missing or malformed

if 'My Result' not in df.columns:
    df["My Result"] = df.apply(lambda row: get_my_result(row["Result"], row["Player Color Me"]), axis=1)




#extraact weekday and write in new column
if 'Weekday' not in df.columns:
    # Parse the 'Date' column and extract the weekday
    df["Weekday"] = pd.to_datetime(df["Date"], format="%Y.%m.%d", errors="coerce").dt.day_name()
    
print("game data tranformed to df and saved as csv")


# Save
df.to_csv("chess-com-analytics/all_chess_games.csv", index=False)


