import requests
import json
from datetime import datetime

# 1. Le cerveau temporel : on récupère la date exacte du moment de l'exécution
date_du_jour = datetime.now().strftime("%Y-%m-%d")

# 2. L'URL dynamique (remarque le 'f' avant les guillemets et la variable à la fin)
url = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{date_du_jour}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "*/*",
    "Origin": "https://www.sofascore.com",
    "Referer": "https://www.sofascore.com/"
}

print(f"Lancement de l'extraction sur GitHub pour la date : {date_du_jour}...")

response = requests.get(url, headers=headers, timeout=20)

if response.status_code == 200:
    data = response.json()
    with open("donnees_du_jour.json", "w") as f:
        json.dump(data, f)
    print(f"✅ Succès total ! Fichier donnees_du_jour.json mis à jour pour le {date_du_jour}.")
else:
    print(f"❌ Échec de la connexion. Code : {response.status_code}")
    exit(1) # Le script se saborde pour déclencher l'alerte d'échec
