import numpy as np
from pprint import pprint
import complexite as c
import graphPlot as g

#-----------------------------------exécution des fonctions-----------------------------------#
######### 2.0 - Exemple de dessin d'un graphe et d'un chemin à partir de sa matrice #########
# M=np.array([    #exemple de matrice fortement connexe
#      [0, 1, 0],
#      [0, 0, 1],
#      [1, 0, 0]
# ])
# r=saisir_sommets() #permet à l'utilisateur de saisir un chemin à afficher
# dessinerGraphe(M, r, 0) #dessiner un graphe

######### 3.0 - Génération aléatoire de matrice de graphes pondérés #########
M = c.graphe(5,-4,6) 
print(M)
M = c.graphe2(5, 0.8, -4, 6)
print(M)

######### 4.0 - Codage des algorithmes de plus court chemin #########
M = np.array([
    [float('inf'), 4, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [4, float('inf'), 8, float('inf'), float('inf'), float('inf'), float('inf'), 11, float('inf')],
    [float('inf'), 8, float('inf'), 7, float('inf'), 4, float('inf'), float('inf'), 2],
    [float('inf'), float('inf'), 7, float('inf'), 9, 14, float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), 9, float('inf'), 10, float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), 4, 14, 10, float('inf'), 2, float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf'), 1, 6],
    [8, 11, float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf'), 7],
    [float('inf'), float('inf'), 2, float('inf'), float('inf'), float('inf'), 6, 7, float('inf')]
])
M=M.astype('float64')

######### Solution avec l'algorithme de Dijkstra (matrice avec pondérations positives) #########
print('Matrice pondérations positives : ')
print('Matrice originale')
pprint(M)
resultat=c.Dijkstra(M, 8)
print('Solution trouvé en utilisant Dijkstra')
pprint(resultat)
g.dessinerGraphe(M, resultat, 0)

######### Solution avec l'algorithme de Bellman-Ford (matrice avec pondérations positives) #########
print('Matrice pondérations positives : ')
print('Matrice originale')
pprint(M)
resultat, nbTours =c.BellmanFord(M, 8, 1)
print('Solution trouvé en utilisant Bellman-Ford')
pprint(resultat)
g.dessinerGraphe(M, resultat,0)

######### Solution avec l'algorithme de Bellman-Ford (matrice avec pondérations négatives) #########
print('Matrice pondérations négatives : ')
M = np.array([
     [float('inf'), 5, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
     [float('inf'), float('inf'), 20, float('inf'), float('inf'), 30, 60, float('inf'), float('inf'), float('inf')],
     [float('inf'), float('inf'), float('inf'), 10, 75, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
     [float('inf'), float('inf'), -15, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 100],
     [float('inf'), float('inf'), float('inf'), float('inf'), 25, float('inf'), 5, float('inf'), 50, float('inf')],
     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), -50, float('inf'), float('inf')],
     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), -10, float('inf')],
     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),float('inf') , float('inf')]
  ])
M=M.astype('float64')
print('Matrice originale')
pprint(M)
resultat, nbTours = c.BellmanFord(M, 0, 1)
print('Solution trouvé en utilisant Bellman-Ford')
pprint(resultat)
g.dessinerGraphe(M, resultat,8)

######### 5.0 - Influence du choix de la liste ordonnée des flèches pour l'algorithme Bellman-Ford #########
c.TestBellmanFordParcours();

######### 6.1 - Deux fonctions ”temps de calcul” #########
n_sommets = 500
p = 0.8
print(f"Temps de calcul de l'algorithme de Dijkstra pour {n_sommets} sommets : ", c.TempsDij(n_sommets, p)*1000,"ms")
print(f"Temps de calcul de l'algorithme de Bellman-Ford pour {n_sommets} sommets : ", c.TempsBellmanFord(n_sommets, p) * 1000, "ms")

######### 6.2.1 - Comparaison des temps de calculs avec une proportion p de flèches fixes #########
g.dessinerGrapheComplexite(0.5)

######### 6.2.2 - Comparaison des temps de calculs avec une proportion p de flèches diminuant #########
g.dessinerGrapheComplexiteDiminuant()

######### 7.0 - Test de forte connexité #########
if c.fc(M):
    print("fortement connexe")
else:
    print("pas fortement connexe")

######### 8.0 - Forte connexité pour un graphe avec p=50% de flèches #########
for i in range(3,15):
    print(i, " : ",c.testStatFc(i))
c.pourcentageConnexiteTaille()

######### 9.0 - Détermination du seuil de forte connexité #########
c.seuil(15)

######### 10.0 - Détermination du seuil de forte connexité #########
c.representationGraphiqueSeuil()
 