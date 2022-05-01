import statistics

# ========= LES VARIABLES =========
def variables():
    username = "oxy"
    age = 16
    wallet = 500
    print("Lui c'est", username, "il a", age,"ans il possède", wallet, "€")

variables()

# ========= LES CONDITIONS =========
def conditions():
    wallet = 2400
    rtx = 2000
    dispo = 2

    if(wallet > rtx and dispo > 1):# != est différent
        print("Oxy peut s'acehter sa rtx mais il lui restera" , wallet - rtx,"€")

    else:
        print("oxy ne peut pas s'acheter sa rtx car il lui manque ", rtx - wallet,"€ ou la rtx n'est pas disponible")

    password = input("Entrez votre mot de passe :")
    password_length = len(password) #len renvoie le nb de caractères
    print(password_length)

    if(password_length <= 8):
        print("Le mot de passe fournie ets trop court")
    else:
        print("Mot de passe valide !")

conditions()

#========= LES LISTES ==========
def listes():
    allsuser = ["Ashinura", "Oxydis", "Wraith"] #depart à 0 alors Ashi = 0...
    print(allsuser)
    print(allsuser[0])
    print(allsuser[len(allsuser) - 1 ])

    allsuser[0] = "Happy"
    allsuser[2:3] = ["Mee6"]

    allsuser.append("Sharko") #injection en fin de liste 
    allsuser.extend(["PetitJus", "Fyxou"]) #ajout d'éléments en fin de liste 

    allsuser.pop(1) #supprimer un élements par son chiffre
    allsuser.remove("Mee6") #supprimer un élement par son nom 

    allsuser.clear() #supprime tout les élements de la liste 

    print(allsuser)

    notes = [15, 17, 9, 5, 16]

    result = statistics.mean(notes) #utilisation du module importé en ligne 1

    print("La moyenne de l'élève est de {}".format(result))

listes()
#========= LES BOUCLES ==========
def boucles():
    for list_client in range(1, 6):
        print("Vous êtes le client n°", list_client)

    emails = ["oxy.oxy@oxy.oxy", "ashi.ashi@ashi.ashi", "sharko.sharko@sharko.sharko", "happy.happy@happy.happy"]
    blacklist = ["sharko.sharko@sharko.sharko", "happy.happy@happy.happy"]

    for email in emails:

        if email in blacklist:
            print("Envoie impossible à : {}".format(email))
            continue #permet de continuer vers l'autre boucle
                     #break permet de casser la boucle

        print("E-mails envoyés à :", email)

    salary = 1500

    while salary < 2000:
        salary = salary + 150
        print("Ton salaire est de {}".format(salary))

boucles()

#========= LES FONCTIONS =========
def fonctions():
    
    global year
    print("Fin de l'année", year)
    year += 1 #+= egal à : year = year + 1
    print("Début de l'année", year)

year = 2018
fonctions()
fonctions()

#exemple d'un calcul
def calc():
        result = 10 + 10
        return result

print("Le résultat de ce calcul est :", calc())

def max(a, b):
        if a > b:
            return a
        else:
            return b

first_value = int(input("Donnez la valeur de A :")) #int convertit une valeur sous forme de nombres
second_value = int(input("Donnez la valeur de b :"))

print("La valeur max est de : " , max(first_value, second_value))

#========= LES OBJETS=========
class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue aux joueurs :",pseudo, "/ Points de vie :",health, "/ Points d'attaques :",attack) #je peut remplacer pseudo par self.pseudo

    #premier types de méthodes
    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    #second type de méthodes
    def damage(self, damage):
        self.health -= damage
        print("Aie... le joueur", self.pseudo, "vient de subir", damage, "de dégats !")

    def attack_player(self, target_player):
        target_player.damage(self.attack)

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_name(self):
        return self.get_name

    def get_damage_amount(self):
        return self.damage

knife = Weapon("Karambit", 2)

player1 = Player("Oxy", 20 , 3) #cela est comme des variables mais ce sont des consctucteur
player2 = Player("Ashi", 40, 5)
player1.damage(4) #je retire 3 pts de vie au joueur 1
print("Vous possedez désormais", player1.get_health(), " points de vie")
print("Pseudo :", player1.get_pseudo())

player1.attack_player(player2)
print(player1.get_pseudo(), "Vient d'attaquer", player2.get_pseudo())
print("Bienvenue aux joueurs :",player1.get_pseudo(), "/ Points de vie :",player1.get_health(), "/ Points d'attaques :",player1.get_attack_value())
print("Bienvenue aux joueurs :",player2.get_pseudo(), "/ Points de vie :",player2.get_health(), "/ Points d'attaques :",player2.get_attack_value())

player2 = Player("Ashi", 40, 2)

#========= L'HERITAGE =========
#permet d'éviter de ce répeter

class Warrior(Player):#Player le parent de la classe Warrior

    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3
        print("Bienvenue au guerrier :",pseudo, "/ Points de vie :",health, "/ Points d'attaques :",attack)

    def damage(self, damage):
        #pass signifie qu'il n'y a pas de code pour le moment et que je ne veut pas d'erreurs
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        super().damage(damage)

    def blade(self):
        self.armor = 3
        print("Les points d'armures ont été recharger")

    def get_armor_point(self):
        return self.armor

warrior = Warrior("Happy", 30, 4)
warrior.damage(4)
print("Vie :", warrior.get_health(), "armure:", warrior.get_armor_point())

if issubclass(Warrior, Player):
    print("Le guerrier est bien une spécialisation de Player")