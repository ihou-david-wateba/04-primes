"""Module pour vérifier si un nombre est premier."""
from math import sqrt

#### Fonction secondaire


def isprime(p:int)->bool:
    """Vérifie si un nombre entier est premier."""
    # votre code ici
    rap=sqrt(p)
    if p<2:
        return False
    if p==2:
        return True
    # Pour cette boucle nous pouvons l'écrire de 2 manières
    # for i in range(2, int(rap)+1): ou for i in range(2, p-1): car on vérifie si tous les
    # nombres compris entre 2(inclus) et p-1(inclus)
    for i in range(2, int(rap) + 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main():
    """Fonction principale pour tester la fonction isprime."""
    # vos appels à la fonction secondaire ici
        #Tests de la fonction isprime
    print(isprime(2))#True
    print(isprime(3))#True
    print(isprime(4))#False
    print(isprime(5))#True
    print(isprime(10))#False
    print(isprime(17))#True
    print(isprime(20))#False

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
