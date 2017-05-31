# -*- coding: utf-8 -*-

import math

class modele_pile:
    def __init__(self, fabricant, hauteur, diametre):
        self.fabricant = fabricant
        self.hauteur = hauteur
        self.diametre = diametre

class pile:
    def premiere(self, i, j, piles, alpha):
        a = math.tan((math.pi - alpha) / 2)
        c = 0 - piles[i - 1][0].x
        d = self.rayon / math.sin(alpha/2) - piles[i - 1][0].y
        b = (a * d - c - math.sqrt(-a**2 * c**2 + (a**2 + 1) * (self.rayon + piles[i - 1][0].rayon)**2 - 2 * a * c * d - d**2)) / (a**2 + 1)
        x = 0 + b * 1
        y = self.rayon / math.sin(alpha/2) + b * (- math.tan((math.pi - alpha) / 2))
        return x, y

    def milieu(self, i, j, piles, alpha):
        beta = 0
        x = piles[i - 1][j].x + (piles[i - 1][j].rayon + self.rayon)**2 * (- math.sin(beta))
        y = piles[i - 1][j].y + (piles[i - 1][j].rayon + self.rayon)**2 * (math.cos(beta))
        dist1 = math.sqrt( (x - piles[i - 1][j - 1].x)**2 + (y - piles[i - 1][j - 1].y)**2 )
        dist2 = math.sqrt( (x - piles[i][j - 1].x)**2 + (y - piles[i][j - 1].y)**2 )
        cond1 = dist1 > (self.rayon + piles[i - 1][j - 1].rayon)
        cond2 = dist2 > (self.rayon + piles[i][j - 1].rayon)
        k = 0
        while cond1 and cond2 and k < 1000:
            beta = beta + 0.005
            #print("i, j : " + str(i) + ", " + str(j))
            x = piles[i - 1][j].x + (piles[i - 1][j].rayon + self.rayon) * (- math.sin(beta))
            y = piles[i - 1][j].y + (piles[i - 1][j].rayon + self.rayon) * (math.cos(beta))
            dist1 = math.sqrt( (x - piles[i - 1][j - 1].x)**2 + (y - piles[i - 1][j - 1].y)**2 )
            dist2 = math.sqrt( (x - piles[i][j - 1].x)**2 + (y - piles[i][j - 1].y)**2 )
            #print(dist1, (self.rayon + piles[i - 1][j - 1].rayon))
            cond1 = dist1 > (self.rayon + piles[i - 1][j - 1].rayon)
            #print(dist2, (self.rayon + tab[j - 1].rayon))
            cond2 = dist2 > (self.rayon + piles[i][j - 1].rayon)
            k = k + 1
        return x, y

    def fin(self, i, j, piles, alpha):
        # 1) on calcule d'abord sa position par rapport à celle du dessous (i-1,j-1)
        # 1.1) on commence par calculer T, le point qui est sur la droite perp à d2, à la distance Rij de d2
        beta = math.asin((piles[i-1][j-1].rayon - self.rayon) / (piles[i-1][j-1].rayon + self.rayon))
        d = (piles[i-1][j-1].rayon + self.rayon) * math.cos(beta)
        norme = math.sqrt(1 + math.tan((math.pi - alpha) / 2)**2)
        vn_x = 1 / norme * (-math.tan((math.pi - alpha) / 2))
        vn_y = 1 / norme
        xt = piles[i-1][j-1].x - (piles[i-1][j-1].rayon - self.rayon) * vn_x
        yt = piles[i-1][j-1].y - (piles[i-1][j-1].rayon - self.rayon) * vn_y

        # 1.2) on déplace T de d suivant vn pour trouver Cij
        xa = xt + d / norme * 1
        ya = yt + d / norme * math.tan((math.pi - alpha) / 2)

        # 2) On verifie que la pile (i, j-1) ne se superpose pas
        # si ce n'est pas le cas,
        dist = math.sqrt((xa - piles[i][j-1].x)**2 + (ya - piles[i][j-1].y)**2)
        #print i, j
        #print(dist, piles[i][j-1].rayon + self.rayon)

        if dist > (piles[i][j-1].rayon + self.rayon):
            return xa, ya
        else:
            # 2.1)
            a = math.tan((math.pi - alpha) / 2)
            f = abs(a * piles[i][j-1].x - piles[i][j-1].y) / math.sqrt(1 + a**2)
            #print f, self.rayon, piles[i][j-1].rayon
            beta = math.acos((f - self.rayon) / (self.rayon + piles[i][j-1].rayon))
            e = f - self.rayon
            d = e * math.tan(beta)
            xt = piles[i][j-1].x - e * (-a) / math.sqrt(1 + a**2)
            yt = piles[i][j-1].y - e * 1 / math.sqrt(1 + a**2)
            xb = xt + d * 1 / math.sqrt(1 + a**2)
            yb = yt + d * a / math.sqrt(1 + a**2)

            return xb, yb

    def calcul_centre(self, i, j, piles, l_left, l_right, l_top):

        n1 = float(l_left**2 + l_right**2 - l_top**2)
        n2 = float(2 * l_left * l_right)
        alpha = math.acos(n1 / n2)
        if i == 0:
            x = 0
            y = self.rayon / math.sin(alpha / 2)

        # 1) Placer la première bille de la rangée
        if i > 0 and j == 0:
            x, y = self.premiere(i, j, piles, alpha)

        # 2) Insérer une bille dans la rangée, en dehors des extrémités
        if i > 0 and j > 0 and j < i:
            x, y = self.milieu(i, j, piles, alpha)

        # 3) placer la dernière bille de la rangée
        if i > 0 and j > 0 and j == i:
            x, y = self.fin(i, j, piles, alpha)

        # 4) we check if the pile is in the bounds
        # 4.1) to check if the center is inside the triangle :
        # p = p0 + (p1 - p0) * s + (p2 - p0) * t
        # The point p is inside the triangle if 0 <= s <= 1 and 0 <= t <= 1 and s + t <= 1
        # if the center is out, x, y = -1, -1
        xa = 0
        ya = 0
        xb = l_right * math.cos((math.pi - alpha) / 2)
        yb = l_right * math.sin((math.pi - alpha) / 2)
        xc = - l_left * math.cos((math.pi - alpha) / 2)
        yc = l_left * math.sin((math.pi - alpha) / 2)
        t = (y - ya - (x - xa) / (xb - xa) * (yb - ya)) / (yc - ya - (xc - xa) / (xb - xa) * (yb - ya))
        s = (x - xa - t * (xc - xa)) / (xb - xa)
        if (0 <= s and s <= 1 and s + t <= 1):
            # 4.2) If the center is inside, we check the distance to the 3 lines
            # if it is not > rayon of the pile, the pile is outbounds
            err = 0.001
            Dab = abs(( (x - xb) * (yb - ya) - (y - yb) * (xb - xa) ) / math.sqrt( (xa - xb)**2 + (ya - yb)**2 )) + err
            Dac = abs(( (x - xc) * (yc - ya) - (y - yc) * (xc - xa) ) / math.sqrt( (xa - xc)**2 + (ya - yc)**2 )) + err
            Dcb = abs(( (x - xb) * (yb - yc) - (y - yb) * (xb - xc) ) / math.sqrt( (xc - xb)**2 + (yc - yb)**2 )) + err

            if( Dab >= self.rayon and Dac >= self.rayon and Dcb >= self.rayon ):
                self.inbounds = True
            else:
                self.inbounds = False
            #print(i, j, self.rayon, Dab, Dac, Dcb, self.inbounds)
        else:
            self.inbounds = False
        #print(self.inbounds)
        return x, y

    def __init__(self, modele, i, j, piles, l_left, l_right, l_top):
        self.rayon = modele.diametre / 2
        self.x, self.y = self.calcul_centre(i, j, piles, l_left, l_right, l_top)
        self.i, self.j = i, j
        self.fabricant = modele.fabricant

def empilage(batterie, pile):
    i, j = pile.i, pile.j
    if i == 0 and j == 0:
        tab = [pile]
        batterie.append(tab)
    if i > 0 and j == 0: # on crée une nouvelle ligne
        tab = [pile]
        batterie.append(tab)
    if i > 0 and j > 0:
        tab = batterie[i]
        tab.append(pile)
        batterie.pop()
        batterie.append(tab)
    return batterie

import unittest
class TestMethods(unittest.TestCase):
    def setUp(self):
        self.err_max = 0.05
        self.piles = []
        self.alpha = math.pi / 3
        self.pile1 = modele_pile("panasonic", 68, 15)
        self.pile2 = modele_pile("panasonic", 68, 16)
        self.pile3 = modele_pile("panasonic", 68, 17)

        empilage(self.piles, pile(self.pile1, 0, 0, self.piles, self.alpha))
        empilage(self.piles, pile(self.pile2, 1, 0, self.piles, self.alpha))
        empilage(self.piles, pile(self.pile2, 1, 1, self.piles, self.alpha))
        empilage(self.piles, pile(self.pile2, 2, 0, self.piles, self.alpha))
        empilage(self.piles, pile(self.pile2, 2, 1, self.piles, self.alpha))
        empilage(self.piles, pile(self.pile2, 2, 2, self.piles, self.alpha))

    def test_0_0(self):
        #empilage(self.piles, pile(self.pile1, 0, 0, self.piles, self.alpha))
        xvrai = 0
        yvrai = 14
        err = math.sqrt((self.piles[0][0].x - xvrai)**2 + (self.piles[0][0].y - yvrai)**2)
        self.assertTrue(err < self.err_max)

    def test_milieu(self):
        # on vérifie que la pile est presque exactement à Rij + Rautre des piles les plus proches
        tolerance = 0.3 # mm
        for piles1 in self.piles:
            for pile in piles1:
                if pile.j > 0 and pile.j < pile.i:
                    # d avec la pile sur même ligne, à gauche
                    dig = math.sqrt((pile.x - self.piles[pile.i][pile.j - 1].x)**2 + (pile.y - self.piles[pile.i][pile.j - 1].y)**2)
                    dig_min = pile.rayon + self.piles[pile.i][pile.j - 1].rayon
                    cond1 = dig >= dig_min - tolerance
                    # idem, mais à droite
                    did = math.sqrt((pile.x - self.piles[pile.i][pile.j + 1].x)**2 + (pile.y - self.piles[pile.i][pile.j + 1].y)**2)
                    did_min = pile.rayon + self.piles[pile.i][pile.j + 1].rayon
                    cond2 = did >= did_min - tolerance
                    # d avec la pile sur la ligne du dessous, à gauche
                    di1g = math.sqrt((pile.x - self.piles[pile.i - 1][pile.j - 1].x)**2 + (pile.y - self.piles[pile.i - 1][pile.j - 1].y)**2)
                    di1g_min = pile.rayon + self.piles[pile.i - 1][pile.j - 1].rayon
                    cond3 = di1g >= di1g_min - tolerance
                    # idem, mais à droite
                    di1d = math.sqrt((pile.x - self.piles[pile.i - 1][pile.j].x)**2 + (pile.y - self.piles[pile.i - 1][pile.j].y)**2)
                    di1d_min = pile.rayon + self.piles[pile.i - 1][pile.j].rayon
                    cond4 = dig >= dig_min - tolerance

                    # !!!! ajouter une condition :
                    # une ou deux billes du dessous doivent presque toucher
                    # si une seule bille du dessous, la bille de gauche de la même ligne

        self.assertTrue(cond1 and cond2 and cond3 and cond4)

if __name__ == '__main__':
    unittest.main()
=======
# -*- coding: utf-8 -*-

import math

class modele_pile:
    def __init__(self, fabricant, hauteur, diametre):
        self.fabricant = fabricant
        self.hauteur = hauteur
        self.diametre = diametre

class pile:
    def premiere(self, i, j, piles, alpha):
        a = math.tan((math.pi - alpha) / 2)
        c = 0 - piles[i - 1][0].x
        d = self.rayon / math.sin(alpha/2) - piles[i - 1][0].y
        b = (a * d - c - math.sqrt(-a**2 * c**2 + (a**2 + 1) * (self.rayon + piles[i - 1][0].rayon)**2 - 2 * a * c * d - d**2)) / (a**2 + 1)
        x = 0 + b * 1
        y = self.rayon / math.sin(alpha/2) + b * (- math.tan((math.pi - alpha) / 2))
        return x, y

    def milieu(self, i, j, piles, alpha):
        beta = 0
        x = piles[i - 1][j].x + (piles[i - 1][j].rayon + self.rayon)**2 * (- math.sin(beta))
        y = piles[i - 1][j].y + (piles[i - 1][j].rayon + self.rayon)**2 * (math.cos(beta))
        dist1 = math.sqrt( (x - piles[i - 1][j - 1].x)**2 + (y - piles[i - 1][j - 1].y)**2 )
        dist2 = math.sqrt( (x - piles[i][j - 1].x)**2 + (y - piles[i][j - 1].y)**2 )
        cond1 = dist1 > (self.rayon + piles[i - 1][j - 1].rayon)
        cond2 = dist2 > (self.rayon + piles[i][j - 1].rayon)
        k = 0
        while cond1 and cond2 and k < 1000:
            beta = beta + 0.005
            #print("i, j : " + str(i) + ", " + str(j))
            x = piles[i - 1][j].x + (piles[i - 1][j].rayon + self.rayon) * (- math.sin(beta))
            y = piles[i - 1][j].y + (piles[i - 1][j].rayon + self.rayon) * (math.cos(beta))
            dist1 = math.sqrt( (x - piles[i - 1][j - 1].x)**2 + (y - piles[i - 1][j - 1].y)**2 )
            dist2 = math.sqrt( (x - piles[i][j - 1].x)**2 + (y - piles[i][j - 1].y)**2 )
            #print(dist1, (self.rayon + piles[i - 1][j - 1].rayon))
            cond1 = dist1 > (self.rayon + piles[i - 1][j - 1].rayon)
            #print(dist2, (self.rayon + tab[j - 1].rayon))
            cond2 = dist2 > (self.rayon + piles[i][j - 1].rayon)
            k = k + 1
        return x, y

    def fin(self, i, j, piles, alpha):
        # 1) on calcule d'abord sa position par rapport à celle du dessous (i-1,j-1)
        # 1.1) on commence par calculer T, le point qui est sur la droite perp à d2, à la distance Rij de d2
        beta = math.asin((piles[i-1][j-1].rayon - self.rayon) / (piles[i-1][j-1].rayon + self.rayon))
        d = (piles[i-1][j-1].rayon + self.rayon) * math.cos(beta)
        norme = math.sqrt(1 + math.tan((math.pi - alpha) / 2)**2)
        vn_x = 1 / norme * (-math.tan((math.pi - alpha) / 2))
        vn_y = 1 / norme
        xt = piles[i-1][j-1].x - (piles[i-1][j-1].rayon - self.rayon) * vn_x
        yt = piles[i-1][j-1].y - (piles[i-1][j-1].rayon - self.rayon) * vn_y

        # 1.2) on déplace T de d suivant vn pour trouver Cij
        xa = xt + d / norme * 1
        ya = yt + d / norme * math.tan((math.pi - alpha) / 2)

        # 2) On verifie que la pile (i, j-1) ne se superpose pas
        # si ce n'est pas le cas,
        dist = math.sqrt((xa - piles[i][j-1].x)**2 + (ya - piles[i][j-1].y)**2)
        #print i, j
        #print(dist, piles[i][j-1].rayon + self.rayon)

        if dist > (piles[i][j-1].rayon + self.rayon):
            return xa, ya
        else:
            # 2.1)
            a = math.tan((math.pi - alpha) / 2)
            f = abs(a * piles[i][j-1].x - piles[i][j-1].y) / math.sqrt(1 + a**2)
            #print f, self.rayon, piles[i][j-1].rayon
            beta = math.acos((f - self.rayon) / (self.rayon + piles[i][j-1].rayon))
            e = f - self.rayon
            d = e * math.tan(beta)
            xt = piles[i][j-1].x - e * (-a) / math.sqrt(1 + a**2)
            yt = piles[i][j-1].y - e * 1 / math.sqrt(1 + a**2)
            xb = xt + d * 1 / math.sqrt(1 + a**2)
            yb = yt + d * a / math.sqrt(1 + a**2)

            return xb, yb

    def calcul_centre(self, i, j, alpha, piles):
        if i == 0:
            x = 0
            y = self.rayon / math.sin(alpha / 2)
            return x, y

        # 1) Placer la première bille de la rangée
        if i > 0 and j == 0:
            return self.premiere(i, j, piles, alpha)

        # 2) Insérer une bille dans la rangée, en dehors des extrémités
        if i > 0 and j > 0 and j < i:
            return self.milieu(i, j, piles, alpha)

        # 3) placer la dernière bille de la rangée
        if i > 0 and j > 0 and j == i:
            return self.fin(i, j, piles, alpha)

    def __init__(self, modele, i, j, piles, alpha):
        self.rayon = modele.diametre / 2
        self.x, self.y = self.calcul_centre(i, j, alpha, piles)
        self.i, self.j = i, j
        self.fabricant = modele.fabricant

def empilage(batterie, pile):
    i, j = pile.i, pile.j
    if i == 0 and j == 0:
        tab = [pile]
        batterie.append(tab)
    if i > 0 and j == 0: # on crée une nouvelle ligne
        tab = [pile]
        batterie.append(tab)
    if i > 0 and j > 0:
        tab = batterie[i]
        tab.append(pile)
        batterie.pop()
        batterie.append(tab)
    return batterie

import unittest
class TestMethods(unittest.TestCase):
    def setUp(self):
        self.err_max = 0.05
        self.piles = []
        self.alpha = math.pi / 3
        self.pile1 = modele_pile("panasonic", 68, 15)
        self.pile2 = modele_pile("panasonic", 68, 16)
        self.pile3 = modele_pile("panasonic", 68, 17)

        empilage(self.piles, pile(self.pile1, 0, 0, self.piles, self.alpha))
        empilage(self.piles, pile(self.pile2, 1, 0, self.piles, self.alpha))
        empilage(self.piles, pile(self.pile2, 1, 1, self.piles, self.alpha))
        empilage(self.piles, pile(self.pile2, 2, 0, self.piles, self.alpha))
        empilage(self.piles, pile(self.pile2, 2, 1, self.piles, self.alpha))
        empilage(self.piles, pile(self.pile2, 2, 2, self.piles, self.alpha))

    def test_0_0(self):
        #empilage(self.piles, pile(self.pile1, 0, 0, self.piles, self.alpha))
        xvrai = 0
        yvrai = 14
        err = math.sqrt((self.piles[0][0].x - xvrai)**2 + (self.piles[0][0].y - yvrai)**2)
        self.assertTrue(err < self.err_max)

    def test_milieu(self):
        # on vérifie que la pile est presque exactement à Rij + Rautre des piles les plus proches
        tolerance = 0.3 # mm
        for piles1 in self.piles:
            for pile in piles1:
                if pile.j > 0 and pile.j < pile.i:
                    # d avec la pile sur même ligne, à gauche
                    dig = math.sqrt((pile.x - self.piles[pile.i][pile.j - 1].x)**2 + (pile.y - self.piles[pile.i][pile.j - 1].y)**2)
                    dig_min = pile.rayon + self.piles[pile.i][pile.j - 1].rayon
                    cond1 = dig >= dig_min - tolerance
                    # idem, mais à droite
                    did = math.sqrt((pile.x - self.piles[pile.i][pile.j + 1].x)**2 + (pile.y - self.piles[pile.i][pile.j + 1].y)**2)
                    did_min = pile.rayon + self.piles[pile.i][pile.j + 1].rayon
                    cond2 = did >= did_min - tolerance
                    # d avec la pile sur la ligne du dessous, à gauche
                    di1g = math.sqrt((pile.x - self.piles[pile.i - 1][pile.j - 1].x)**2 + (pile.y - self.piles[pile.i - 1][pile.j - 1].y)**2)
                    di1g_min = pile.rayon + self.piles[pile.i - 1][pile.j - 1].rayon
                    cond3 = di1g >= di1g_min - tolerance
                    # idem, mais à droite
                    di1d = math.sqrt((pile.x - self.piles[pile.i - 1][pile.j].x)**2 + (pile.y - self.piles[pile.i - 1][pile.j].y)**2)
                    di1d_min = pile.rayon + self.piles[pile.i - 1][pile.j].rayon
                    cond4 = dig >= dig_min - tolerance

                    # !!!! ajouter une condition :
                    # une ou deux billes du dessous doivent presque toucher
                    # si une seule bille du dessous, la bille de gauche de la même ligne

        self.assertTrue(cond1 and cond2 and cond3 and cond4)

if __name__ == '__main__':
    unittest.main()
#>>>>>>> 342872beb6a087e778d3166980c280bee753475c
