import requests
from typing import List, Dict

def get_games_full_list() -> List[Dict[str, str]]:
    res = requests.get('https://www.freetogame.com/api/games')
    games = res.json()
    return games
    
def create_pagination(page = 1, per_page = 10) -> Dict[str, int]:

    start_range = (int(page) - 1)  * int(per_page)
    final_range = int((start_range + per_page)) - 1

    return {'start_range': start_range, 'final_range': final_range}

def parse_games_full_list(page = 1, per_page = 10) -> List[Dict[str, str]]:
    games_data = get_games_full_list()
    pagination = create_pagination(page, per_page)

    start_range, final_range = pagination['start_range'], pagination['final_range']
    games_fetched = games_data[int(start_range) : int(final_range) if int(final_range) < len(games_data) else len(games_data)]

    return games_fetched

def create_filter(filter: str = '') -> List[str]:

    if(len(filter) == 0):
        return []
    filter_handled = filter.replace(' ', '').split(';')
    return filter_handled

def apply_filter(filter: List[str], data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    if(len(filter) == 0 ):
        return data
    filtered_data = []
    for d in data:
        filtered_game = {}
        for field in filter:
            if(field in d):
                filtered_game[field] = d[field]
        if(filtered_game):
            filtered_data.append(filtered_game)        
    if(len(filtered_data) == 0):
        return []
    return filtered_data
