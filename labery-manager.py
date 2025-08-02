import random

def generer_id(prefix):
    return prefix + ''.join([str(random.randint(0, 9)) for _ in range(9)])

class Admin:
    def __init__(self, nom, email, mdp):
        self.id = generer_id("AD")
        self.nom = nom
        self.email = email
        self.mot_de_passe = mdp

class Etudiant:
    def __init__(self, nom, mdp):
        self.id = generer_id("ST")
        self.nom = nom
        self.mot_de_passe = mdp
        self.livres_empruntes = []

class Auteur:
    def __init__(self, nom):
        self.id = generer_id("AU")
        self.nom = nom
        self.livres = []

class Livre:
    def __init__(self, titre, desc, quantite):
        self.id = generer_id("BK")
        self.titre = titre
        self.description = desc
        self.auteurs = []
        self.qte_total = quantite
        self.qte_dispo = quantite

class Bibliotheque:
    def __init__(self):
        self.admins = []
        self.etudiants = []
        self.livres = []
        self.auteurs = []

    def charger_donnees_initiales(self, donnees):
        self.admins.extend(donnees["admins"])
        self.etudiants.extend(donnees["etudiants"])
        self.auteurs.extend(donnees["auteurs"])
        self.livres.extend(donnees["livres"])

    def verifier_admin(self, email, mot_de_passe):
        for admin in self.admins:
            if admin.email == email and admin.mot_de_passe == mot_de_passe:
                return admin
        return None

    def verifier_etudiant(self, nom, mot_de_passe):
        for etu in self.etudiants:
            if etu.nom == nom and etu.mot_de_passe == mot_de_passe:
                return etu
        return None

    def creer_compte_admin(self, nom, email, mdp):
        nouvel_admin = Admin(nom, email, mdp)
        self.admins.append(nouvel_admin)
        return nouvel_admin

    def creer_compte_etudiant(self, nom, mdp):
        nouvel_etu = Etudiant(nom, mdp)
        self.etudiants.append(nouvel_etu)
        return nouvel_etu

# Données initiales simulées
bibliotheque_data = {
    "admins": [
        Admin("Yassine", "yassine@mail.com", "pass123"),
        Admin("Samiha", "samiha@mail.com", "admin321")
    ],
    "etudiants": [
        Etudiant("Omar", "omar123"),
        Etudiant("Leila", "leila321")
    ],
    "auteurs": [
        Auteur("Victor Hugo"),
        Auteur("Albert Camus")
    ],
    "livres": [
        Livre("Les Misérables", "Roman classique français.", 5),
        Livre("L'Étranger", "Un roman d'Albert Camus.", 3)
    ]
}


bibliotheque_data["livres"][0].auteurs.append(bibliotheque_data["auteurs"][0])
bibliotheque_data["livres"][1].auteurs.append(bibliotheque_data["auteurs"][1])
bibliotheque_data["auteurs"][0].livres.append(bibliotheque_data["livres"][0])
bibliotheque_data["auteurs"][1].livres.append(bibliotheque_data["livres"][1])


if __name__ == "__main__":
    biblio = Bibliotheque()
    biblio.charger_donnees_initiales(bibliotheque_data)
    print("Bienvenue dans le système de gestion de la bibliothèque\n")

    while True:
        print("1. Se connecter comme Admin")
        print("2. Se connecter comme Étudiant")
        print("3. Créer un compte Admin")
        print("4. Créer un compte Étudiant")
        print("5. Quitter")
        choix = input("Choix: ")

        if choix == "1":
            email = input("Email: ")
            mdp = input("Mot de passe: ")
            admin = biblio.verifier_admin(email, mdp)
            if admin:
                print(f"Bienvenue Admin {admin.nom}!\n")
            else:
                print("Identifiants incorrects.\n")

        elif choix == "2":
            nom = input("Nom: ")
            mdp = input("Mot de passe: ")
            etu = biblio.verifier_etudiant(nom, mdp)
            if etu:
                print(f"Bienvenue Étudiant {etu.nom}!\n")
            else:
                print("Identifiants incorrects.\n")

        elif choix == "3":
            nom = input("Nom: ")
            email = input("Email: ")
            mdp = input("Mot de passe: ")
            admin = biblio.creer_compte_admin(nom, email, mdp)
            print(f"Compte Admin créé avec succès. ID: {admin.id}\n")

        elif choix == "4":
            nom = input("Nom: ")
            mdp = input("Mot de passe: ")
            etu = biblio.creer_compte_etudiant(nom, mdp)
            print(f"Compte Étudiant créé avec succès. ID: {etu.id}\n")

        elif choix == "5":
            print("Au revoir!")
            break

        else:
            print("Choix invalide.\n")