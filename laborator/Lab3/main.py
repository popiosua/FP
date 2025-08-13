def citire():
    """
    Citeste o lista de numere de la utilizator
    Return - lista de numere
    """
    numere = input("Dati lista de nummere: ")
    numere = numere.split(',')
    list_nr = []
    for elem in numere:
        list_nr.append(int(elem))
    print('Lista actualizata\n')
    return list_nr
    

# 2. Contine cel mult trei valori distincte
def dist_3(lista):
    """
    Returneaza secventa cea mai lunga din lista ce are cel mult trei valori distincte
    list - lista de intregi
    Return - lista de numere ce satisface conditia
    """
    x = y = 0
    for i in range(len(lista)):
        distincte = []
        j = i
        while(j < len(lista) and len(distincte) <= 3):
            if(lista[j] not in distincte):
                distincte.append(lista[j])
            
            j = j+1
        
        if(len(distincte) == 4):
            j = j - 1

        if(j - i > y - x):
            x = i
            y = j

        i = j
    # print(f'{x} {y+1}')
    return lista[x:y]
        
# 8. au toate elementele in intervalul [0, 10] dat
def interval(lista):
    """
    Returneaza secventa cea mai lunga din lista ce are elemente din intervalul [0-10]
    list - lista de intregi
    Return - lista de numere ce satisface conditia
    """
    x = y = 0
    nr = [0,1,2,3,4,5,6,7,8,9,10]
    for i in range(len(lista)):
        j = i
        while(j < len(lista) and lista[j] in nr):
            j = j + 1
    

        if(j - i > y - x):
                x = i
                y = j
        
        i = j
    # print(f'{x} {y+1}')
    return lista[x:y]

# Consola
def meniu():
    """
    Afiseaza optiunile utilizatorului
    """
    print(
        '1 Citirea unei liste de numere intregi (separrate prin prigula)\n' \
        'Gasirea secventelor de lungime maxima care respectă o proprietatea:\n' \
        '2 Contine cel mult trei valori distincte\n' \
        '3 Au toate elementele in intervalul [0, 10] dat\n' \
        '4 Iesire din aplicatie.\n'
        )

def consola():
    """
    Programul principal (coordonator)
    Se afiseaza meniul si asteapta optiune de la utilizator
    in functie de ce alege utilizatorul se afiseaza raspunsul pana ce se inchide programul
    """
    list = []
    while(True):
        meniu()
        optiune = int(input("Optiunea: "))
        match optiune:
            case 1: 
                list = citire()
            case 2:
                print(dist_3(list))
            case 3:
                print(interval(list))
            case 4:
                return
        
            case default:
                print('Optiune invalida.\n')

def test_dist_3():
    """
    Functie ce testeaza proprietatea secventa cu cel mult 3 valori distincte intr-o secventa
    """
    assert dist_3([1,2,3]) == [1,2,3]
    assert dist_3([]) == []
    assert dist_3([1,2,31,1,2,1,10]) == [1,2,31,1,2,1] 

def test_interval():
    """
    Functie ce testeaza proprietate secventa cu elementele din intervalul [0,10]
    """
    assert interval([1,2,3]) == [1,2,3]
    assert interval([]) == []
    assert interval([1,2,1,1,2,1,10,1,2,3]) == [1,2,1,1,2,1,10,1,2,3] 

if __name__ == '__main__':
    test_dist_3()
    test_interval()
    consola()