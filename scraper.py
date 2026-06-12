from curl_cffi import requests
import json
from datetime import datetime

# 1. Le cerveau temporel 
date_du_jour = datetime.now().strftime("%Y-%m-%d")

# 2. L'URL dynamique
url = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{date_du_jour}"

print(f"Lancement de l'extraction furtive (Signature Chrome) pour la date : {date_du_jour}...")

# L'assaut avec usurpation d'identité cryptographique
response = requests.get(url, impersonate="chrome110", timeout=30)

if response.status_code == 200:
    data = response.json()
    with open("donnees_du_jour.json", "w") as f:
        json.dump(data, f)
    print(f"✅ Succès total ! Le pare-feu a été contourné. Fichier mis à jour pour le {date_du_jour}.")
else:
    print(f"❌ Échec de la connexion. Code : {response.status_code}")
    exit(1)
