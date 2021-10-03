from Domain.magazin import Magazin
from Repository.entitate_repository import FileRepository


class MagazinService:
    def __init__(self, magazin_reposiotry: FileRepository):
        self.__magazin_repository = magazin_reposiotry

    def create(self, id_magazin, nume, categorie):
        """
        Creeaza un magazin

        :param id_magazin: id-ul magazinului
        :param nume: numele magazinului
        :param categorie: categoria
        :return: -
        """
        if nume == '':
            raise ValueError('Numele trebuie sa fie un string nenul!')
        magazin = Magazin(id_magazin, nume, categorie)
        self.__magazin_repository.create(magazin)

    def get_all(self):
        """
        Returneaa toate magazinele

        :return: toate magaiznele
        """
        return self.__magazin_repository.get_all()
