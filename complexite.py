import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import time

def Dijkstra(M, d):
    """
    Trouve le plus court chemin entre un sommet de départ (d) et tous les autres sommets dans un graphe pondéré

    Args:
        M: La matrice qui représente le graphe
        d: Le sommet de départ

    Returns:
        Un dictionnaire avec les distances et les chemins les plus courts entre le sommet de départ et les autres sommets
    """
    # Dictionnaire pour stocker les distances depuis le sommet de départ
    distance = {}

    # Dictionnaire pour stocker le sommet précédent dans le chemin optimal
    sommetPrecedent={}

    # Listes des sommets visités et non visités
    visited = []
    unvisited = []

    # Initialisation des distances et des sommets
    for i in range(len(M)):
        distance[i]=float('inf')
        sommetPrecedent[i]=None
        unvisited.append(i)
    distance[d] = 0

    # Tant qu'il reste des sommets non visités
    while unvisited:
        ligne=None
        smallest_distance = float('inf')

        # Trouver le sommet non visité avec la plus petite distance
        for sommet in unvisited:
            if (distance[sommet]<smallest_distance):
                smallest_distance=distance[sommet]
                ligne = sommet

        # Si aucun sommet n'est trouvé, sortir de la boucle
        if ligne is None:
            break
        
        # Mettre à jour les distances des voisins du sommet actuel
        for col in range(len(M)):
            if (M[ligne][col]) > 0 and col in unvisited:
                nouvelle_distance=distance[ligne]+M[ligne][col]
                if nouvelle_distance < distance[col]:
                    distance[col] = nouvelle_distance
                    sommetPrecedent[col] = ligne

        # Marquer le sommet actuel comme visité
        unvisited.remove(ligne)
        visited.append(ligne)
    
    resultats = {}
    for sommet in range(len(M)):
        chemin = [sommet]
        dernierSommet = sommet
        while sommetPrecedent[dernierSommet] is not None:
            chemin.insert(0, sommetPrecedent[dernierSommet])
            dernierSommet = sommetPrecedent[dernierSommet]
        if distance[sommet] == float('inf'):
            resultats[sommet] = [distance[sommet], "sommet non joignable à d par un chemin dans le graphe G"]
        else:
            resultats[sommet] = [distance[sommet], chemin]

    return resultats

def saisir_sommets():
    """
    Fonction pour saisir les sommets du graphe

    Returns:
        Un dictionnaire avec les sommets saisis
    """
    sommets = input("Saisir la liste des sommets séparés par un espace: ")
    sommets = sommets.split(" ")
    sommets = [int(element) for element in sommets]
    resultat ={}
    resultat[0]=(-1,sommets)
    
    return resultat


def parcoursSequentiel(M):
    """
    Effectue un parcours séquentiel sur une matrice d'adjacence

    Args:
        M: La matrice d'adjacence

    Returns:
        Une liste des sommets visités
    """
    resultat = []
    for i in range(len(M)):
        resultat.append(i);
    return resultat

def parcoursEnLargeur(M, s):
    """
    Effectue un parcours en largeur sur une matrice à partir d'un sommet de départ

    Args:
        M: La matrice d'adjacence
        s: Le sommet de départ

    Returns:
        Une liste des sommets visités
    """
    n=len(M)    #On colorie tous les sommets en blanc et s (depart) en ver
    couleur={}
    for i in range(n):
        couleur[i]='blanc'
    couleur[s]='vert'
    file=[s]
    Resultat=[s]
    while file!=[]:
        i=file[0]   #on prend le premier terme du file
        for j in range(n):  #on enfile les successeurs de i encore blancs
            if(M[file[0]][j]==1 and couleur[j]=='blanc'):
                file.append(j)
                couleur[j]='vert'    #On les colorie en vert(sommets visites)
                Resultat.append(j)  #On les place dans la liste Resultat
        file.pop(0) #on defile i (on reture le premier element)
    return (Resultat)

def parcoursEnProfondeur(M, s):
    """
    Effectue un parcours en profondeur sur une matrice à partir d'un sommet de départ

    Args:
        M: La matrice d'adjacence
        s: Le sommet de départ

    Returns:
        Une liste des sommets visités
    """
    n=len(M)       # taille du tableau = nombre de sommets
    couleur={}     # On colorie tous les sommets en blanc et s en vert
    for i  in range(n):
        couleur[i]='blanc'
    couleur[s]='vert'
    pile=[s]       # on initialise la pile à s
    Resultat=[s] # on initialise la liste des résultats à s
    
    while pile !=[]: # tant que la pile n'est pas vide,
        i=pile[-1]          # on prend le dernier sommet i de la pile
        Succ_blanc=[]       # on crée la liste de ses successeurs non déjà visités (blancs)
        for j in range(n):
            if (M[i,j]==1 and couleur[j]=='blanc'):
                Succ_blanc.append(j)
        if Succ_blanc!=[]:  # s'il y en a,
            v= Succ_blanc[0]    # on prend le premier (si on veut l'ordre alphabétique)
            couleur[v]='vert'   # on le colorie en vert, 
            pile.append(v)      # on l'empile
            Resultat.append(v)  # on le met en liste rsultat
        else:               # sinon:
            pile.pop()          # on sort i de la pile
    
    return Resultat

def matriceIncidence(M):
    """
    Construit une matrice d'incidence à partir d'une matrice d'adjacence

    Args:
        M: La matrice d'adjacence

    Returns:
        Une nouvelle matrice dont les valeurs sont 0 ou 1
    """
    incidence=np.copy(M)
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] == float('inf'):
                incidence[i][j] = 0
            else:
                incidence[i][j] = 1
    return incidence;

def BellmanFord(M, d, choix):
    """
    Trouve le plus court chemin entre un sommet de départ (d) et tous les autres sommets dans un graphe pondéré.
    En utilisant l'algorithme de Bellman-Ford.

    Args:
        M: La matrice qui représente le graphe
        d: Le sommet de départ
        choix: Le type de parcours à effectuer (1: séquentiel, 2: en largeur, 3: en profondeur)

    Returns:
        Un dictionnaire avec les distances et les chemins les plus courts entre le sommet de départ et les autres sommets
    """
    matriceI = matriceIncidence(M)
    listeSommets = []
    # Choix du parcours
    if choix == 1:
        listeSommets = parcoursSequentiel(matriceI)
    elif choix == 2:
        listeSommets = parcoursEnLargeur(matriceI, d);
    elif choix == 3:
        listeSommets = parcoursEnProfondeur(matriceI, d);
    else:
        print("Type invalide")
        return "Type invalide"

    #Ajouter tous les sommets non inclus dans la liste des sommets
    for i in range(len(M)):
        if i not in listeSommets:
            listeSommets.append(i)

    listeFleches=[]
    #Créer la liste des arêtes (flèches) du graphe avec leurs poids
    for i in listeSommets:
        for j in range(len(matriceI)):
            if matriceI[i][j] == 1:
                tuple=(i, j, M[i][j])
                listeFleches.append(tuple)

    poids = []
    sommetPrecedent = []
    #Initialiisation des poids et des prédécesseurs
    for sommet in listeSommets:
        if sommet == d:
            poids.append(0)
            sommetPrecedent.append(sommet)
        else:   
            poids.append(float('inf'))
            sommetPrecedent.append(None)
    
    changed=True
    iterations = 0
    while iterations<len(M) and changed:
        changed = False
        #Parcourir toutes les arêtes (flèches) du graphe
        for fleche in listeFleches:
            # Si une distance plus courte vers le sommet de destination est trouvée
            if fleche[2] + poids[fleche[0]] < poids[fleche[1]]:
                # Mettre à jour le poids (distance) vers ce sommet
                poids[fleche[1]] = fleche[2] + poids[fleche[0]]
                # Mettre à jour le prédécesseur de ce sommet
                sommetPrecedent[fleche[1]] = fleche[0]
                # Indiquer qu'un changement a été effectué
                changed = True
        # Incrémenter le nombre d'itérations
        iterations += 1
    
    # Vérification de l'existence de cycles négatifs
    for i in range(len(M)):
        for fleche in listeFleches:
            if fleche[2] + poids[fleche[0]] < poids[fleche[1]]:
                poids[fleche[1]] = -float('inf')
                poids[fleche[0]]=-float('inf')
                
    resultat = {}
    # Construction des résultats
    for j in range(len(poids)):
        if j != d:
            if poids[j] != float('inf') and poids[j] != -float('inf'):
                chemin = []
                chemin.append(j)
                pred = j
                while pred != d:
                    pred = sommetPrecedent[pred]
                    chemin.append(pred)
                resultat[j] = [poids[j], chemin[::-1]]  
            elif poids[j] == -float('inf'):
                resultat[j] = f"Sommet joignable depuis {d} par un chemin dans le graphe G, mais pas de plus court chemin (présence d'un cycle négatif)"
            else:
                resultat[j] = f"Sommet non joignable depuis {d} à {j} par un chemin dans le graphe G"
    return resultat,iterations;
        
def graphe(n, a, b):
    """
    Génère une matrice (carrée) de taille n dont les coefficients sont des entiers aléatoires entre a et b

    Args:
        n: La taille de la matrice
        a: La borne inférieure
        b: La borne supérieure

    Returns:
        Une matrice de taille n*n
    """
    # Génère une matrice binaire aléatoire de taille n*n avec des valeurs 0 ou 1
    g = np.random.binomial(1, 0.5, size=(n, n))
    # Convertit la matrice en type float64 pour permettre l'utilisation de float('inf')
    g = g.astype('float64')
    
    # Parcourir chaque élément de la matrice
    for i in range(n):
        for j in range(n):
            # Si la valeur est 0, cela signifie qu'il n'y a pas d'arête entre les sommets i et j
            if g[i][j] == 0:
                g[i][j] = float('inf') # Assigne 'inf' pour représenter l'absence d'arête
            else:
                # Sinon, génère un entier aléatoire entre a et b pour représenter le poids de l'arête
                g[i][j] = np.random.randint(a, b)
    return g

def graphe2(n,p,a,b):
    """
    Génère une matrice (carrée) de taille n dont les coefficients sont des entiers aléatoires entre a et b.
    Le graphe contiendra une proporition p de flèches.

    Args:
        n: La taukke de la matrice
        p: La proportion de flèches dans le graphe
        a: La borne inférieure
        b: La borne supérieure

    Returns:
        Une matrice de taille n*n avec une proportion p de flèches
    """
    # Génère une matrice binaire aléatoire de taille n*n avec des valeurs 0 ou 1
    # La probabilité d'obtenir un 1 est p, ce qui contrôle la proportion de flèches
    g = np.random.binomial(1, p , size=(n, n))
    # Convertit la matrice en type float64 pour permettre l'utilisation de float('inf')
    g = g.astype('float64')
    # Parcourir chaque élément de la matrice
    for i in range(n):
        for j in range(n):
            # Si la valeur est 0, cela signifie qu'il n'y a pas d'arête entre les sommets i et j
            if g[i][j] == 0:
                g[i][j] = float('inf')# Assigne 'inf' pour représenter l'absence d'arête
            else:
                # Sinon, génère un entier aléatoire entre a et b pour représenter le poids de l'arête
                g[i][j] = np.random.randint(a, b)
    return g

def TestBellmanFordParcours():
    """
    Trace un graphique en bâtons afin de comparer le nombre de tours effectués par les 3 types de parcours.
    """
    # Génère un graphe de taille 500 avec une proportion de 1% de flèches, et des poids entre 1 et 100
    M = graphe2(500, 0.01, 1, 100)
    
    # Listes pour stocker le nombre de tours pour chaque type de parcours
    listeSeq = []
    listeLargeur = []
    listeProfondeur = []
    
    # Effectue 50 tests pour chaque type de parcours
    for i in range(50):
        resultatSeq, nbToursSeq = BellmanFord(M, 0, 1)
        resultatLargeur, nbToursLargeur = BellmanFord(M, 0, 2)
        resultatProfondeur, nbToursProfondeur = BellmanFord(M, 0, 3)
        listeSeq.append(nbToursSeq)
        listeLargeur.append(nbToursLargeur)
        listeProfondeur.append(nbToursProfondeur)
        
    # Noms des types de parcours pour l'affichage
    typeParcours = ['Sequentiel', 'En Largeur', 'En Profondeur']
    
    # Calcule la moyenne du nombre de tours pour chaque type de parcours
    avgNbToursSeq = st.mean(listeSeq)
    avgNbToursLargeur = st.mean(listeLargeur)
    avgNbToursProfondeur = st.mean(listeProfondeur)

    # Liste des moyennes pour l'affichage
    nbTours = [avgNbToursSeq, avgNbToursLargeur, avgNbToursProfondeur]
    
    # Titre et étiquettes du graphique
    plt.title('Nombre de tours effectués par type de parcours')
    plt.xlabel('Type de parcours')
    plt.ylabel('Nombre de tours effectués')
    
    # Trace le graphique en bâtons
    plt.bar(typeParcours, nbTours, width=0.5, color=["red", "blue", "green"])
    
    # Affiche le graphique
    plt.show()
    
def TempsDij(n, p):
    """
    Mesure le temps d'exécution de l'algorithme de Dijkstra pour un graphe de taille n avec une proportion p de flèches

    Args:
        n: La taille du graphe
        p: La proportion de flèches

    Returns:
        Le temps d'exécution de l'algorithme
    """
    M = graphe2(n, p, 1, 100)
    debut = time.perf_counter()
    Dijkstra(M, 0)
    fin = time.perf_counter()
    return fin - debut

def TempsBellmanFord(n, p):
    """
    Mesure le temps d'exécution de l'algorithme de Bellman-Ford pour un graphe de taille n avec une proportion p de flèches

    Args:
        n: La taille du graphe
        p: La proportion de flèches

    Returns:
        Le temps d'exécution de l'algorithme
    """
    M = graphe2(n, p, 1, 100)
    debut = time.perf_counter()
    BellmanFord(M, 0, 2)
    fin = time.perf_counter()
    return fin - debut

def ComplexiteDij(p):
    """
    Calcul la complexité de l'algorithme de Dijkstra en fonction du nombre de sommets

    Args:
        p: La proportion de flèches dans le graphe

    Returns:
        Deux listes, une pour les valeurs de n (taille des matrices) et une pour les temps d'exécution
    """
    n = []
    temps = []
    
    for i in range(2, 200):
        M = graphe2(i,p, 1, 100)
        debut = time.perf_counter()
        Dijkstra(M, 0)
        fin = time.perf_counter()
        n.append(i)
        temps.append(fin - debut)
    return n, temps

def ComplexiteBF(p):
    """
    Calcul la complexité de l'algorithme de Bellman-Ford en fonction du nombre de sommets

    Args:
        p: La proportion de flèches dans le graphe

    Returns:
        Deux listes, une pour les valeurs de n (taille des matrices) et une pour les temps d'exécution
    """
    n = []
    temps = []
    
    for i in range(2, 200):
        M = graphe2(i,p, 1, 100)
        debut = time.perf_counter()
        BellmanFord(M, 0, 1)
        fin = time.perf_counter()
        n.append(i)
        temps.append(fin - debut)
    return n, temps

def croissancePolynomiale(x,y):
    """
    Calcule la croissance polynomiale d'un ensemble de données (x et y)

    Args:
        x: les valeurs de x
        y: les valeurs de y

    Returns:
        La croissance polynomiale
    """
    covariance = np.cov(x,y,bias=True)[0][1]
    variance = np.var(x)
    return covariance/variance

def valeurC(x,y,a):
    """
    Calcul la valeur c de cn^a
    """
    return np.mean(y)-(a*np.mean(x))

def ComplexiteDijPDiminuant():
    """
    Calcule la complexité de l'algorithme de Dijkstra en fonction du nombre de sommets avec une proportion de flèches diminuant

    Returns:
        Deux listes, une pour les valeurs de n (taille des matrices) et une pour les temps d'exécution
    """
    n = []
    temps = []
    
    for i in range(2, 200):
        M = graphe2(i,1/i, 1, 100)
        debut = time.perf_counter()
        Dijkstra(M, 0)
        fin = time.perf_counter()
        n.append(i)
        temps.append(fin - debut)
    return n, temps

def ComplexiteBFPDiminuant():
    """
    Calcule la complexité de l'algorithme de Bellman-Ford en fonction du nombre de sommets avec une proportion de flèches diminuant

    Returns:
        Deux listes, une pour les valeurs de n (taille des matrices) et une pour les temps d'exécution
    """
    n = []
    temps = []
    
    for i in range(2, 200):
        M = graphe2(i,1/i, 1, 100)
        debut = time.perf_counter()
        BellmanFord(M, 0, 1)
        fin = time.perf_counter()
        n.append(i)
        temps.append(fin - debut)
    return n, temps

def fc(M):
    """
    Détermine si une matrice est fortement connexe

    Args:
        M: La matrice représentant le graphe

    Returns:
        True si le graphe est fortement connexe, False sinon
    """
    k=np.shape(M)[0] # nb de lignes du tableau M. len(M) fonctionne si M est de type array
    N=M #initialisation de la somme des M^k
    P = M  #initialisation des puissances de M
    P=reduction2(P)
    for i in range(k-1): #reduction des coeff non nuls a 1
        P=reduction(np.dot(M,P))
        N = reduction(N + P)
    O=np.ones((len(N),len(N)))
    return np.array_equal(O,N)

def reduction(N): #fonction reduction qui met les coeffs non nuls
    """
    Réduit tous les coefficients infinis à 0 et les coefficients non nuls à 1

    Args:
        N: La matrice à réduire

    Returns:
        La matrice réduite
    """
    k=np.shape(N)[0]
    for i in range (k): #reduction des coeff non nuls a 1
        for j in range(k):
            if N[i, j] == float('inf'):
                N[i,j]=0
            else:
                N[i,j]=min(N[i,j],1)

    return (N)

def reduction2(N): #fonction reduction qui met les coeffs non nuls
    """
    Réduit tous les coefficients infinis à 0

    Args:
        N: La matrice à réduire

    Returns:
        La matrice réduite
    """
    k=np.shape(N)[0]
    for i in range (k): #reduction des coeff non nuls a 1
        for j in range(k):
            if N[i, j] == float('inf'):
                N[i,j]=0
            else:
                N[i,j]=N[i,j]
    return (N)

def testStatFc(n):
    """
    Détermine le pourcentage de matrices connexes parmi 200 matrices générées de taille n

    Args:
        n: La taille des matrices

    Returns:
        Le pourcentage de matrices connexes
    """
    connexe = 0
    for i in range(200):
        M = graphe(n, 1, 10)
        if fc(M):
            connexe += 1
    return connexe / (200) * 100
    
def pourcentageConnexiteTaille():
    """
    Trace un graphique représentant le pourcentage de connexité en fonction de la taille de la matrice
    """
    taille = []
    pourcentage = []
    
    for i in range(1,21):
        taille.append(i)
        pourcentage.append(testStatFc(i))
    plt.figure(figsize=(15,5))
    plt.grid()
    plt.plot(taille, pourcentage, color="blue")
    plt.xticks(taille)
    plt.xlabel("Taille de matrice")
    plt.ylabel("Pourcentage de connexité")
    plt.title("Pourcentage de connexité en fonction de la taille de la matrice")
    for (i, j) in zip(taille, pourcentage):
        plt.text(i,j,f'{round(j,2)}',fontsize=8,ha='right')
    plt.show()

def testStatFc2(n, p):
    """
    Détermine le pourcentage de matrices connexes parmi 50 matrices générées de taille n avec une proportion p de flèches

    Args:
        n: La taille des matrices
        p: La proportion de flèches

    Returns:
        Le pourcentage de matrices fortement connexes
    """
    connexe = 0
    for i in range(50):
        M = graphe2(n,p, 1, 2)
        if fc(M):
            connexe += 1
    return (connexe / 50) * 100
    
def seuil(n):
    """
    Détermine le seuil à partir duquel le pourcentage de matrices fortement connexes est inférieur à 99%

    Args:
        n: La taille des matrices

    Returns:
        Le seuil
    """
    p=0.5
    while testStatFc2(n, p)>=99:
        p -= 0.01
    print (p + 0.01)
    return (p + 0.01)