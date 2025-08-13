"""
TODO lab3:
    - documentatie (document word sau ceva similar):
        - scenarii de rulare (curs1)
        - cazuri de testare (curs1)
    - teste in cod (assert)
    - specificatii functii
    - User Interface + cele doua probleme
"""

def test():
    """
    ruleaza toate testele din program
    input: -
    output: -
    """
    pass

class InvalidCommand(BaseException):
    """
    clasa care mosteneste BaseException
    folosita pentru a notifica cand o comanda primita
     de la utilizator nu e valida
    """
    pass

def handle_command(comanda):
    """
    trateaza comanda primita de la utilizator si
     redirecteaza catre functia care rezolva comanda ceruta
    input: comanda - numar natural din multimea {1, 2, 3, 4}
    output: True daca programul s-a terminat, False altfel
    raises: InvalidCommand cand comanda nu face parte din multimea {1, 2, 3, 4}
    """
    # varianta 1 - similar cu switch case din C/C++
    match comanda:
        case 1:
            # citim n numere naturale
            # intrebare: unde sunt stocate numerele naturale dupa?
            # idei: 1. adaugat parametru mutabil (lista, dictionar, clasa) care este modificat direct (clear + append)
            #       2. prin return + exit fortat prin exceptie noua, tratata prin "pass" in main
            pass
        case 2:
            # gaseste secventa 1 + afisare
            pass
        case 3:
            # gaseste secventa 2 + afisare
            pass
        case 4:
            # exit(0)  # termina tot programul principal,
            # poate duce la incheierea "prea brusca" a programului
            return True
            # fara clase, ar trebui returnate numerele
        case _:
            # default case, intra cand nu se face
            # match pe cele de dinainte

            # print(f"Command {comanda} is not valid!")  # caz exceptional de tratat;
            # merita considerata o exceptie de aruncat
            raise InvalidCommand(f"Command {comanda} is not valid!")
    return False

    """
    # varianta 2 - if-else
    if comanda == 1:
        # citim n numere naturale
        pass
    elif comanda == 2:
        # gaseste sir 1
        pass
    elif comanda == 3:
        # gaseste sir 2
        pass
    elif comanda == 4:
        return True
    else:
        raise InvalidCommand(f"Command {comanda} is not valid!")
    """

"""
# nice idea to read stuff from console

def generic_read(message, str_to_type):
    \"""
    citeste de la tastatura afisand mesajul
     message si converteste la tipul str_to_type
    input: message - un text, str_to_type - functie ce primeste un string si il
      converteste la orice valoare
    output: valoarea dupa apelul str_to_type pe datele primite de la utilizator
    \"""
    data = input(message)
    try:
        data = str_to_type(data)
    except ValueError:
        print(f"Invalid type: expected {str_to_type.__name__}")

# asa se poate apela:
generic_read("Reading an int: ", int)  # se va apela int(input(...)) => int
generic_read("Reading a string: ", str)  # se va apela str(input(...)) => str
"""

def start_ui():
    """
    porneste interfata grafica cu utilizatorul de tip consola
    input: -
    output: -
    """
    while True:
        try:
            comanda = int(input(">>"))
            if handle_command(comanda):
                break
        except ValueError:
            # se prinde exceptia aruncata de convertirea string->int
            print("We were expecting an integer!")
        except InvalidCommand as ex:
            # se prinde exceptia aruncata de handle_command
            print(ex)
    
def main():
    """
    functia principala a programului
    input: -
    output: -
    """
    start_ui()


if __name__ == "__main__":
    test()
    main()
