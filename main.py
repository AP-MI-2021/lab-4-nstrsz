def citire_lista():
    l = []
    n = int(input("Dati nr. de elemente:"))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def print_menu():
    print("1. Citire lista")
    print("x. Iesire")


def nr_prim(n):
    '''
    Algoritmul stabileste daca un numar este sau nu prim
    :param n: numarul pe care il verificam
    :return: True daca numarul dat este prim, False in caz contrar
    '''
    if n<2:
        return False
    if n == 2:
        return True
    if n % 2== 0:
        return False
    for i in range(3,n//2+1,2):
        if n%i == 0:
            return True
    return True

def eliminare_elemente_prime(l):
    for i in range(0 , len(l)):
        if


def meniu():
    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        if optiune =="x":
            break

meniu()