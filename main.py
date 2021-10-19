def factorial (n):
    factorial=1
    i=1
    while i<=n:
        factorial*=i
        i+=1
    return factorial


def get_base_16_from_2(nr_b2):
    '''

    Transformă un număr dat din baza 2 în baza 16. Numărul se dă în baza 2.
    :param1: numarul dat in baza 2
    :rezultat: numarul dat din baza 2 transformat in baza 16

    '''
    x = int(nr_b2, 2)  # transformarea numarului dat din baza 2 in baza 10
    rezultat = str(hex(x)[2:])  # convertirea numarului din baza 10 in baza 16, taind primele 2 caractere 0x
    return rezultat


def get_n_choose_k(n, k):
    '''
    :param1: n, combinari de cate elemente
    :param2: k, numarul de cate ori sunt luate cele n elemente
    :return: combinarile de n luate cate k
    '''
    n_k =n-k
    x = factorial(n)
    y = factorial(k)
    z = factorial(n_k)
    if n != k:
        combinari = x/(y*z)
    else:
        combinari = 1
    return combinari


def get_leap_years(an_1, an_2):
    '''

    :param an_1: anul de la care pornim cautarea anilor bisecti
    :param an_2: anul la care ne oprim cu cautarea anilor bisecti
    :return:  anii bisecti gasiti intre cei doi ani dati
    '''
    leap_years = []
    for i in range(an_1, an_2):
        if i % 4 == 0:
            if i % 100 == 0:
                if i % 400 == 0:
                    leap_years.append(i)
                    pass
            else:
                leap_years.append(i)
        else:
            pass
    return leap_years


def test_factorial():
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(2) == 2


def test_get_base_16_from_2():
    assert get_base_16_from_2("10") == "2"
    assert get_base_16_from_2("101") == "5"
    assert get_base_16_from_2("1111") == "f"


def test_get_n_choose_k():
    assert get_n_choose_k(3, 2) == 3
    assert get_n_choose_k(5, 3) == 20
    assert get_n_choose_k(2, 2) == 1


def test_get_leap_years():
    assert get_leap_years(2000, 2006) == '2004'
    assert get_leap_years(1901, 1918) == '1904, 1908, 1912, 1916'
    assert get_leap_years(2010, 2011) == '0'


def main():
    test_get_base_16_from_2()
    finish = False
    while not finish:
        print("1.transformati un nr din baza 2 in baza 16")
        print("2.Calculati combinari de n luate cate k")
        print("3.Gasiti anii bisecti intre 2 ani dati")
        print("x.Exit")
        optiune = input()
        if optiune == '1':
            nr_b2 = input("Adaugati un nr scris in baza 2:")
            print(get_base_16_from_2(nr_b2))
        elif optiune == '2':
            n = int(input("Adaugati n "))
            k = int(input("Adaugati k mai mic sau egal cu n "))
            print(get_n_choose_k(n, k))
        elif optiune == '3':
            an_1 = int(input("Introduceti primul an "))
            an_2 = int(input("introduceti al doilea an, mai mare ca primul introdus"))
            print(get_leap_years(an_1, an_2))

        elif optiune == 'x':
            finish = True
        else:
            print("Optiunea introdusa nu este valida, reincercati!")


if __name__ == "__main__":
    main()
