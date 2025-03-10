import json

from fltk import *
import ast
import  time

#SIDI MOUAYAD ET Bergeot Loic , TP_7

def choix(largeur):
    """cette fonction permet de choisir un des donjons present dans le menu et ça renvoi None si on quitte le menu"""
    # creer les parametres selon le plateau choisis
    taille_f = largeur * 105
    mid_f = taille_f / 2
    case_f = taille_f / 5
    espace_f = case_f / 5

    texte((taille_f - mid_f) - 90, espace_f, "Wallisyou", taille=51)
    texte((taille_f - mid_f) - 100, case_f, "Veuillez choisir un Donjon :", taille=21)
    # affichage des options

    image(1.5 * case_f, mid_f, 'medias/donjon1.png')
    image(3 * case_f + 100, mid_f, 'medias/donjon2.png')
    image(3 * case_f + 100, 250 + mid_f, 'medias/donjon3.png')
    image(1.5 * case_f, 250 + mid_f, 'medias/donjon4.png')

    texte(2 * espace_f + 75, mid_f - 110, "Donjon N°1")

    texte(2 * espace_f + 75, mid_f + 140, "Donjon N°3")

    texte(3 * case_f + 40, mid_f - 110, "Donjon N°2")

    texte(3 * case_f + 40, mid_f + 140, "Donjon N°4")

    # attend le choix
    fin = True
    while fin:

        ev = attend_ev()
        ty = type_ev(ev)
        if ty == "ClicGauche":
            i = abscisse(ev)
            j = ordonnee(ev)

            if i >= (1.5 * case_f) - 75 and j <= mid_f + 75 and i <= mid_f + 75 and j >= (1.5 * case_f) - 75:
                return "maps/map1.txt"
            elif i >= 3 * case_f + 100 - 75 and j <= mid_f + 75:  # and i <=mid_f+75 and j>=3 * case_f+100 -75:
                return "maps/map2.txt"
            elif i <= 3 * case_f + 100 - 75 and j <= mid_f + 250 + 75:  # and i <=mid_f+250+75 and j >=3 * case_f+100 -75  :
                return "maps/map4.txt"
            elif i >= 1.5 * case_f - 75 and j <= 250 + mid_f + 75:  # and i<=mid_f+250+75 and j >=1.5 * case_f-75:
                return "maps/map3.txt"
        elif ty=="Quitte":
             ferme_fenetre()
             return None







def fenetre_fin(largeur):

    """Cette fonction affiche une fenetre fin lorsque le jeu est terminé ça demande si on veut rejouer ou quitter definitvement"""
    taille_f = largeur * 105
    mid_f = taille_f / 2
    case_f = taille_f / 5
    espace_f = case_f / 2

    texte((taille_f - mid_f) - 68, espace_f, "Wallisyou", taille=51)
    texte((taille_f - mid_f) - 80, case_f + 50, "Que souhaitez vous faire ?", taille=21)

    rectangle(espace_f, 2.25 * mid_f - (case_f // 2), 1.75 * case_f, 1.4 * mid_f + (case_f // 2), remplissage="blue")
    texte(espace_f + 55, 1.75 * mid_f - 40, "↺", couleur="white", taille=90)

    rectangle(4.45 * espace_f, 2.25 * mid_f - (case_f // 2), 3.5 * case_f, 1.4 * mid_f + (case_f // 2),
              remplissage="darkred")
    texte(4 * espace_f + 85, 1.75 * mid_f - 25, "X", couleur="white", taille=75)

    rectangle(8 * espace_f, 2.25 * mid_f - (case_f // 2), 5.20 * case_f, 1.4 * mid_f + (case_f // 2),
              remplissage="grey")
    texte(8 * espace_f + 50, 1.75 * mid_f - 15, "➜", couleur="white", taille=60)

    # attend le choiX
    fin=True
    while fin:
            ev = attend_ev()
            ty = type_ev(ev)
            if ty == "ClicGauche":
                i = abscisse(ev)
                j = ordonnee(ev)

                if distance(i,j)<= distance(espace_f,2.25 * mid_f - (case_f // 2)) and distance(i,j)>=distance( 1.75 * case_f, 1.4 * mid_f + (case_f // 2)):
                     return True

                elif distance(i,j)<=distance(4.45 * espace_f, 2.25 * mid_f - (case_f // 2)) and distance(i,j)>=distance(3.5 * case_f, 1.4 * mid_f + (case_f // 2)):
                        return False
                elif distance(i,j)<=distance(8 * espace_f, 2.25 * mid_f - (case_f // 2)) and distance(i,j)<=distance( 5.20 * case_f, 1.4 * mid_f + (case_f // 2)):
                    return False




def distance(x,y):
    """cette fonction permet de calculer la distance d'un point dans un repere"""
    return (x**2 + y**2)**0.5

def charger(fichier):
    """Cette fonction renvoie le donjon,l'aventurier et la liste dragons dans cet ordre
    """

    with open(fichier, 'r', encoding='utf-8') as file:

        lines = file.readlines()

        dragons = []
        donjon = []
        aventurier = {}

        for i in range(len(lines)):
            line = []
            dic = {}
            for j in range(len(lines[i])):

                if lines[i][j] == "╬":
                    line.append((True, True, True, True))
                    #print(lines[i][j])
                elif lines[i][j] == "═":
                    line.append((False, True, False, True))
                    #print(lines[i][j])
                elif lines[i][j] == "╠":
                    line.append((True, True, True, False))
                    #print(lines[i][j])
                elif lines[i][j] == "╔":
                    line.append((False, True, True, False))
                    #print(lines[i][j])
                elif lines[i][j] == "║":
                    line.append((True, False, True, False))
                    #print(lines[i][j])
                elif lines[i][j] == "╗":
                    line.append((False, False, True, True))
                    #print(lines[i][j])
                elif lines[i][j] == "╣":
                    line.append((True, False, True, True))
                    #print(lines[i][j])
                elif lines[i][j] == "╝":
                    line.append((True, False, False, True))
                    #print(lines[i][j])
                elif lines[i][j] == "╩":
                    line.append((True, True, False, True))
                    #print(lines[i][j])
                elif lines[i][j] == "╦":
                    line.append((False, True, True, True))
                    #print(lines[i][j])
                elif lines[i][j] == "╚":
                    line.append((True, True, False, False))
                elif lines[i][j] == "╨":
                    line.append((True, False, False, False))
                    #print(lines[i][j])
                elif lines[i][j] == "╥":
                    line.append((False, False, True, False))
                elif lines[i][j] == "╞":
                    line.append((False, True, False, False))
                    #print(lines[i][j])
                elif lines[i][j] == "╡":
                    line.append((False, False, False, True))
                    #print(lines[i][j])
                elif lines[i][j] == 'A':

                    aventurier['position'] = (int(lines[i][j + 2]), int(lines[i][j + 4]))
                    aventurier['niveau']=1

                elif lines[i][j] == 'D':

                    dic['position'] = (int(lines[i][j + 2]), int(lines[i][j + 4]))
                    dic['niveau'] = int(lines[i][j + 6])

            if len(line) != 0:
                donjon.append(line)
            if len(dic) != 0:
                dragons.append(dic)
        file.close()
        return donjon, aventurier, dragons


def charger_fichier_enregistrer(fichier):
     """cette fonction permet de charger un jeu en cours """
     with open(fichier, 'r') as f:
        jeu_recupere = f.readlines()
        f.close()

     donj=ast.literal_eval(jeu_recupere[0].strip())
     avent=ast.literal_eval(jeu_recupere[1].strip())
     drag=ast.literal_eval(jeu_recupere[2].strip())
     return donj,avent,drag

def fichier_vide(fichier):
    """cette fonction teste si le fchier rentré est vide ou pas"""


    if fichier==None:
        return None

    with open(fichier, 'r',encoding='utf-8') as f:
        premiere_ligne = f.readline()
        if premiere_ligne:
            return False

        else:
            return True


def pivoter(position, donjon):  # Fonctionne

    """Cette fonction permet de pivoter la salle de 90° dans le sens horaire"""

    i, j = position
    salle = donjon[i][j]
    new_salle = (salle[3], salle[0], salle[1], salle[2])
    donjon[i][j] = new_salle


def connect(donjon, position1, position2):

    """Cette permet de tester si deux salles sont connectés .Si c'est le cas ça renvoi True
    Sinon ça renvoi False"""


    x, y = position1
    i, j = position2

    #Ici on test si les deux salles sont sur la meme ligne

    if x==i and y==j+1 :
        if donjon[x][y][3]==True and  donjon[i][j][1]==True :
            return True
        else:
            return False
    elif x==i and j==y+1:
        if  donjon[i][j][3]== True and donjon[x][y][1]==True:
            return True
        else:
            return False

    #Ici on teste si les deux salles sont sur la meme colonne
    elif y==j and x==i+1 :
        if donjon[x][y][0] == True and donjon[i][j][2]==True :
            return True
        else:
            return False
    elif y==j and i==x+1:
        if donjon[i][j][0]== True and donjon[x][y][2]==True:
            return  True
        else:
            return False

    #Sinon on renoie False
    else:
        return False

def cases_voisines(position,donjon):

    """Cette fonction permet de generer les cases voisines àpartir d'une certaine position
    .ATTENTION: la condition y<len(donjon[X])-1: est à prendre en compte, comme 'y' c'est la colonne , dans ce cas il
    mesurer la longuer de la ligne-1:
    Exemple:  un donjon de 3 ligne ET 2 colonne , si on est a la position (0,1) :
    ça va renvoyer[(0,0),(1,1)], si on met pas le (len(donjon[X]) ça va rajouter (0,2) dans la liste"""

    x, y = position
    cases = []

    # Ajouter les voisins à gauche et à droite
    if y > 0:
        cases.append((x, y - 1))
    if y < len(donjon[x]) - 1:
        cases.append((x, y + 1))

    # Ajouter les voisins en haut et en bas
    if x > 0:
        cases.append((x - 1, y))
    if x < len(donjon) - 1:
        cases.append((x + 1, y))

    return cases


def intention(position,dragons,donjon,visite=None):

    """ Cette fonction permet renvoie un chemin vers un dragon qui lui est disponoble
    et ça renvoie  None s'il n'y a pas de chemin. ATTENTION , ici ça renvoie un tuple, (chemin,niveau)"""

    if visite is None:
        visite = set()
    visite.add(position)



    for dragon in dragons:
        if position == dragon['position']:
            return [position],dragon['niveau']
    #On parcous la liste de cases_voisines(position,donjon)
    for position_voisine in cases_voisines(position,donjon):

        #Ici on teste si la position_voisine  n'est pas dans visite et qu'elle est connecté à position(salle courant)
        if position_voisine not in visite and connect(donjon,position,position_voisine):

            res = intention(position_voisine, dragons, donjon,visite)
            #Ici on a notre chemin si res n'est pas None
            if res is not None:
                return [position] + res[0],res[1]

    #Sinon on renvoie None
    return None



def trouver_chemins_possibles(position, donjon, dragons, visite=None):
    """cette fonction permet de chercher les chemins qui sont possibles vers les dragons: Celle ci est faite sans  recursivité"""
    if visite is None:
        visite = set()
    visite.add(position)

    chemins_possibles = []
    for voisin in cases_voisines(position, donjon):
        if voisin not in visite and connect(donjon,position,voisin):
            est_dragon = False
            for dragon in dragons:
                if voisin == dragon['position']:
                    est_dragon = True
                    break
            if est_dragon:
                chemins_possibles.append([voisin])
            else:
                sous_chemins = trouver_chemins_possibles(voisin, donjon, dragons, visite)
                for sous_chemin in sous_chemins:
                    chemins_possibles.append([voisin] + sous_chemin)

    return chemins_possibles

def intention_2(position,dragons,donjon,visite=None):

    """Meilleur version de l'intention : Cette fonction permet de renvoyer le chemin vers le dragon du plus haut niveau"""
    if visite is None:
        visite = set()
    visite.add(position)

    chemins_possibles = []
    #on parcours la liste des position des cases voisines
    for voisin in cases_voisines(position, donjon):

        if voisin not in visite and connect(donjon,position,voisin):
            est_dragon = False
            for dragon in dragons:
                if voisin == dragon['position']:
                    est_dragon = True
                    break
            if est_dragon:
                chemins_possibles.append([voisin])
            else:

                sous_chemins = trouver_chemins_possibles(voisin, donjon, dragons, visite)
                for sous_chemin in sous_chemins:
                    chemins_possibles.append([voisin] + sous_chemin)


    niveaux_dragons_voisins = []

    #Ici on parcours les chemins qui sont possibles et ensuite on recupere les niveaux des dragons
    for chemin in chemins_possibles:

        for etape in chemin:
            for dragon in dragons:
                if etape == dragon['position']:
                    niveaux_dragons_voisins.append(dragon["niveau"])

    """Apres avoir recuperer les niveaux  , on parcous les chemin et
     on regarde le dragon qui le niveau supérieur ou egale a ce niveau """
    if niveaux_dragons_voisins:
            maximum_niveau = max(niveaux_dragons_voisins)

            for chemin in chemins_possibles:
                for etape in chemin:
                    for dragon in dragons:
                        if etape == dragon['position'] and dragon['niveau'] >= maximum_niveau:

                            return ([aventurier["position"]]+chemin,maximum_niveau)
    return None



def renconcontre(aventurier,dragons):
    """Cette fonction permet de savoir si l'aventurier est tué par le dragon dans ce cas , ça rencoie False
     ou sinon ça renvoie vrai et son niveau augmente de 1, au pire ça renvoie s'il n'y a pas de chemin (le dragon est tué)"""


    for dragon in dragons:
        # print(position,"position",dragon['position'])

        if aventurier['position'] == dragon['position']:

            if aventurier['niveau'] < dragon['niveau']:
                    #aventurier.clear()
                    tombe['position']=dragon['position']
                    break

            else:
                aventurier['niveau'] += 1
                dragons.remove(dragon)





def appliquer_chemin(aventurier,dragons,chemin):
    """Cette fonction permet de chevaucher un chemin en plaçant l'avanturier dans chaque position
    .ça affiche le message indiqué 'il n y a pas de  chemin' s'il n y a pas de chemin bien sure"""

    i = 1
    for position in chemin[1:]:

                    aventurier['position'] = position
                    renconcontre(aventurier,dragons)

                    if partie_gagne(aventurier,dragons)==0:

                         creation_plateau_graphisme(donjon, "medias/pebble0.png", aventurier, "medias/Knight_s.png", "medias/Dragon_s.png")

                         i1, i2 = aventurier['position']
                         for x1, y1 in chemin[i:]:
                             ligne(i2 * taille_image + taille_image // 2, i1 * taille_image + taille_image // 2,
                                   y1 * taille_image + taille_image // 2,
                                   x1 * taille_image + taille_image // 2, couleur="red")
                             i1,i2 = x1, y1
                         i = i + 1


                    else:
                        if partie_gagne(aventurier,dragons)==-1:
                            tombe['position'] = aventurier['position']
                            creation_plateau_graphisme(donjon, "medias/pebble0.png", tombe, "medias/tombe.jpg",
                                                       "medias/Dragon_s.png")
                            break
                        elif partie_gagne(aventurier, dragons) == 1:
                            creation_plateau_graphisme(donjon, "medias/pebble0.png", aventurier, "medias/Knight_s.png",
                                                       "medias/Knight_s.png")
                            break

                    mise_a_jour()



def partie_gagne(aventurier,dragons):

    """Cette fonctio renvoi 1 si l'aventurier gagne la partie,-1 si l'aventurier est tué sinon 0 la partie continue"""
    if dragons == []:
        return 1
    for dragon in dragons:
        if dragon['position']==aventurier['position']:
            if aventurier['niveau'] < dragon['niveau']:
                    return -1



    return 0



def creation_plateau_graphisme(donjon,images,aventur,image_aventurier,image_dragon):
    """Cette fonction permet de creer le plateau du jeu
       ça permet de dessiner l'aventurier,les dragons , les salles et les murs"""

    x,y = aventur['position']
    ordonne = (taille_image * 15) // 120
    absciss = (taille_image * 90) // 120



    for i in range(len(donjon)):
        x_case = taille_image // 2
        y_case = i * taille_image + taille_image // 2

        for j in range(len(donjon[i])):

            image(x_case,y_case,images)
            # Dessiner les murs et les portes
            c1 = j * taille_image + taille_image
            c2 = j * taille_image

            if not donjon[i][j][0]:
                # Mur en haut
                rectangle(c2, i * taille_image, c1, i * taille_image + ordonne, remplissage="black")

            if not donjon[i][j][1]:
                # Mur à droite
                rectangle(j * taille_image + taille_image - (ordonne-5), i * taille_image, j * taille_image + taille_image,
                          i * taille_image + taille_image, remplissage="black")

            if not donjon[i][j][2]:
                # Mur en bas
                rectangle(c2, i * taille_image + taille_image - ordonne, c1, i * taille_image + taille_image,
                          remplissage="black")

            if not donjon[i][j][3]:
                # Mur à gauche
                rectangle(j * taille_image, i * taille_image, j * taille_image + ordonne, i * taille_image + taille_image,
                          remplissage="black")

            # Dessiner les portes
            if donjon[i][j][0] == True:
                # Porte en haut
                rectangle(j * taille_image, i * taille_image, j * taille_image + 2*ordonne, i * taille_image + ordonne,
                          remplissage="black")

                rectangle(j * taille_image + absciss, i * taille_image, j * taille_image + taille_image,
                          i * taille_image + ordonne,
                          remplissage="black")

            if donjon[i][j][1] == True:
                # Porte à droite
                rectangle(j * taille_image + taille_image - ordonne, i * taille_image, j * taille_image + taille_image,
                          i * taille_image + 2*ordonne, remplissage="black")

                rectangle(j * taille_image + taille_image - ordonne, i * taille_image + taille_image - 2*ordonne,
                          j * taille_image + taille_image,
                          i * taille_image + taille_image, remplissage="black")

            if donjon[i][j][2] == True:
                # Porte en bas
                rectangle(j * taille_image, i * taille_image + taille_image - ordonne, j * taille_image + 2*ordonne,
                          i * taille_image + taille_image, remplissage="black")

                rectangle(j * taille_image + absciss, i * taille_image + taille_image - ordonne,
                          j * taille_image + taille_image + taille_image,
                          i * taille_image + taille_image, remplissage="black")

            if donjon[i][j][3] == True:
                # Porte à gauche
                rectangle(j * taille_image, i * taille_image, j * taille_image + ordonne, i * taille_image + 2*ordonne,
                          remplissage="black")
                rectangle(j * taille_image, i * taille_image +taille_image- 2*ordonne, j * taille_image + ordonne,
                          i * taille_image + taille_image,
                          remplissage="black")


            x_case = x_case + taille_image
    for dragon in dragons:
        for cle in dragon:
            if cle == 'position':
                x1, y1 = dragon[cle]

            #Affichage des images des dragons
            image(y1 * taille_image + taille_image // 2,x1 * taille_image + taille_image // 2, image_dragon)

            if partie_gagne(aventurier,dragons) !=-1 :
                texte(y1 * taille_image + taille_image//2 +2*ordonne ,x1 * taille_image + taille_image//2 - 2*ordonne,dragon['niveau'],
                      couleur="white",taille=10,tag='niveau')

    if partie_gagne(aventurier,dragons)!=-1:

        #Ca me permet d'afficher le niveau au dessus de l'aventurier
        texte(y * taille_image + taille_image//2 +2*ordonne ,x * taille_image + taille_image//2 - 3*ordonne,
              aventurier['niveau'],couleur="white",taille=10,tag='niveau')
    image(y * taille_image + taille_image // 2, x * taille_image + taille_image // 2, image_aventurier)




def pixel_vers_case(x,y,taille_case):
    return int(y//taille_case) ,int(x//taille_case)











#creation du fenetre
cree_fenetre(7*100,7*100)

#recupération du fichier

"""Si on veut recuperer le fichier enregistrer ,il suffit d'affecter "fichier" par "maps/charger_jeu.txt" """


#fichier="maps/charger_jeu.txt"
fichier=choix(6)


if fichier==None:
    print("vous aves quitté le jeu")

elif not fichier_vide(fichier):


    if fichier=="maps/charger_jeu.txt":
        donjon=charger_fichier_enregistrer(fichier)[0]
        aventurier=charger_fichier_enregistrer(fichier)[1]
        dragons=charger_fichier_enregistrer(fichier)[2]

    else:
        donjon = charger(fichier)[0]
        aventurier = charger(fichier)[1]
        dragons = charger(fichier)[2]






    hauteur=len(donjon)
    largeur=len(donjon[0])

    taille_image=100

    # Cette dictionnaire tombe me permet d'affecter la postion où l'aventurier (pour afficher une tombe)
    tombe={}

    ferme_fenetre()
    time.sleep(1)
    #Creation de fenetre
    cree_fenetre(largeur*taille_image,hauteur*taille_image)

    #Creation du plateau
    creation_plateau_graphisme(donjon,"medias/pebble0.png", aventurier, "medias/Knight_s.png", "medias/Dragon_s.png")


    #C'est une liste de position des dragons (#Utile pour les test)
    liste_position_dragon=[]
    for dragon in dragons:
        liste_position_dragon.append(dragon['position'])


    jouer=True
    while jouer:
        ev = donne_ev()
        tev = type_ev(ev)

        if partie_gagne(aventurier, dragons) == -1 or partie_gagne(aventurier,dragons)==1:


            #creation_plateau_graphisme(donjon, "medias/pebble0.png", tombe, "medias/tombe.jpg", "medias/Dragon_s.png")
            time.sleep(2)
            ferme_fenetre()

            cree_fenetre(largeur*120,hauteur*120)
            m=fenetre_fin(largeur)

            if m==True:

                ferme_fenetre()

                cree_fenetre(largeur * taille_image, hauteur * taille_image)
                if fichier!="maps/charger_jeu.txt":
                    donjon = charger(fichier)[0]
                    aventurier = charger(fichier)[1]
                    dragons = charger(fichier)[2]
                    tombe = {}
                    creation_plateau_graphisme(donjon,"medias/pebble0.png",aventurier,"medias/Knight_s.png","medias/Dragon_s.png")

                    jouer=True
                else:
                    donjon = charger_fichier_enregistrer(fichier)[0]
                    aventurier = charger_fichier_enregistrer(fichier)[1]
                    dragons = charger_fichier_enregistrer(fichier)[2]
                    tombe={}
                    creation_plateau_graphisme(donjon, "medias/pebble0.png", aventurier, "medias/Knight_s.png",
                                               "medias/Dragon_s.png")

            elif m==False:
                ferme_fenetre()
                jouer=False
                break

        #chemin=intention(aventurier['position'],dragons,donjon)
        chemin = intention_2(aventurier['position'], dragons, donjon)


        if chemin is not None:


            chemin = chemin[0]

            i1,i2=aventurier['position']
            for x,y in chemin[1:]:
                ligne(i2*taille_image+taille_image//2,i1*taille_image+taille_image//2,y*taille_image+taille_image//2,
                      x*taille_image+taille_image//2,couleur="red")
                i1,i2=x,y
                mise_a_jour()



            # Action dépendant du type d'événement reçu :

            if tev=="Touche":
                    nom_touche=touche(ev)
                    if nom_touche=='space':
                                appliquer_chemin(aventurier,dragons,chemin)

            elif tev=="Quitte":

                    jouer=False
                    break


            elif tev == "ClicGauche" :

                        x,y=pixel_vers_case(abscisse(ev),ordonnee(ev),taille_image)
                        #si vous voulez que la case que vous voulez pivoter ne soit pas celle du dragon ou du chevalier decoder la ligne suivante
                        #if (x,y)!=aventurier['position'] and (x,y) not in liste_position_dragon:
                        pivoter((x,y),donjon)
                        creation_plateau_graphisme(donjon, "medias/pebble0.png", aventurier, "medias/Knight_s.png",
                                                               "medias/Dragon_s.png")

                        mise_a_jour()


            elif tev == 'ClicDroit':  # on sauvegarde le jeu

                with open('maps/charger_jeu.txt', 'w') as f:
                    """Cette partie permet d'enregistré le jeu en cours"""
                    f.write(str(donjon) + '\n')
                    f.write(str(aventurier) + '\n')
                    f.write(str(dragons))

                    f.close()
            mise_a_jour()

        while chemin==None:

            ev = donne_ev()
            tev = type_ev(ev)

            if  tev == "ClicGauche" :

                        x,y=pixel_vers_case(abscisse(ev),ordonnee(ev),taille_image)
                        #if (x,y)!=aventurier['position'] and (x,y) not in liste_position_dragon:
                        pivoter((x,y),donjon)
                        creation_plateau_graphisme(donjon, "medias/pebble0.png", aventurier, "medias/Knight_s.png",
                                                       "medias/Dragon_s.png")


                        #chemin=intention(aventurier['position'],dragons,donjon)
                        chemin = intention_2(aventurier['position'], dragons, donjon)

            elif tev == "Quitte":
                    jouer = False
                    break
            elif tev == 'ClicDroit':  # on sauvegarde le jeu
                with open('maps/charger_jeu.txt', 'w') as f:

                    f.write(str(donjon) + '\n')
                    f.write(str(aventurier) + '\n')
                    f.write(str(dragons))

                    f.close()
            mise_a_jour()


    print("vous avez quitté le jeu!! MERCI")


else:

    print("Le fichier est vide")





