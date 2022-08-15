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
    games_fetched = games_data[int(start_range) : int(final_range)]

    return games_fetched

def create_filter(filter: str = '') -> List[str]:
    filter_handled = filter.replace(' ', '').split(';')
    print(filter_handled)
    if(len(filter) == 0):
        return []
    return filter_handled

def apply_filter(filter: List[str], data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    if(len(filter) == 0 ):
        return data
    filtered_data = []
    for d in data:
        filtered_game = {}
        for field in filter:
            if(not d[field]):
                continue
            filtered_game[field] = d[field]
        filtered_data.append(filtered_game)
    return filtered_data
    
