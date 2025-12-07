#!/usr/bin/env python3
"""
🔓 DÉCRYPTEUR OFFICIEL - RANSONLOCKER V1.0
Description: Décrypte les fichiers après paiement de la rançon
AVERTISSEMENT: Code éducatif uniquement
"""

import os
import sys
import time
from pathlib import Path
from cryptography.fernet import Fernet
from datetime import datetime


class RansomwareDecryptor:
    """Décrypteur officiel pour les fichiers chiffrés"""
    
    def __init__(self):
        """Initialise le décrypteur"""
        self.key = None
        self.decrypted_count = 0
        self.failed_count = 0
        self.key_filename = "my_key.key"
        
    def _clear_screen(self):
        """Efface l'écran"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_decryptor_banner(self):
        """Affiche le banner du décrypteur"""
        self._clear_screen()
        banner = """
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ██████╗ ███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗     ║
║   ██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝     ║
║   ██║  ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║        ║
║   ██║  ██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║        ║
║   ██████╔╝███████╗╚██████╗██║  ██║   ██║   ██║        ██║        ║
║   ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝        ║
║                                                                  ║
║              🔓 DÉCRYPTEUR OFFICIEL V1.0 🔓                      ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
        print("\033[92m" + banner + "\033[0m")  # Vert
    
    def verify_payment(self):
        """Simule la vérification du paiement"""
        print("\n\033[93m[*] Vérification du paiement...\033[0m")
        time.sleep(2)
        
        # En production, ceci contacterait le serveur C2
        print("\033[92m[✓] Paiement vérifié avec succès\033[0m")
        print("\033[92m[✓] Transaction confirmée sur la blockchain\033[0m")
        time.sleep(1)
    
    def load_decryption_key(self):
        """Charge la clé de déchiffrement"""
        print("\n\033[93m[*] Chargement de la clé de déchiffrement...\033[0m")
        time.sleep(1)
        
        if not os.path.exists(self.key_filename):
            print("\033[91m[✗] ERREUR: Fichier de clé introuvable!\033[0m")
            print("\033[91m[!] Sans la clé, le déchiffrement est impossible.\033[0m")
            print("\n\033[93mContactez le support: recovery@example.sth\033[0m")
            sys.exit(1)
        
        try:
            with open(self.key_filename, "rb") as key_file:
                self.key = key_file.read()
            print("\033[92m[✓] Clé de déchiffrement chargée avec succès\033[0m")
        except Exception as e:
            print(f"\033[91m[✗] Erreur lors du chargement de la clé: {e}\033[0m")
            sys.exit(1)
    
    def scan_encrypted_files(self):
        """Scanne les fichiers chiffrés (.locked)"""
        print("\n\033[93m[*] Scan des fichiers chiffrés...\033[0m")
        time.sleep(1)
        
        encrypted_files = []
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(".locked"):
                    filepath = os.path.join(root, file)
                    encrypted_files.append(filepath)
        
        if not encrypted_files:
            print("\033[93m[!] Aucun fichier chiffré trouvé.\033[0m")
            return []
        
        print(f"\033[92m[✓] {len(encrypted_files)} fichier(s) chiffré(s) détecté(s)\033[0m")
        return encrypted_files
    
    def decrypt_file(self, filepath):
        """Déchiffre un fichier individuel"""
        try:
            # Lire le contenu chiffré
            with open(filepath, "rb") as f:
                encrypted_data = f.read()
            
            # Déchiffrer
            fernet = Fernet(self.key)
            decrypted_data = fernet.decrypt(encrypted_data)
            
            # Restaurer le nom original (enlever .locked)
            original_filepath = filepath[:-7]  # Enlever ".locked"
            
            # Écrire les données déchiffrées
            with open(original_filepath, "wb") as f:
                f.write(decrypted_data)
            
            # Supprimer le fichier chiffré
            os.remove(filepath)
            
            return True
        except Exception as e:
            return False
    
    def decrypt_all_files(self, files):
        """Déchiffre tous les fichiers avec barre de progression"""
        print("\n\033[92m[*] DÉCHIFFREMENT EN COURS...\033[0m\n")
        
        for i, filepath in enumerate(files, 1):
            filename = os.path.basename(filepath)
            
            if self.decrypt_file(filepath):
                self.decrypted_count += 1
                status = "\033[92m✓\033[0m"
            else:
                self.failed_count += 1
                status = "\033[91m✗\033[0m"
            
            # Barre de progression
            progress = int((i / len(files)) * 50)
            bar = "█" * progress + "░" * (50 - progress)
            percentage = (i / len(files)) * 100
            
            print(f"\r\033[92m[{bar}] {percentage:.1f}% | {status} {filename}\033[0m", end="")
            time.sleep(0.1)
        
        print("\n")
    
    def display_success_message(self):
        """Affiche le message de succès"""
        print("\033[92m" + "="*70)
        print("║ DÉCHIFFREMENT TERMINÉ")
        print("="*70 + "\033[0m\n")
        
        print(f"\033[92m✅ Fichiers restaurés: {self.decrypted_count}\033[0m")
        if self.failed_count > 0:
            print(f"\033[91m❌ Échecs: {self.failed_count}\033[0m")
        
        print(f"\n\033[93m📅 Date de récupération: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m")
        
        print("\n\033[92m╔══════════════════════════════════════════════════════════════════╗")
        print("║            VOS FICHIERS ONT ÉTÉ RESTAURÉS AVEC SUCCÈS            ║")
        print("╚══════════════════════════════════════════════════════════════════╝\033[0m\n")
        
        print("\033[93m💡 Conseils de sécurité pour l'avenir:\033[0m")
        print("   • Installez un antivirus à jour")
        print("   • Effectuez des sauvegardes régulières")
        print("   • Ne cliquez pas sur des liens suspects")
        print("   • Mettez à jour vos logiciels régulièrement")
        print("   • Utilisez des mots de passe forts\n")
        
        print("\033[92m✨ Merci d'avoir fait confiance à nos services de récupération.\033[0m")
        print("\033[93m📧 Support technique: recovery@example.sth\033[0m\n")
    
    def cleanup(self):
        """Nettoie les fichiers de rançon"""
        print("\033[93m[*] Nettoyage des fichiers de rançon...\033[0m")
        
        files_to_remove = [
            "README_RANSOM.txt",
            "RANSOM_NOTE.html",
            "DECRYPT_INSTRUCTIONS.txt"
        ]
        
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)
                print(f"\033[92m[✓] Supprimé: {file}\033[0m")
        
        time.sleep(1)
    
    def run(self):
        """Exécute le processus de déchiffrement"""
        # Banner
        self.display_decryptor_banner()
        
        print("\n\033[93m" + "="*70)
        print("⚠️  DÉCRYPTEUR OFFICIEL - CRYPTOLOCKER V4.0 ⚠️")
        print("="*70 + "\033[0m\n")
        
        # Vérification du paiement
        self.verify_payment()
        
        # Chargement de la clé
        self.load_decryption_key()
        
        # Scan des fichiers
        files = self.scan_encrypted_files()
        
        if not files:
            print("\n\033[93m[!] Rien à déchiffrer. Vos fichiers sont peut-être déjà restaurés.\033[0m")
            return
        
        # Confirmation
        print(f"\n\033[92m[!] {len(files)} fichier(s) vont être déchiffrés [!]\033[0m")
        confirm = input("\nAppuyez sur ENTRÉE pour continuer (ou Ctrl+C pour annuler)...")
        
        # Déchiffrement
        self.decrypt_all_files(files)
        
        # Message de succès
        self.display_success_message()
        
        # Nettoyage
        self.cleanup()
        
        print("\n\033[92m✅ Processus terminé avec succès!\033[0m\n")


def main():
    """Point d'entrée principal"""
    decryptor = RansomwareDecryptor()
    decryptor.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[91m[!] Déchiffrement interrompu.\033[0m")
        print("\033[93m[!] Vos fichiers restent chiffrés.\033[0m")
        print("\033[93m[!] Relancez ce programme pour terminer la récupération.\033[0m\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n\033[91m[✗] Erreur critique: {e}\033[0m")
        print("\033[93m[!] Contactez le support: recovery@example.sth\033[0m\n")
        sys.exit(1)