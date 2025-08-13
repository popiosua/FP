# 4. Dându-se numărul natural n, determina numerele prime p1 si p2 astfel ca n = p1 + p2
# (verificarea ipotezei lui Goldbach). Pentru ce fel de n exista soluție?

def prim(n):
    """
    Verifica daca un numar este prim
    n - numar intreg
    Return - True daca numarul e prim, respectiv False in caz contrar
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

def goldbach(n):
    """
    Verifica teorema lui goldbach daca un numar se poate scrie ca si suma de doua numere prime
    n - numar intreg
    Return - lista cu perechi de numere posibile ce satisfac teorema pentru numarul n
    """
    combinatii = []
    # print(f'Pentru numarul {n}')
    for i in range(n+1):
        if(prim(i) and prim(n-i)):
            combinatii.append((i, n-i))
    
    # print(f'Exista {len(combinatii)} combinatii')
    # print(combinatii)
    return combinatii

def test_goldbach():
    assert goldbach(1) == []
    assert goldbach(2) == []

    assert goldbach(18) == [(5, 13), (7, 11), (11, 7), (13, 5)]
    assert goldbach(14) == [(3, 11), (7, 7), (11, 3)]
    assert goldbach(7) == [(2, 5), (5, 2)]
    assert goldbach(6) == [(3, 3)]

if __name__ == '__main__':
    test_goldbach()