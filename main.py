def citire_lista():
    l = []
    n = int(input("Dati nr. de elemente:"))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def print_menu():
    print("1. Citire lista")
    print("2. Afisare lista dupa eliminarea elementelor prime")

    print("a. Afisare lista")
    print("x. Iesire")


def nr_prim(n):
    '''
    Algoritmul stabileste daca un numar este sau nu prim
    :param n: numarul pe care il verificam
    :return: True daca numarul dat este prim, False in caz contrar
    '''
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False
    return True


def afisare_lista(l):
    for x in l:
        print(x, " ")


def eliminare_elemente_prime(l):
    i = 0
    while i < len(l):
        if nr_prim(l[i]):
            l.pop(i)
        else:
            i = i + 1
    return l

def meniu():
    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(eliminare_elemente_prime(l))
        elif optiune == "a":
            afisare_lista(l)
        elif optiune == "x":
            break

meniu()

