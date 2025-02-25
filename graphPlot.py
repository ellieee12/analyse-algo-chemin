import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import complexite as c

def dessinerGraphe(matrice, resultat, d):
    """
    Déssine un graphe à partir d'une matrice, dessine aussi un chemin donné à partir d'un sommet d'arrivée

    Args:
        matrice: La matrice qui représente le graphe
        resultat: Tous les plus courts chemins
        d: Le sommet d'arrivée
    """
    # Remplace les valeurs infinies par 0
    M = np.copy(matrice)
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] == float('inf'):
                M[i][j]=0;
    G = nx.DiGraph()  #Permet d'avoir un graphe orienté
    # Récupère le plus court chemin jusqu'au sommet d
    cheminPlusCourt=resultat[d][1]    
    # Pour chaque sommet de la matrice
    for i in range(len(M)):
        for j in range(len(M[i])):
            # on ajoute une arrête si la valeur est différente de 0
            if M[i][j] != 0:
                G.add_edge(i, j, weight=M[i][j])                
    # Options d'affichage
    options = {
    'node_size': 500,
    'node_color': "white",
    'edgecolors': "black",
    'arrows' : True,
    'connectionstyle': 'arc3,rad=0.1',
    }
    center_node = ' '
    edge_nodes = set(G) - {center_node}
    pos = nx.circular_layout(G.subgraph(edge_nodes))
    pos[center_node] = np.array([0, 0])

    # Dessin du graphe
    nx.draw(G, pos, **options)
    nx.draw_networkx(G, pos, **options)
    # Dessin des arrêtes
    nx.draw_networkx_edges(G, pos, edge_color="black", arrowsize=20, connectionstyle='arc3,rad=0.1')
    edges = [(cheminPlusCourt[i], cheminPlusCourt[i+1]) for i in range(len(cheminPlusCourt)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2,arrowsize=20, connectionstyle='arc3,rad=0.1')
    # Dessin des étiquettes des arrêtes
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), label_pos=0.3)
    # Affichage du graphe dessiné
    plt.show()
  
def dessinerGrapheComplexite(p):
    """
    Dessine un graphe représentant la complexité des algorithmes de Dijkstra et Bellman-Ford en fonction du nombre de sommets

    Args:
        p: La proportion de flèches dans le graphe
    """
    #Generation des données
    nDij, tempsDij = c.ComplexiteDij(p)
    nBF, tempsBF = c.ComplexiteBF(p)
    
    #Dessiner le graphe de complexité 
    plt.plot(nDij, tempsDij,label='Dijkstra', color="blue")
    plt.plot(nBF, tempsBF, label='Bellman-Ford',color="green")
    plt.title('Complexité en fonction du nombre de sommets')
    plt.xlabel('Nombre de sommets')
    plt.ylabel('Temps d\'exécution')
    plt.legend()
    plt.show()
    
    #transformation en log et ajustement linéarire
    log_nD=np.log(nDij)
    log_tempsD=np.log(tempsDij)
    coefficientsDij = np.polyfit(log_nD,log_tempsD,1) #ajuste une ligne droite aux données 
    slopeD=coefficientsDij[0] #la pente de la ligne est l'exposant
    interceptD = coefficientsDij[1] #l'ordonnée à l'origine de la ligne
    
    log_nBF=np.log(nBF) 
    log_tempsBF=np.log(tempsBF)
    coefficientsBF = np.polyfit(log_nBF,log_tempsBF,1)
    slopeBF = coefficientsBF[0]
    interceptBF = coefficientsBF[1]
    
    #fonction croissance polynomiale 
    print("Valeur de a (Dijkstra) en utilisant la fonction croissancePolynomiale : ",c.croissancePolynomiale(log_nD, log_tempsD))
    print("Valeur de a (Bellman-Ford) en utilisant la fonction croissancePolynomiale : ",c.croissancePolynomiale(log_nBF, log_tempsBF))
    
    #tracer le graphe loglog
    plt.loglog(nDij, tempsDij, color="blue",label='Dijkstra')
    plt.loglog(nBF, tempsBF, color="green",label='Bellman-Ford')
    
    #Tracer les lignes ajustées sur le graphe loglog
    plt.plot(nDij,np.exp(interceptD) * nDij**slopeD,color="red",label='Ajustement linéaire Dijkstra')
    plt.plot(nBF,np.exp(interceptBF) * nBF**slopeBF,color="orange",label='Ajustement linéaire Bellman-Ford')
    
    plt.title('Complexité en fonction du nombre de sommets (Graphe loglog)')
    plt.xlabel('Nombre de sommets')
    plt.ylabel('Temps d\'exécution')
    plt.legend()
    plt.show()
    
    print('a (Dijkstra) : ',slopeD)
    print('a (Bellman-Ford) :', slopeBF)
    
def dessinerGrapheComplexiteDiminuant():
    """
    Dessine un graphe représentant la complexité des algorithmes de Dijkstra et Bellman-Ford en fonction du nombre de sommets avec une proportion de flèches diminuant
    """
    nDij, tempsDij = c.ComplexiteDijPDiminuant()
    nBF, tempsBF = c.ComplexiteBFPDiminuant()
    
    #Dessiner le graphe de complexité 
    plt.plot(nDij, tempsDij,label='Dijkstra', color="blue")
    plt.plot(nBF, tempsBF, label='Bellman-Ford',color="green")
    plt.title('Complexité avec proportion de flèches diminuant en fonction du nombre de sommets')
    plt.xlabel('Nombre de sommets')
    plt.ylabel('Temps d\'exécution')
    plt.legend()
    plt.show()
    
    #transformation en log et ajustement linéarire
    log_nD=np.log(nDij)
    log_tempsD=np.log(tempsDij)
    coefficientsDij = np.polyfit(log_nD,log_tempsD,1) #ajuste une ligne droite aux données 
    slopeD=coefficientsDij[0] #la pente de la ligne est l'exposant
    interceptD = coefficientsDij[1] #l'ordonnée à l'origine de la ligne
    
    log_nBF=np.log(nBF) 
    log_tempsBF=np.log(tempsBF)
    coefficientsBF = np.polyfit(log_nBF,log_tempsBF,1)
    slopeBF = coefficientsBF[0]
    interceptBF = coefficientsBF[1]
    
    #fonction croissance polynomiale 
    print("Valeur de a (Dijkstra) en utilisant la fonction croissancePolynomiale : ",c.croissancePolynomiale(log_nD, log_tempsD))
    print("Valeur de a (Bellman-Ford) en utilisant la fonction croissancePolynomiale : ",c.croissancePolynomiale(log_nBF, log_tempsBF))
    
    #tracer le graphe loglog
    plt.loglog(nDij, tempsDij, color="blue",label='Dijkstra')
    plt.loglog(nBF, tempsBF, color="green",label='Bellman-Ford')
    
    #Tracer les lignes ajustées sur le graphe loglog
    plt.plot(nDij,np.exp(interceptD) * nDij**slopeD,color="red",label='Ajustement linéaire Dijkstra')
    plt.plot(nBF,np.exp(interceptBF) * nBF**slopeBF,color="orange",label='Ajustement linéaire Bellman-Ford')
    
    plt.title('Complexité avec proportion de flèches diminuant en fonction du nombre de sommets (Graphe loglog)')
    plt.xlabel('Nombre de sommets')
    plt.ylabel('Temps d\'exécution')
    plt.legend()
    plt.show()
    
    print('a (Dijkstra) : ',slopeD)
    print('a (Bellman-Ford) :', slopeBF)
    
def representationGraphiqueSeuil():
    """
    Trace un graphique représentant le seuil en fonction de la taille de la matrice
    """
    iListe= []
    seuilListe = []
    
    # Boucle pour tester différentes tailles de matrices (i allant de 10 à 40)
    for i in range(10, 41):
        # Ajoute la taille de la matrice à la liste des tailles
        iListe.append(i)
        # Calcule et ajoute le seuil correspondant à la taille de la matrice à la liste des seuils
        seuilListe.append(c.seuil(i))
        
    # Transformation log pour l'analyse de la croissance
    iListeLog=np.log(iListe)
    seuilListeLog= np.log(seuilListe)
    
    # Estimation de la croissance polynomiale
    a=c.croissancePolynomiale(iListeLog,seuilListeLog)
    # Calcul de la valeur de c
    c=c.valeurC(iListeLog, seuilListeLog, a)
    
    print("Valeur de a : " ,a)
    print("Valeur de c : ",c)

    # Tracé du premier graphique avec une échelle linéaire
    plt.scatter(iListe,seuilListe, color="blue",label="Variation de seuil")
    plt.plot(iListe,np.exp(c)*iListe**a,color="red")
    plt.xlabel("Taille de matrice")
    plt.ylabel("Seuil")
    plt.title("Variation de seuil en fonction de la taille de matrice")
    plt.legend()
    plt.show() 
    
    # Tracé du deuxième graphique avec une échelle log-log
    plt.scatter(iListeLog,seuilListeLog, color="blue", label="Variation de seuil")
    plt.plot(iListeLog,c+iListeLog*a,color="red",label='Ajustement linéaire')
    plt.xlabel("Taille de matrice")
    plt.ylabel("Seuil")
    plt.title("Variation de seuil en fonction de la taille de matrice (Graphe log-log)")
    plt.legend()
    plt.show() 