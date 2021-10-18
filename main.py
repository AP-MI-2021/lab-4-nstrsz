def citire_lista():
    l = []
    n = int(input("Dati nr. de elemente:"))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def print_menu():
    print("1. Citire lista")
    print("2. Afisare lista dupa eliminarea elementelor prime")
    print("3. Este media aritmetica mai mare decat un numar dat?")
    print("4. Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului.")
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

def media_aritmetica_lista(l):
    '''
    algoritmul calculeaza media aritmetica a numerelor intregi dintr-o lista
    :param l: lista de numere intregi
    :return: media aritmetica a numerelor intregi din lista
    '''
    m=0
    c=0
    for x in l:
        m = m + x
        c = c + 1
    return m//c


def este_media_aritmetica_mai_mare_decat_n(l,n):
    '''
    Algoritmul stabileste daca media aritmetica a numerelor dintr-o lista este mai mare decat un numar n dat
    :param l: lista de numere intregi
    :param n: numarul fata de care verificam ca media aritmetica sa fie mai mare
    '''
    if media_aritmetica_lista(l) > n:
        print("Da")
    else:
        print("Nu")


def nr_div_proprii(n):
    ''' Stabileste numarul de divizori proprii ai unui numar, returnand acel numar'''
    c=0
    for i in range (2,n//2+1):
        if n%i==0:
            c=c+1
    return c


def afisare_lista_cu_nr_de_div_proprii(l):
   '''
   Algoritmul stabileste daca un numar este sau nu prim
   :param n: numarul pe care il verificam
   :return: True daca numarul dat este prim, False in caz contrar
   '''
   i=0
   while i<len(l):
       l.insert(i+1,nr_div_proprii(l[i]))
       i=i+2
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
        elif optiune =="3":
            n=int(input("Dati n: "))
            este_media_aritmetica_mai_mare_decat_n(l,n)
        elif optiune == "4":
            print(afisare_lista_cu_nr_de_div_proprii(l))
        elif optiune == "a":
            afisare_lista(l)
        elif optiune == "x":
            break

meniu()