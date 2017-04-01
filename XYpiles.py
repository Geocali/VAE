# -*- coding: utf-8 -*-
# attention, ici les indices commencent à 0
import math
import pile
#%matplotlib inline
import numpy as np


# ============ on crée et empile les piles

alpha = math.pi / 3
pile1 = pile.modele_pile("pile1", 68, 15)
pile2 = pile.modele_pile("pile2", 68, 16)
pile3 = pile.modele_pile("pile3", 68, 17)

# ======== On visualise un exemple
import visualisations
# piles = []
# pile.empilage(piles, pile.pile(pile2, 0, 0, piles, alpha))
# pile.empilage(piles, pile.pile(pile3, 1, 0, piles, alpha))
# pile.empilage(piles, pile.pile(pile1, 1, 1, piles, alpha))
# pile.empilage(piles, pile.pile(pile2, 2, 0, piles, alpha))
# pile.empilage(piles, pile.pile(pile3, 2, 1, piles, alpha))
# pile.empilage(piles, pile.pile(pile1, 2, 2, piles, alpha))
# visualisations.visu_piles(piles, alpha)

# ======== calcul des emplacements possibles pour le centre des piles
# une fonction qui
# prend en entrée nb de piles, loi de proba du type de chaque pile
# donne en sortie le tableau "piles"
def increment_ij(i, j):
    if (i ==j):
        i = i + 1
        j = 0
    else:
        j = j + 1
    return i, j

import pandas as pd
nb_piles = 105
pile1 = pile.modele_pile("samsung_inr", 66.85, 18.33)
pile2 = pile.modele_pile("panasonic_cgr", 65.2, 18.6)
pile3 = pile.modele_pile("HW", 65, 18)
probas = {"pile1":0.2, "pile2":0.5, "pile3":0.3}
nb_simulations = 2
tab_piles = []
for m in range(0, nb_simulations): # m : indice de la simulation
    print("simulation " + str(m + 1))
    i = 0
    j = 0
    piles = []
    for k in range(0, nb_piles): # k = indice des piles
        rd_nb = np.random.random_integers(0, 100)

        if rd_nb < probas["pile1"] * 100:
            modele = pile1
        elif (rd_nb >= probas["pile1"] * 100) and (rd_nb <= (probas["pile1"] + probas["pile2"]) * 100):
            modele = pile2
        else:
            modele = pile3

        pile.empilage(piles, pile.pile(modele, i, j, piles, alpha))
        tab_piles.append([m, k, i, j, piles[i][j].fabricant, piles[i][j].rayon, piles[i][j].x, piles[i][j].y])
        i, j = increment_ij(i, j)

centres = pd.DataFrame(data = tab_piles, columns = ['n_simu', 'n_pile', 'i', 'j', 'fabricant', 'rayon', 'x', 'y'])
#visualisations.visu_centres(centres)

# ====== Calcul du circuit électrique
# pour une seule simulation

def increment_ij_circuit(i, j):

    if i%2 == 0:
        pair = True
    else:
        pair = False


    if (pair == False): # i impair : j augmente
        if (i == j):
            i = i + 1
            j = i
        else:
            j = j + 1
    else: # i pair : j diminue
        if (j == 0):
            i = i + 1
            j = 0
        else:
            j = j -1
    return i, j

nb_piles_par_cellule = 6
tab_circuits = []
n = 0
i = 0
j = 0
circuit = 0
for k in range(0, nb_piles):
    if n < nb_piles_par_cellule:
        tab_circuits.append([circuit, n, k, i, j, piles[i][j].fabricant, piles[i][j].rayon, piles[i][j].x, piles[i][j].y])
    else:
        circuit = circuit + 1
        n = 0
        tab_circuits.append([circuit, n, k, i, j, piles[i][j].fabricant, piles[i][j].rayon, piles[i][j].x, piles[i][j].y])
    n = n + 1
    i,j = increment_ij_circuit(i, j)

import matplotlib.pyplot as plt
circuits = pd.DataFrame(data=tab_circuits, columns=['circuit', 'n', 'k', 'i', 'j', 'fabricant', 'rayon', 'x', 'y'])

# tableau (x, y) avec le circuit "0":
fig, axes = plt.subplots(nrows=1, ncols=1)
xlim_ = (circuits['x'].min(axis=0) - 10, circuits['x'].max(axis=0) + 10)
ylim_ = (circuits['y'].min(axis=0) - 10, circuits['y'].max(axis=0) + 10)
for n_circuit in range(0, circuits['circuit'].max(axis=0)):
    tab = circuits.loc[circuits['circuit'] == n_circuit][['x', 'y']]
    tab.plot(x='x', y='y', ax=axes, xlim=xlim_, ylim=ylim_)

centres.plot.scatter(x='x', y='y', ax=axes)#, s=np.ones(nb_centres))
plt.show()
#circuits.plot()
#plt.plot(circuits['i'], circuits['j'])
# for kk in range(0, n):
#     plt.plot(circuits['n', 'x', 'y'].loc[]
# plt.show()
