# 8. Pentru un număr natural n dat găsiți numărul natural maxim m format cu aceleași cifre. 
# Ex. n=3658, m=8653.

def maxim_cifre(n):
    """
    Gaseste cel mai mare numar ce se poate forma cu cifrele numarului primit
    n - numar natural
    Return - numar natural >= n 
    """
    cifre = []
    while(n):
        cifre.append(n%10)
        n = n // 10
    
    cifre.sort(reverse=True)

    maxim = 0
    for cifra in cifre:
        maxim = maxim * 10 + cifra
    
    return maxim

def test_maxim_cifre():
    assert maxim_cifre(0) == 0
    assert maxim_cifre(123) == 321
    assert maxim_cifre(987) == 987
    assert maxim_cifre(3658) == 8653

if __name__ == '__main__':
    test_maxim_cifre()
