## NOM DU PROGRAMME: MC_integral.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt

def MC_Integral(f, a, b, N):
    # N  nombre d'essais
    x = np.linspace(a, b, 100)
    ymin = min(f(x))
    ymax = max(f(x))
    np.random.seed(6)   # pour fixer un nombre alléatoires
                        # pour avoir un résultat reproductible
    x_rand = a + (b - a) * np.random.rand(N)
    y_rand = (ymax - ymin) * np.random.rand(N)
    # nombre de points dans l'aire de la fonction (Air sous la fonction)
    n = np.sum(y_rand - f(x_rand) < 0.0)
    # valeur approchée de pi
    print('PI numpy       : ', np.pi)
    print('PI monte carlo : ', 4*n/N)
    print('différence     : ', 4*n/(N) - np.pi)
    #----- Sortie et graphiques -------------------
    index_below = np.where(y_rand < f(x_rand))
    index_above = np.where(y_rand >= f(x_rand))
    plt.figure(figsize=(7,7))
    plt.plot(x,f(x),'--k')
    plt.scatter(x_rand[index_below], y_rand[index_below],
                c="r", s = 5, label = "Pts sous la courbe")
    plt.scatter(x_rand[index_above], y_rand[index_above],
                c="b", s = 5, label = "Pts au-dessus de la courbe")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), ncol=2)
    plt.show()
    #print(np.mean(f(x_rand))*(b-a)) # aire de la fonction
    
if __name__ == "__main__":
    f = lambda x : np.sqrt(1-x*x)
    N = 1000
    MC_Integral(f, 0, 1, N)
