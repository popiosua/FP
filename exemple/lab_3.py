
class Persoana:
    _total_persoane = 0  # atribut static al clasei Persoana

    def __init__(self, varsta, nume):  # constructorul clasei Persoana
        self.varsta = varsta  # variabila public - este accesibila de oriunde
        self.nume = nume
        self.__cnp = "abc"  # variabila private - nu poate fi accesat din afara clasei
        self._protected_stuff = "abc"  # variabila protected - la fel ca private, dar pot fi accesate de clasele ce
                                       # mostenesc Persoana
        Persoana._total_persoane += 1

    def __str__(self):  # suprascrie outputul functiei str(persoana)
                        # instance method - opereaza date la nivelul unei instante de tip Persoana
        return f"Salut, sunt {self.nume}, am {self.varsta} ani"

    @classmethod  # class method - opereaza date de la nivelul clasei Persoana
    def total_persoane(cls):
        return cls._total_persoane

    @staticmethod  # static method - nu acceseaza sau modifica starea unei clase sau al unui obiect din clasa Persoana
    def print_hello():
        print("Hello there!")


class Student(Persoana):  # mosteneste clasa Persoana, deci primeste atributele si metodele unei Persoane
    def rezolva_test(self, intrebari):
        return ["b", "c", "e"]


class Profesor(Persoana):
    def creeaza_test(self):
        intrebari = ["A", "B", "C"]
        raspunsuri = ["b", "c", "d"]
        return intrebari, raspunsuri

    def evalueaza_test(self, raspunsuri, raspunsuri_student):
        total_raspunsuri_corect = 0
        for raspuns_corect, raspuns_student in zip(raspunsuri, raspunsuri_student):  # zip itereaza prin doua liste simultan
            total_raspunsuri_corect += int(raspuns_corect == raspuns_student)  # adauga 1 daca boolea-ul este True, altfel aduna 0
        return total_raspunsuri_corect / len(raspunsuri) * 10

    def __str__(self):
        return f"{super().__str__()} si sunt un profesor"  # super() acceseaza clasa parinte


def main():
    p = Profesor(50, "Vancea")
    s = Student(19, "Alexandru")
    intrebari, raspunsuri = p.creeaza_test()
    raspunsuri_student = s.rezolva_test(intrebari)
    nota = p.evalueaza_test(raspunsuri, raspunsuri_student)
    print(nota)
    print(p)  # converteste obiectul primite la string cu metoda str
    print(s)
    print(Persoana.total_persoane())
    Persoana.print_hello()


if __name__ == '__main__':
    main()
