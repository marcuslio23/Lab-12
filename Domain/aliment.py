from Domain.entitate import Entitate
from datetime import datetime

class Aliment(Entitate):
    """
    Descrie un aliment
    """
    def __init__(self, id_aliment, id_magazin, nume, data_valabilitate):
        super().__init__(id_aliment)
        self.__id_magazin = id_magazin
        self.__nume = nume
        self.__data_valabilitate = data_valabilitate

    @property
    def id_magazin(self):
        return self.__id_magazin

    @id_magazin.setter
    def id_magazin(self, value):
        self.__id_magazin = value

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, value):
        self.nume = value

    @property
    def data_valabilitate(self):
        return self.__data_valabilitate

    @data_valabilitate.setter
    def data_valabilitate(self, value):
        self.__data_valabilitate = value

    def __str__(self):
        return f'{self.id_entitate} - id_magazin:{self.__id_magazin}, nume:{self.__nume},' \
               f' data_valabilitate:{datetime.strftime(self.__data_valabilitate, "%d.%m.%Y")}'
