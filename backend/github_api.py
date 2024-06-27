import requests
import time
import json
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup

CACHE_FILE = Path("github_cache.json")
CACHE_DURATION = 900  # 15 minutes

def load_cache():
    if CACHE_FILE.exists():
        with CACHE_FILE.open('r') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with CACHE_FILE.open('w') as f:
        json.dump(cache, f)

def get_user_commits(username):
    cache = load_cache()
    now = time.time()
    
    if username in cache and now - cache[username]['timestamp'] < CACHE_DURATION:
        return cache[username]['data']

    time.sleep(1)  # Rate limiting
    url = f"https://github.com/users/{username}/contributions"
    headers = {
        'User-Agent': 'GitHubLeaderboard/1.0 (your@email.com)'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch data for {username}: {str(e)}"}

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        today = datetime.now().strftime("%Y-%m-%d")   
        graph = soup.find('div', class_='js-yearly-contributions')
        if not graph:
            return {"error": f"Couldn't find contribution data for {username}"}

        total_contributions = graph.find('h2', class_='f4 text-normal mb-2').text.strip().split()[0]

        today = datetime.now().strftime("%Y-%m-%d")
        today_rect = graph.find('rect', {'data-date': today})
        daily_commits = today_rect['data-count'] if today_rect else "0"

        result = {
            "username": username,
            "daily_commits": int(daily_commits),
            "yearly_contributions": int(total_contributions)
        }

        cache[username] = {'timestamp': now, 'data': result}
        save_cache(cache)

    return result
    
# Example usage
print(get_user_commits("pbrowne011"))
