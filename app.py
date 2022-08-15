import requests
from typing import List, Dict

def get_games_full_list() -> List[Dict[str, str]]:
    res = requests.get('https://www.freetogame.com/api/games')
    games = res.json()
    return games
    
def create_pagination(page = 1, per_page = 10) -> Dict[str, int]:

    start_range = (page - 1)  * per_page
    final_range = (start_range + per_page) -1

    return {'start_range': start_range, 'final_range': final_range}
