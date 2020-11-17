from math import pi
r = 10.6
a = 1.3    # un côté du rectangle
aire_cercle = pi*r**2
b = 0      # valeur de départ choisie pour l'autre côté du rectangle
while a*b < aire_cercle:
    b += 1
b -= 1     # doit annuler la dernière mise à jour pour obtenir la bonne valeur
print("La plus grande valeur possible de b : ", b)
