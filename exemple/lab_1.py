
"""
# cum se specifica o functie:
def functie():
    \"""
    <descriere>
    input: <descriere input>
    output: <descriere output>
    <raises, if any>
    \"""
"""

def read_numbers():
    """
    citeste un numar n si n numere intregi de la tastatura
    input: -
    output: numbers - un sir de numere intregi
    """
    n = int(input("n = "))
    numbers = []
    for i in range(n):
        number = int(input(f"number[{i}] = "))
        numbers.append(number)
    return numbers

def compute_sum(numbers):
    """
    calculeaza suma numerelor din numbers
    input: numbers - o lista de numere naturale
    output: suma - suma numerelor din numbers
    """
    suma = 0
    for element in numbers:
        suma += element
    return suma

def print_sum(suma):
    """
    afiseaza suma pe ecran
    input: suma - suma numerelor calculate, un intreg
    output: -
    """
    print(f"Suma numerelor este: {suma}")

def test_compute_sum():
    """
    testeaza compute_sum
    input: -
    output: -
    """
    assert compute_sum([1, 2, 3]) == 6
    assert compute_sum([]) == 0
    # assert compute_sum([]) == 1  # test care crapa (arunca exceptie)

def test():
    """
    ruleaza toate testele din program
    input: -
    output: -
    """
    test_compute_sum()

def main():
    """
    functia principala a programului
    input: -
    output: -
    """
    numbers = read_numbers()
    suma = compute_sum(numbers)
    print_sum(suma)
    
if __name__ == "__main__":
    test()
    # daca testele trec, apelam functia main
    main()

# print("Hello world!")# comentariu pe o linie

"""
comentariu multiline
"""
