from domain.melodie import get_durata, creare_melodie, get_gen, get_titlu
from list_management.list_manager import add_to_list


#https://www.geeksforgeeks.org/args-kwargs-python/

def filter_cu_functie(lista_melodii, fct_criteriu_filtrare, *args):
    print("Args is: ", args)
    return [melodie for melodie in lista_melodii if fct_criteriu_filtrare(melodie, *args)]


def filter_by_durata(melodie, durata_s, durata_f):
    return durata_s < get_durata(melodie) < durata_f


def filter_by_gen(melodie, gen):
    return get_gen(melodie) == gen


def filter_by_title(melodie):
    """
    Returneaza True daca titlul melodiei contine cuvantul "the", False altfel
    :param melodie:
    :return:
    """
    return get_titlu(melodie).lower().find("the") != -1


def test_filter_cu_functie():
    melodie1 = creare_melodie("T1", "A1", "pop", 2.33)
    melodie2 = creare_melodie("T2", "A2", "folk", 3)
    melodie3 = creare_melodie("T3", "A4", "rock", 5)
    melodie4 = creare_melodie("T4", "A5", "rock", 8)
    test_list = []
    add_to_list(test_list, melodie1)
    add_to_list(test_list, melodie2)
    add_to_list(test_list, melodie3)
    add_to_list(test_list, melodie4)

    lista_filtrata = filter_cu_functie(test_list, filter_by_durata, 2, 10)
    assert (len(lista_filtrata) == 4)

    lista_filtrata = filter_cu_functie(test_list, filter_by_durata, 1, 4)
    assert (len(lista_filtrata) == 2)

    lista_filtrata = filter_cu_functie(test_list, filter_by_durata, 7, 9)
    assert (len(lista_filtrata) == 1)

    lista_filtrata = filter_cu_functie(test_list, filter_by_gen, "gen")
    assert (len(lista_filtrata) == 0)

    lista_filtrata = filter_cu_functie(test_list, filter_by_gen, "pop")
    assert (len(lista_filtrata) == 1)

    lista_filtrata = filter_cu_functie(test_list, filter_by_gen, "rock")
    assert (len(lista_filtrata) == 2)

    lista_filtrata = filter_cu_functie(test_list, filter_by_title)
    assert (len(lista_filtrata) == 0)


test_filter_cu_functie()
