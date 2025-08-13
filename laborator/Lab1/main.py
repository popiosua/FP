def suma_n_numere(n):
    """
    Suma lui Gauss a primilor n termeni
    n - numar intreg
    Return - numar intreg, suma
    """
    suma = (1+n) * n /2
    return suma

def prim(n):
    """
    Verificare daca un numar este prim
    n - njumar intreg
    Return - True daca numarul este prim, False in caz contrar
    """
    if(n < 2):
        return False
    elif(n > 2 and n%2==0):
        return False
    
    div = 3

    while(div * div <= n):
        if(n % div == 0):
            return False
        
        div = div + 2
    
    return True

def prim_tastatura():
    """
    Citim un numar de la tastatura si verificam daca este prim
    Return - True daca numarul introdus e prim, respectiv False in caz contrar
    """
    n = int(input("Introduceti un numar:"))
    return prim(n)

def max_cmmdc(x, y):
    while(y):
        if(x > y):
            x = x - y
        else:
            y = y - x
    
    return x

def test_functii():
    assert suma_n_numere(10) == 55.0

    assert prim(2) == True
    assert prim(4) == False

    assert max_cmmdc(1, 2) == 1
    assert max_cmmdc(36, 4) == 4


if __name__ == '__main__':
    print(prim_tastatura())
