def aire_rectangle(longueur, largeur):
    return longueur * largeur

resultat = aire_rectangle(5, 3)
print("L'aire du rectangle est:", resultat)

def est_pair(n):
    return n % 2 == 0
print(est_pair(4))

def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print (maximum(5, 9))
def compter_jusqu_a(n):
    for i in range(1, n + 1):
        print(i)
compter_jusqu_a(5)


