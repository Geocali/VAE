<<<<<<< HEAD
# -*- coding: utf-8 -*-
# attention, ici les indices commencent à 0

#%matplotlib inline
import math
import numpy as np
import visualisations
import pandas as pd

import pile
import simulations
import electrical_circuits

# ===== parameters =========
nb_piles = 200
l_left = 30 * 10
l_right = 20 * 10
l_top = 40 * 10
pile1 = pile.modele_pile("samsung_inr", 66.85, 18.33)
pile2 = pile.modele_pile("panasonic_cgr", 65.2, 18.6)
pile3 = pile.modele_pile("HW", 65, 18)
modeles_piles = [pile1, pile2, pile3]
probas = {"pile1":0.2, "pile2":0.5, "pile3":0.3}
nb_simulations = 1

# ====== we calculate the position of the cells for each simulation
simu = simulations.simulations(l_left, l_right, l_top, nb_piles, modeles_piles, probas)
positions = simu.calculate_positions(nb_simulations)

# ====== Calcul du circuit électrique
# pour une seule simulation
nb_piles_par_cellule = 6
circuits = electrical_circuits.electrical_circuit(positions)
n_simu = 0
circuits_results = circuits.calculate(nb_piles_par_cellule, n_simu)

import matplotlib.pyplot as plt
n1 = float(l_left**2 + l_right**2 - l_top**2)
n2 = float(2 * l_left * l_right)
alpha = math.acos(n1 / n2)
xa = 0
ya = 0
xb = l_right * math.cos((math.pi - alpha) / 2)
yb = l_right * math.sin((math.pi - alpha) / 2)
xc = - l_left * math.cos((math.pi - alpha) / 2)
yc = l_left * math.sin((math.pi - alpha) / 2)
xlim_ = (min([xa, xb, xc]), max([xa, xb, xc]))
ylim_ = (min([ya, yb, yc]), max([ya, yb, yc]))

# tableau (x, y) avec le circuit "0":
fig, axes = plt.subplots(nrows=1, ncols=1)
#xlim_ = (circuits_results['x'].min(axis=0) - 10, circuits_results['x'].max(axis=0) + 10)
#ylim_ = (circuits_results['y'].min(axis=0) - 10, circuits_results['y'].max(axis=0) + 10)
nb_circuits = circuits_results['circuit'].max(axis=0)
for n_circuit in range(nb_circuits + 1):
    tab = circuits_results.loc[circuits_results['circuit'] == n_circuit][['x', 'y']]
    tab.plot(x='x', y='y', ax=axes, label=n_circuit, xlim=xlim_, ylim=ylim_)
dict_c = {True: 'g', False: 'r'}
colors = positions.loc[positions.n_simu == n_simu]['inbounds'].map(dict_c)
positions.loc[positions.n_simu == n_simu].plot.scatter(x='x', y='y', ax=axes, c = colors)#, s=np.ones(nb_centres))

plt.plot([xa, xb, xc, xa], [ya, yb, yc, ya])

plt.show()
=======
# -*- coding: utf-8 -*-
# attention, ici les indices commencent à 0

#%matplotlib inline
import math
import numpy as np
import visualisations
import pandas as pd

import pile
import simulations
import electrical_circuits

# ===== parameters =========
nb_piles = 105
alpha = math.pi / 3
pile1 = pile.modele_pile("samsung_inr", 66.85, 18.33)
pile2 = pile.modele_pile("panasonic_cgr", 65.2, 18.6)
pile3 = pile.modele_pile("HW", 65, 18)
modeles_piles = [pile1, pile2, pile3]
probas = {"pile1":0.2, "pile2":0.5, "pile3":0.3}
nb_simulations = 5

# ====== we calculate the position of the cells for each simulation
simu = simulations.simulations(alpha, nb_piles, modeles_piles, probas)
positions = simu.calculate_positions(nb_simulations)

# ====== Calcul du circuit électrique
# pour une seule simulation
nb_piles_par_cellule = 6
circuits = electrical_circuits.electrical_circuit(positions)
n_simu = 0
circuits_results = circuits.calculate(nb_piles_par_cellule, n_simu)

import matplotlib.pyplot as plt
# tableau (x, y) avec le circuit "0":
fig, axes = plt.subplots(nrows=1, ncols=1)
xlim_ = (circuits_results['x'].min(axis=0) - 10, circuits_results['x'].max(axis=0) + 10)
ylim_ = (circuits_results['y'].min(axis=0) - 10, circuits_results['y'].max(axis=0) + 10)
for n_circuit in range(0, circuits_results['circuit'].max(axis=0)):
    tab = circuits_results.loc[circuits_results['circuit'] == n_circuit][['x', 'y']]
    tab.plot(x='x', y='y', ax=axes, xlim=xlim_, ylim=ylim_, label=n_circuit)
positions.plot.scatter(x='x', y='y', ax=axes)#, s=np.ones(nb_centres))
plt.show()
>>>>>>> 342872beb6a087e778d3166980c280bee753475c
