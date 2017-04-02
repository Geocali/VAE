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
nb_simulations = 2

# ====== we calculate the position of the cells for each simulation
simu = simulations.simulations(alpha, nb_piles, modeles_piles, probas)
positions = simu.calculate_positions(nb_simulations)

# ====== Calcul du circuit électrique
# pour une seule simulation
nb_piles_par_cellule = 6
circuits = electrical_circuits.electrical_circuit(positions)
n_simu = 0
circuits.calculate(nb_piles_par_cellule, n_simu)
