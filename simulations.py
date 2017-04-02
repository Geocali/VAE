import pile
import numpy as np
import pandas as pd

class simulations:
    def __init__(self, alpha, nb_piles, modeles_piles, probas):
        self.alpha = alpha
        self.nb_piles = nb_piles
        self.modeles_piles = modeles_piles
        self.probas = probas

    # une fonction qui
    # prend en entree nb de piles, loi de proba du type de chaque pile
    # donne en sortie le tableau "piles"
    def increment_ij(self, i, j):
        if (i ==j):
            i = i + 1
            j = 0
        else:
            j = j + 1
        return i, j

    def calculate_positions(self, nb_simulations):
        tab_piles = []
        self.piles = []
        for m in range(0, nb_simulations): # m : indice de la simulation
            print("simulation " + str(m + 1))
            i = 0
            j = 0
            piles = []
            for k in range(0, self.nb_piles): # k = indice des piles
                rd_nb = np.random.random_integers(0, 100)

                if rd_nb < self.probas["pile1"] * 100:
                    modele = self.modeles_piles[0]
                elif (rd_nb >= self.probas["pile1"] * 100) and (rd_nb <= (self.probas["pile1"] + self.probas["pile2"]) * 100):
                    modele = self.modeles_piles[1]
                else:
                    modele = self.modeles_piles[2]

                pile.empilage(piles, pile.pile(modele, i, j, piles, self.alpha))
                tab_piles.append([m, k, i, j, piles[i][j].fabricant, piles[i][j].rayon, piles[i][j].x, piles[i][j].y])
                i, j = self.increment_ij(i, j)

        self.positions = pd.DataFrame(data = tab_piles, columns = ['n_simu', 'n_pile', 'i', 'j', 'fabricant', 'rayon', 'x', 'y'])
        #visualisations.visu_centres(centres)
        return self.positions
