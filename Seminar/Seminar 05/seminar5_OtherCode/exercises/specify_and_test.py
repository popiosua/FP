#Specificati si testati urmatoarele functii:

def f1(x):
    """
    TO ADD: ce face functia
    :param x: tipul parametrului (fie aici, fie type hint), scurta descriere, preconditii
    :return: tipul returnat, descriere (ce reprezinta?), postconditii
    :raises: tipul de exceptie ridicat si cazul in care aceasta este ridicata
            ValueError daca numarul dat e negativ
    """
    if x < 0:
        raise ValueError()
    a = 0
    while x != 0:
        a += x % 10
        x = x // 10
    return a



def f2(x):
    if len(x) < 3:
        raise ValueError()
    d = {0: 0, 1: 0}

    for e in x:
        d[e % 2] += 1

    return d[1]


def f3(x):
    if x < 0:
        raise ValueError
    i = 0
    while x != 0:
        x = x // 2
        i += 1
    return i - 1


def f4(x):
    if len(x) < 3:
        raise ValueError()

    a = 0
    b = 0
    for i in range(len(x)):
        if x > 0:
            a += 1
        else:
            b += 1
    return a > b


print(f4([1, 2, 3, 4]))
