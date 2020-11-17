from math import pi, sqrt
N = int(input('Donnez le nombre de termes en somme pour pi: '))

# Leibniz
sum1 = 0
cptLeibniz = 0
while cptLeibniz <= N :
    sum1 += 1.0/((4*cptLeibniz + 1)*(4*cptLeibniz + 3))
    cptLeibniz+=1 
    
sum1 *= 8
print ("Leibniz pi : ", sum1)
Leibniz_error = abs(pi - sum1)
print ("Leibniz erreur: ", Leibniz_error)

# Euler
sum2 = 0
cptEuler = 1
while cptEuler <= N :
    sum2 += 1.0/cptEuler**2
    cptEuler+=1

sum2 *= 6
sum2 = sqrt(sum2)
print("Euler pi : ", sum2)
Euler_error = abs(pi - sum2)
print("Euler erreur : ", Euler_error)

