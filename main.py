import json
import requests

source_json_url = "https://cdn.jsdelivr.net/gh/gn-math/assets/zones.json"
HTML_URL = "https://cdn.jsdelivr.net/gh/gn-math/html@main"
ICON_URL = "https://raw.githubusercontent.com/Instel12/Astria-Repo/refs/heads/main/icon.png"

response = requests.get(source_json_url)
zones = response.json()

repo = {
    "title": "Astria",
    "icon": ICON_URL,
    "games": []
}

for zone in zones:
    if zone.get("id", 0) < 0:
        continue
    
    game_entry = {
        "title": zone["name"],
        "url": zone["url"].replace("{HTML_URL}", HTML_URL)
    }
    repo["games"].append(game_entry)

with open("repo.json", "w", encoding="utf-8") as f:
    json.dump(repo, f, ensure_ascii=False, indent=4)
