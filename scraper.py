import requests
import json

url = "https://api.sofascore.com/api/v1/sport/football/scheduled-events/2026-06-12"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "*/*",
    "Origin": "https://www.sofascore.com",
    "Referer": "https://www.sofascore.com/"
}

print("Lancement de l'extraction sur les serveurs de GitHub (Azure)...")

response = requests.get(url, headers=headers, timeout=20)

if response.status_code == 200:
    data = response.json()
    # Le robot enregistre les données dans un fichier texte
    with open("donnees_du_jour.json", "w") as f:
        json.dump(data, f)
    print(f"✅ Succès total ! Fichier donnees_du_jour.json créé.")
else:
    print(f"❌ Échec de la connexion. Code : {response.status_code}")
    exit(1) # Fait planter l'action volontairement pour t'alerter
