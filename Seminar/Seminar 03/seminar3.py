def afiseaza_meniu():
    print("1. Adauga melodie la lista")
    print("2. Cauta melodie dupa titlu si artist")
    print("3. Stergea unui cantec dupa titlu si artist")
    print("P. Afiseaza lista de melodii")
    print("E. Iesire din aplicatie")


# F1: add la lista

def citeste_info_melodie() -> tuple:
    titlu = input("Introduceti titlul melodiei:")
    artist = input("Introduceti artist melodiei:")
    gen = input("Introduceti genul melodiei:")
    durata = input("Introduceti durata melodiei:")
    durata = float(durata)
    return titlu, artist, gen, durata


def creare_melodie(titlu: str, artist: str, gen: str, durata: float) -> dict:
    """
    Creeaza melodie pe baza informatiilor date
    :param titlu: titlul melodiei
    :param artist: artistul melodiei
    :param gen: genul melodiei
    :param durata: durata melodiei
    :return: un dictionar care reprezinta meloldia
    """
    return {'titlu': titlu, 'artist': artist, 'gen': gen, 'durata': durata}
    # return [titlu, artist, gen, durata]


def add_to_list(lst_melodii: list, melodie: dict) -> None:
    """
    Adauga melodia data la lista de melodii
    :param lst_melodii: lista de melodii
    :param melodie: melodia care se adauga
    :return: -; lista data se modifica prin adaugarea melodiei la finalul listei
    """
    lst_melodii.append(melodie)


def cauta_melodie(lista_melodii: list, titlu_cautat: str, artist_cautat: str) -> dict:
    """
    Cauta o melodie in lista dupa titlu si artist
    :param lista_melodii: lista in care se cauta melodia
    :param titlu_cautat: titlul dupa care se cauta
    :param artist_cautat: artistul dupa care se cauta
    :return: melodia cu titlul si artistul dat, daca aceasta exista in lista
             None, altfel
    """
    for melodie in lista_melodii:
        if melodie['titlu'] == titlu_cautat and melodie['artist'] == artist_cautat:
            return melodie


def sterge_melodie(lista_melodii: list, titlu: str, artist: str):
    """
    Sterge melodia cu titlul si artistul dat, daca aceasta exista in lista
    :param lista_melodii: lista de melodii din care se sterge
    :param titlu: titlul melodiei pentru care se incearca stergerea
    :param artist: artistul melodiei pentru care se incearca stergerea
    :return: -; lista_melodii se modifica prin stergerea melodiei cu titlu, artist dat,
                daca aceasta melodie exista; altfel, lista ramane nemodificata
    """
    melodie_cautata = cauta_melodie(lista_melodii, titlu, artist)
    if melodie_cautata is not None:
        lista_melodii.remove(melodie_cautata)


def afiseaza_melodii(lista_melodii):
    for i, song in enumerate(lista_melodii):
        # end = "": don't jump to new line, end fiind caracterul
        # afisat dupa ultima valoare de afisat (by default, end=new line
        # de aceea de obicei print() afiseaza ce ii dam si apoi se trece la linie noua)
        print("Melodie #" + str(i) + ": ", end="")
        # construim un string cu informatiile unei melodii
        # (doar pentru exersare lucru cu str, se poate printa direct)
        song_info = ""
        for key, value in song.items():
            song_info += key.capitalize() + ": " + str(value) + " | "
        print(song_info)


def run():
    ruleaza_teste()
    lista_melodii = []
    is_running = True
    while is_running:
        afiseaza_meniu()
        optiune = input(">>>").upper().strip()
        match optiune:
            case '1':
                # add la lista
                titlu, artist, gen, durata = citeste_info_melodie()
                melodie = creare_melodie(titlu, artist, gen, durata)
                add_to_list(lista_melodii, melodie)
            case '2':
                # cautare in lista
                titlu_cautat = input("Titlul melodiei cautate: ")
                artist_cautat = input("Artistul melodiei cautate: ")
                melodie_cautata = cauta_melodie(lista_melodii, titlu_cautat, artist_cautat)
                if melodie_cautata is not None:
                    print("Melodia a fost gasita, acestea sunt toate informatiile despre ea:", melodie_cautata)
                else:
                    print("Melodia nu a fost gasita in lista.")
            case '3':
                # stergere din lista
                titlu_de_sters = input("Titlul melodiei de sters:")
                artist_de_sters = input("Artistul melodiei de sters: ")
                sterge_melodie(lista_melodii, titlu_de_sters, artist_de_sters)
                # cum sa verificam daca s-a sters ceva pentru a afisa mesaj de succes
                # sau mesaj ca nu s-a gasit melodia in lista?
            case 'P':
                afiseaza_melodii(lista_melodii)

            case 'E':
                is_running = False


def test_creare_melodie():
    # Ce se intampla daca ne hotaram sa schimbam reprezentarea din dictionar in lista?
    # Sa reprezentam o melodie ca o lista cu [titlu, artist, gen, durata]
    # Trebuie sa schimbam cum am scris testele - or? Putem face altfel, astfel incat testele noastre
    # sa nu depinda de implementare?
    melodie_de_test1 = {'titlu': 'T1', 'artist': 'A1', 'gen': 'folk', 'durata': 3.40}
    assert (creare_melodie('T1', 'A1', 'folk', 3.40) == melodie_de_test1)
    melodie_de_test2 = {'titlu': 'T2', 'artist': 'A2', 'gen': 'rock', 'durata': 7.3}
    assert (creare_melodie('T2', 'A2', 'rock', 7.3) == melodie_de_test2)


def test_add_to_list():
    test_list = []
    assert (len(test_list) == 0)
    add_to_list(test_list, creare_melodie('T1', 'A1', 'folk', 3.40))
    assert (len(test_list) == 1)

    add_to_list(test_list, creare_melodie('T2', 'A2', 'rock', 4.02))
    assert (len(test_list) == 2)


def test_cauta_in_lista():
    melodie1 = {'titlu': 'T1', 'artist': 'A1', 'gen': 'folk', 'durata': 3.40}
    melodie2 = {'titlu': 'T2', 'artist': 'A2', 'gen': 'pop', 'durata': 5.2}
    melodie3 = {'titlu': 'Thunderstruck', 'artist': 'AC/DC', 'gen': 'rock', 'durata': 4.10}
    test_list = [melodie1, melodie2, melodie3]
    assert (cauta_melodie(test_list, "T1", "A1") == melodie1)
    assert (cauta_melodie(test_list, "Highway to Hell", "AC/DC") is None)
    assert (cauta_melodie(test_list, "t1", "a1") is None)
    # inversat artist cu titlu
    assert (cauta_melodie(test_list, "A1", "T1") is None)


def test_stergere_din_lista():
    melodie1 = {'titlu': 'T1', 'artist': 'A1', 'gen': 'folk', 'durata': 3.40}
    melodie2 = {'titlu': 'T2', 'artist': 'A2', 'gen': 'pop', 'durata': 5.2}
    melodie3 = {'titlu': 'Thunderstruck', 'artist': 'AC/DC', 'gen': 'rock', 'durata': 4.10}
    test_list = [melodie1, melodie2, melodie3]
    assert (len(test_list) == 3)
    sterge_melodie(test_list, "T1", "A1")
    assert (len(test_list) == 2)
    sterge_melodie(test_list, "Titlu", "Artist")
    assert (len(test_list) == 2)
    sterge_melodie(test_list, "T2", "A2")
    assert (len(test_list) == 1)
    sterge_melodie(test_list, "Thunderstruck", "AC/DC")
    assert (len(test_list) == 0)

    test_list2 = []
    assert (len(test_list2) == 0)
    sterge_melodie(test_list2, "T1", "A1")
    assert (len(test_list2) == 0)


def ruleaza_teste():
    test_creare_melodie()
    test_add_to_list()
    test_cauta_in_lista()
    test_stergere_din_lista()
    print("[INFO]: Au trecut toate testele")


run()
