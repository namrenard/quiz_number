# importation de la fonction random pour aléatoire
import random

# fonction qui demande a l'user de donner le nombre magique, boucle permet de redemander
# et try de verifier la valeur numérique.
def choix_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique entre {nb_min} et {nb_max} ?")
        try:
            nombre_int = int(nombre_str)
        except:
            print("Erreur, veuillez rentrer une valeur numérique.")
            # ajout de condition else pour verifier dans la boucle si le nombre est
            # entre nb min et nb max.
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
             print(f"Erreur, le nombre magique entre {nb_min} et {nb_max} ")
             nombre_int = 0
    return nombre_int


# constante qui seront aleatoire ET VARIABLE MAX.
NOMBRE_MIN = 1
NOMBRE_MAX = 100
NB_VIES = 10
# la valeur random.randint(valeur min, valeur max) pour générer le nombre aléatoire
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
# condition, tester le nb est petit ou grand et bravo !
# ajout de nombre de vies pour limiter le jeu.
nombre = 0
vies = NB_VIES
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies.")
    nombre = choix_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
     print("Bravo, vous avez gagné !")
    elif nombre > NOMBRE_MAGIQUE:
     print("Le nombre magique est plus petit !")
     vies -= 1
    else:
     print("Le nombre magique est plus grand !")
     vies -= 1


if vies == 0:
    print(f"Vous avez perdu. Le nombre magique était {NOMBRE_MAGIQUE}")

