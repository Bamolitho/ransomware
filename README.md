# Ransomware Éducatif - RansonLocker V1.0

Simulation de ransomware moderne à des fins éducatives et de recherche en cybersécurité.

## Avertissement

**CE PROJET EST STRICTEMENT ÉDUCATIF.**

Ce code est destiné uniquement à :
- L'apprentissage des mécanismes des ransomwares
- La formation en cybersécurité
- La recherche académique
- Les démonstrations en environnement contrôlé

**Toute utilisation malveillante est illégale et passible de poursuites pénales.**

L'auteur décline toute responsabilité en cas d'utilisation inappropriée.

---

## Description

Ce projet simule le comportement d'un ransomware moderne en chiffrant des fichiers avec l'algorithme Fernet (AES-128) et en générant des notes de rançon réalistes. Il inclut également un décrypteur pour restaurer les fichiers.

### Fonctionnalités

**Chiffrement (encrypt.py)**
- Génération d'une clé de chiffrement unique
- Scan récursif des fichiers par extension
- Chiffrement avec Fernet (cryptographie symétrique)
- Renommage des fichiers avec extension .locked
- Génération de notes de rançon (TXT et HTML)
- Interface visuelle inspirée des vrais ransomwares
- Génération d'ID victime unique
- Simulation de deadline et montant de rançon

**Déchiffrement (decrypt.py)**
- Vérification de paiement (simulée)
- Chargement de la clé de déchiffrement
- Restauration des fichiers originaux
- Suppression des fichiers .locked
- Nettoyage automatique des notes de rançon
- Barre de progression et statistiques

---

## Architecture

```bash
ransomware_educatif/
├── encrypt.py                    # Script de chiffrement principal
├── decrypt.py                    # Script de déchiffrement
├── my_key.key                    # Clé de chiffrement (générée automatiquement)
├── README_RANSOM.txt             # Note de rançon texte (générée)
├── RANSOM_NOTE.html              # Note de rançon HTML (générée)
├── DECRYPT_INSTRUCTIONS.txt      # Instructions de déchiffrement
├── fileX.txt / test.test    	  # Des fichiers de test
└── README.md                     # Ce fichier
```

---

## Prérequis

### Logiciels requis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Dépendances Python

```bash
pip install cryptography
```

---

## Installation

1. Cloner le dépôt

```bash
git clone https://github.com/Bamolitho/ransomware.git
cd ransomware
```

2. Installer les dépendances

```bash
pip install -r requirements.txt
```

Ou manuellement :

```bash
pip install cryptography
```

---

## Utilisation

### IMPORTANT : Environnement de test

**Utilisez ce projet UNIQUEMENT dans un environnement de test isolé :**
- Machine virtuelle (VirtualBox, VMware)
- Conteneur Docker
- Dossier dédié avec fichiers de test uniquement

**NE JAMAIS exécuter sur :**
- Votre système principal
- Des fichiers importants
- Un réseau de production
- Des systèmes que vous ne possédez pas

### Étape 1 : Chiffrement

1. Placer encrypt.py dans un dossier contenant des fichiers de test
2. Exécuter le script :

```bash
python3 encrypt.py
```

3. Taper 'SIMULATE' pour confirmer
4. Taper 'YES' pour lancer le chiffrement
5. Les fichiers seront chiffrés avec l'extension .locked
6. Une note de rançon sera créée

### Étape 2 : Déchiffrement

1. Exécuter le script de déchiffrement :

```bash
python3 decrypt.py
```

2. Le script chargera automatiquement la clé (my_key.key)
3. Appuyer sur ENTRÉE pour confirmer
4. Les fichiers seront restaurés automatiquement

---

## Détails techniques

### Algorithme de chiffrement

- **Algorithme** : Fernet (AES-128 en mode CBC avec HMAC)
- **Bibliothèque** : cryptography (Python)
- **Padding** : PKCS7
- **Sécurité** : Authentification des données chiffrées

### Extensions ciblées

Le ransomware cible les extensions suivantes :

```python
.txt, .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx
.jpg, .jpeg, .png, .gif, .mp4, .avi, .mp3
.zip, .rar, .sql, .csv, .json, .xml
.html, .css, .js
```

### Fichiers exclus

Les fichiers suivants ne sont jamais chiffrés :

```python
encrypt.py
decrypt.py
encrypt_v0.py
decrypt_0.py
my_key.key
README_RANSOM.txt
DECRYPT_INSTRUCTIONS.txt
README.md
```

### Structure de la clé

La clé de chiffrement est générée via :

```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()  # Clé aléatoire de 32 bytes
```

Format : Base64, 44 caractères

---

## Fonctionnement d'un vrai ransomware

### Différences avec un ransomware réel

| Aspect | Simulation | Ransomware réel |
|--------|-----------|-----------------|
| Clé de chiffrement | Stockée localement (my_key.key) | Envoyée au serveur C&C, détruite localement |
| Paiement | Simulé, aucun vrai paiement | Bitcoin vers wallet des attaquants |
| Propagation | Aucune | Propagation réseau, exploits, phishing |
| Persistance | Aucune | Modification registre, tâches planifiées |
| Communication | Aucune | Serveur Command & Control (C2) |
| Obfuscation | Code lisible | Code fortement obfusqué |

### Vecteurs d'infection courants

- Pièces jointes email malveillantes (macros Office)
- Exploits de vulnérabilités (EternalBlue, SMB)
- Sites web compromis (drive-by download)
- Faux logiciels / cracks
- RDP (Remote Desktop Protocol) non sécurisé

---

## Mesures de protection

### Prévention

1. **Sauvegardes régulières**
   - Règle 3-2-1 : 3 copies, 2 supports, 1 hors site
   - Sauvegardes déconnectées du réseau
   - Tests réguliers de restauration

2. **Sécurité du système**
   - Mises à jour automatiques (OS, logiciels)
   - Antivirus professionnel à jour
   - Pare-feu activé
   - UAC (User Account Control) activé

3. **Comportement sécurisé**
   - Ne pas ouvrir pièces jointes suspectes
   - Vérifier expéditeur des emails
   - Ne pas cliquer sur liens inconnus
   - Utiliser des mots de passe forts + MFA

4. **Sécurité réseau**
   - Désactiver RDP si non nécessaire
   - VPN pour accès distants
   - Segmentation réseau
   - Monitoring des activités suspectes

### Réaction en cas d'infection

1. **Isoler immédiatement** le système du réseau
2. **Ne pas payer** la rançon (pas de garantie)
3. **Contacter** un spécialiste en cybersécurité
4. **Signaler** aux autorités (police, ANSSI)
5. **Restaurer** depuis sauvegardes si disponibles
6. **Analyser** pour identifier le vecteur d'infection

---

## Aspects légaux

### Législation française

**Code pénal, Article 323-1** : Accès frauduleux à un système de traitement automatisé de données

- Peine : 2 ans d'emprisonnement et 60 000 euros d'amende

**Code pénal, Article 323-2** : Entrave au fonctionnement d'un système
- Peine : 5 ans d'emprisonnement et 150 000 euros d'amende

**Code pénal, Article 323-3** : Atteinte à l'intégrité des données
- Peine : 5 ans d'emprisonnement et 150 000 euros d'amende

### Législation internationale

- **États-Unis** : Computer Fraud and Abuse Act (CFAA) - Jusqu'à 20 ans de prison
- **Union Européenne** : Directive NIS, RGPD - Amendes jusqu'à **min** (4% du CA mondial, 20M euros)
- **Royaume-Uni** : Computer Misuse Act 1990 - Jusqu'à 10 ans de prison

---

## Ressources pédagogiques

### Documentation recommandée

- [No More Ransom Project](https://www.nomoreransom.org/) - Outils de déchiffrement gratuits
- [ANSSI - Guide ransomware](https://www.ssi.gouv.fr/) - Guide officiel français
- [MITRE ATT&CK](https://attack.mitre.org/) - Base de données des techniques d'attaque
- [OWASP](https://owasp.org/) - Ressources sur la sécurité applicative

### Formations en cybersécurité

- Certifications : CEH, OSCP, GIAC
- Plateformes : TryHackMe, HackTheBox, Root-Me
- Cours en ligne : Coursera, Udemy, edX

---

## Contributions

Les contributions sont bienvenues pour améliorer l'aspect éducatif du projet :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit les changements (`git commit -m 'Ajout fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

**Critères d'acceptation :**
- Code bien documenté
- Respect du but éducatif
- Aucune amélioration malveillante
- Tests en environnement isolé

---

## Auteur

**Amolitho Baldé**
- Portfolio : [https://bamolitho.github.io/portfolio/](https://bamolitho.github.io/portfolio/)
- GitHub : [https://github.com/Bamolitho/](https://github.com/Bamolitho/)
- LinkedIn : [https://www.linkedin.com/in/amolithobalde/](https://www.linkedin.com/in/amolithobalde/)

---

## Remerciements

Ce projet a été développé dans un cadre strictement éducatif pour sensibiliser aux dangers des ransomwares et enseigner les bonnes pratiques de cybersécurité.

Merci aux organisations suivantes pour leurs ressources pédagogiques :
- ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information)
- CERT-FR (Centre gouvernemental de veille, d'alerte et de réponse aux attaques informatiques)
- No More Ransom Project
- OWASP Foundation

---

## Changelog

### Version 1.0 (2025-12-07)
- Simulation complète de ransomware moderne
- Interface visuelle réaliste
- Génération de notes de rançon (TXT + HTML)
- Décrypteur avec vérification de paiement
- Documentation complète
- Support multi-plateforme (Windows, Linux, macOS)

---

**RAPPEL FINAL : CE PROJET EST STRICTEMENT ÉDUCATIF. TOUTE UTILISATION MALVEILLANTE EST ILLÉGALE.**
