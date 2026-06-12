from playwright.sync_api import sync_playwright
import json
from datetime import datetime

# Le cerveau temporel 
date_du_jour = datetime.now().strftime("%Y-%m-%d")
url_api = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{date_du_jour}"

print(f"Déploiement du Navigateur Fantôme pour la date : {date_du_jour}...")

with sync_playwright() as p:
    # 1. Lancement d'un vrai navigateur Chrome (invisible)
    browser = p.chromium.launch(headless=True)
    
    # On lui donne la signature d'un vrai PC Windows
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
    page = context.new_page()
    
    try:
        # 2. Phase d'approche : On visite le site normal pour valider le JavaScript Challenge de Cloudflare
        print("Étape 1 : Validation du ticket Cloudflare sur la page d'accueil...")
        page.goto("https://www.sofascore.com/", wait_until="domcontentloaded")
        page.wait_for_timeout(3000) # On simule un humain qui regarde la page 3 secondes
        
        # 3. La Frappe : Maintenant qu'on est validé, on attaque le flux JSON
        print("Étape 2 : Extraction des données pures...")
        page.goto(url_api, wait_until="domcontentloaded")
        
        # Le navigateur affiche le JSON dans la page en texte brut, on le copie
        content = page.locator("body").inner_text()
        
        # 4. Vérification et Sauvegarde
        data = json.loads(content)
        with open("donnees_du_jour.json", "w") as f:
            json.dump(data, f)
            
        print(f"✅ BINGO ! Le mur est tombé. Fichier de données sauvegardé pour le {date_du_jour}.")
        
    except Exception as e:
        print(f"❌ Échec de la mission. Rapport d'erreur : {e}")
        # En cas d'échec, on imprime ce que le navigateur a vu pour comprendre
        try:
            print("Aperçu de la page bloquée :", content[:200])
        except:
            pass
        exit(1)
        
    finally:
        browser.close()
