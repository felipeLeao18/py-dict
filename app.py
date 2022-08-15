import requests
from typing import List, Dict

def get_games_full_list() -> List[Dict[str, str]]:
    res = requests.get('https://www.freetogame.com/api/games')
    games = res.json()
    return games
    
