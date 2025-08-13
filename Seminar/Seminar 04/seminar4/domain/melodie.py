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
    #return [titlu, artist, gen, durata]


def get_titlu(melodie)->str:
    """
    Returneaza titlul melodiei date
    :param melodie: melodia data
    :return: titlul melodiei
    """
    return melodie['titlu']


def get_artist(melodie):
    """
    Returneaza titlul melodiei date
    :param melodie: melodia data
    :return: titlul melodiei
    """
    return melodie['artist']


def get_gen(melodie):
    """
    Returneaza titlul melodiei date
    :param melodie: melodia data
    :return: titlul melodiei
    """
    return melodie['gen']


def get_durata(melodie):
    """
    Returneaza titlul melodiei date
    :param melodie: melodia data
    :return: titlul melodiei
    """
    return melodie['durata']


def test_creare_melodie():
    # Ce se intampla daca ne hotaram sa schimbam reprezentarea din dictionar in lista?
    # Sa reprezentam o melodie ca o lista cu [titlu, artist, gen, durata]
    # Trebuie sa schimbam cum am scris testele - or? Putem face altfel, astfel incat testele noastre
    # sa nu depinda de implementare?
    melodie1 = creare_melodie("T1", "A1", "gen1",3.4)
    assert(get_titlu(melodie1)=="T1")
    # melodie_de_test1 = {'titlu': 'T1', 'artist': 'A1', 'gen': 'folk', 'durata': 3.40}
    # assert (creare_melodie('T1', 'A1', 'folk', 3.40) == melodie_de_test1)
    # melodie_de_test2 = {'titlu': 'T2', 'artist': 'A2', 'gen': 'rock', 'durata': 7.3}
    # assert (creare_melodie('T2', 'A2', 'rock', 7.3) == melodie_de_test2)
