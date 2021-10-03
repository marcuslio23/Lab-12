import jsonpickle
from Domain.entitate import Entitate


class FileRepository:

    def __init__(self, filename):
        self.__storage = {}
        self.__filename = filename

    def __read_file(self):
        try:
            with open(self.__filename, 'r') as f:
                self.__storage = jsonpickle.decode(f.read())
        except:
            self.__storage = {}

    def __write_file(self):
        with open(self.__filename, 'w') as f:
            f.write(jsonpickle.encode(self.__storage))

    def find_by_id(self, id_entitate):
        """
        Cauta entitatea cu id-ul dat

        :param id_entitate: id-ul
        :return: entitatea cu id-ul dat daca o gaseste sau None in caz contrar
        """
        self.__read_file()
        if id_entitate in self.__storage:
            return self.__storage[id_entitate]
        return None

    def create(self, entitate: Entitate):
        """
        Adauga in storage noua entitate

        :param entitate: entiatea
        :return:
        """
        if self.find_by_id(entitate.id_entitate) is not None:
            raise KeyError(f'Entitatea cu id-ul {entitate.id_entitate} exista deja!')
        self.__storage[entitate.id_entitate] = entitate
        self.__write_file()

    def update(self, entitate: Entitate):
        """
        Inlocuieste in storage entitatea modificata

        :param entitate: entitatea
        :return:
        """
        if self.find_by_id(entitate.id_entitate) is None:
            raise KeyError(f'Nu exista o entitate cu id-ul {entitate.id_entitate} pe care sa il actualizam!')
        self.__storage[entitate.id_entitate] = entitate
        self.__write_file()

    def delete(self, id_entitate):
        """
        Sterge din storage entitatea cu id-ul dat

        :param id_entitate: id-ul entitatii
        :return:
        """
        if self.find_by_id(id_entitate) is None:
            raise KeyError(f'Nu exista o entitate cu id-ul {id_entitate} pe care sa il stergem!')

        del self.__storage[id_entitate]
        self.__write_file()

    def get_all(self):
        """
        Returneaza toate valorile din storage

        :return: toate valorile din storage
        """
        self.__read_file()
        return list(self.__storage.values())
