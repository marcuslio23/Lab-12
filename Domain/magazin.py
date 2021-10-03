from Domain.entitate import Entitate


class Magazin(Entitate):
    """
    Descrie un magazin
    """
    def __init__(self, id_magazin, nume, categorie):
        super().__init__(id_magazin)
        self.__nume = nume
        self.__cateogire = categorie

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, value):
        self.__nume = value

    @property
    def cateogire(self):
        return self.__cateogire

    @cateogire.setter
    def cateogire(self, value):
        self.__cateogire = value

    def __str__(self):
        return f'{self.id_entitate} - nume:{self.__nume}, categorie:{self.__cateogire}'
