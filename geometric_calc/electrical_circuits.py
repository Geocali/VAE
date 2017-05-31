<<<<<<< HEAD
import pandas as pd

class electrical_circuit:
    def __init__(self, positions):
        self.positions = positions

    def increment_ij_circuit(self, i, j):
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

    # n_simu : the indice of the simulation for which we want to calculate the circuits
    def calculate(self, nb_piles_par_cellule, n_simu):
        tab_circuits = []
        n = 0 # indice pile in the current circuit
        i = 0 # indice line of the current pile
        j = 0 # indice column of the current pile
        circuit = 0
        nb_piles = self.positions.loc[self.positions.n_simu == n_simu].shape[0]
        piles = self.positions.loc[self.positions.n_simu == n_simu]

        for k in range(0, nb_piles): #k : global indice of the pile
            pile = piles.loc[(piles['i'] == i) & (piles['j'] == j)]
            if pile['inbounds'].values[0]:
                print(n, i, j, k)
                if n < nb_piles_par_cellule:
                    tab_circuits.append([circuit, n, k, i, j, pile.fabricant.values[0], pile.rayon.values[0], pile.x.values[0], pile.y.values[0]])
                else:
                    circuit = circuit + 1
                    n = 0
                    tab_circuits.append([circuit, n, k, i, j, pile.fabricant.values[0], pile.rayon.values[0], pile.x.values[0], pile.y.values[0]])
                n = n + 1
            i,j = self.increment_ij_circuit(i, j)

        self.circuits = pd.DataFrame(data=tab_circuits, columns=['circuit', 'n', 'k', 'i', 'j', 'fabricant', 'rayon', 'x', 'y'])

        return self.circuits
=======
import pandas as pd

class electrical_circuit:
    def __init__(self, positions):
        self.positions = positions

    def increment_ij_circuit(self, i, j):
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

    # n_simu : the indice of the simulation for which we want to calculate the circuits
    def calculate(self, nb_piles_par_cellule, n_simu):
        tab_circuits = []
        n = 0
        i = 0
        j = 0
        circuit = 0
        nb_piles = self.positions.loc[self.positions.n_simu == n_simu].shape[0]
        piles = self.positions.loc[self.positions.n_simu == n_simu]

        for k in range(0, nb_piles):
            pile = piles.loc[(piles['i'] == i) & (piles['j'] == j)]
            if n < nb_piles_par_cellule:
                tab_circuits.append([circuit, n, k, i, j, pile.fabricant.values[0], pile.rayon.values[0], pile.x.values[0], pile.y.values[0]])
            else:
                circuit = circuit + 1
                n = 0
                tab_circuits.append([circuit, n, k, i, j, pile.fabricant.values[0], pile.rayon.values[0], pile.x.values[0], pile.y.values[0]])
            n = n + 1
            i,j = self.increment_ij_circuit(i, j)

        self.circuits = pd.DataFrame(data=tab_circuits, columns=['circuit', 'n', 'k', 'i', 'j', 'fabricant', 'rayon', 'x', 'y'])

        return self.circuits
>>>>>>> 342872beb6a087e778d3166980c280bee753475c
