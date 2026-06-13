import requests
import json
from datetime import datetime

date_du_jour = datetime.now().strftime("%Y-%m-%d")
url = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{date_du_jour}"

# Le camouflage parfait : On annonce au pare-feu que c'est un iPhone qui navigue
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
}

print(f"Lancement de l'attaque depuis l'iPhone pour le {date_du_jour}...")

response = requests.get(url, headers=headers, timeout=15)

if response.status_code == 200:
    data = response.json()
    if "events" in data:
        with open("donnees_du_jour.json", "w") as f:
            json.dump(data, f)
        print(f"✅ BINGO ! Le pare-feu est tombé. L'IP mobile a fonctionné. {len(data['events'])} matchs extraits.")
    else:
        print("❌ Échec : Le pare-feu a renvoyé un faux JSON (Message d'erreur).")
else:
    print(f"❌ Échec. Erreur HTTP : {response.status_code}")
