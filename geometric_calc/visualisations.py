# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math

def visu_piles(piles, alpha):
    couleurs = {'pile1':'g', 'pile2':'b', 'pile3':'r'}
    for pile2 in piles:
        for pile in pile2:
            theta = np.linspace(-np.pi, np.pi, 200)

            plt.plot(pile.x + np.sin(theta) * pile.rayon, pile.y + np.cos(theta) * pile.rayon, color=couleurs[pile.fabricant])
            #plt.plot(pile.x, pile.y, marker='o', color=couleurs[pile.fabricant])
            plt.scatter(pile.x, pile.y, s=1, color=couleurs[pile.fabricant])
            plt.text(pile.x, pile.y, "C(" + str(pile.i) + ", " +str(pile.j) + ")", color=couleurs[pile.fabricant])

    # d1
    longueur = 30.0
    x = (-longueur, 0)
    y = (longueur * math.tan((math.pi - alpha)/2), 0)
    plt.plot(x, y, 'r-', lw=2)

    # d2
    x = (0.0, longueur)
    y = (0, longueur * math.tan((math.pi - alpha)/2))
    plt.plot(x, y, 'r-', lw=2)
    plt.show()

def visu_centres(centres):
    #centres.plot()
    nb_centres = centres.shape[0]
    centres.plot.scatter(x='x', y='y', s=np.ones(nb_centres));
    plt.show()
