import requests
import json
from datetime import datetime

date_du_jour = datetime.now().strftime("%Y-%m-%d")
url = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{date_du_jour}"

# L'armure complète des headers
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
    'Accept': 'application/json',
    'Accept-Language': 'fr-FR,fr;q=0.9',
    'Referer': 'https://www.sofascore.com/',
    'Origin': 'https://www.sofascore.com',
}

print(f"Lancement de l'attaque avec l'armure complète pour le {date_du_jour}...")

response = requests.get(url, headers=headers, timeout=15)

if response.status_code == 200:
    data = response.json()
    if "events" in data:
        with open("donnees_du_jour.json", "w") as f:
            json.dump(data, f)
        print(f"✅ BINGO ! Le camouflage a fonctionné. {len(data['events'])} matchs extraits.")
    else:
        print("❌ Échec : Cloudflare a renvoyé un faux JSON (Message d'erreur).")
else:
    print(f"❌ Échec. Erreur HTTP : {response.status_code}")
