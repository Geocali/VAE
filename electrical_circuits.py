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

        import matplotlib.pyplot as plt

        circuits = pd.DataFrame(data=tab_circuits, columns=['circuit', 'n', 'k', 'i', 'j', 'fabricant', 'rayon', 'x', 'y'])

        # tableau (x, y) avec le circuit "0":
        fig, axes = plt.subplots(nrows=1, ncols=1)
        xlim_ = (circuits['x'].min(axis=0) - 10, circuits['x'].max(axis=0) + 10)
        ylim_ = (circuits['y'].min(axis=0) - 10, circuits['y'].max(axis=0) + 10)
        for n_circuit in range(0, circuits['circuit'].max(axis=0)):
            tab = circuits.loc[circuits['circuit'] == n_circuit][['x', 'y']]
            tab.plot(x='x', y='y', ax=axes, xlim=xlim_, ylim=ylim_, label=n_circuit)

        #centres.plot.scatter(x='x', y='y', ax=axes)#, s=np.ones(nb_centres))
        plt.show()
        #circuits.plot()
        #plt.plot(circuits['i'], circuits['j'])
        # for kk in range(0, n):
        #     plt.plot(circuits['n', 'x', 'y'].loc[]
        # plt.show()
