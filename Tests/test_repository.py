from Domain.aliment import Aliment
from Domain.magazin import Magazin
from Repository.entitate_repository import FileRepository
from Tests.common import clear_file


def test_repository():
    clear_file('magazin_test.txt')
    magazin_repository = FileRepository('magazin_test.txt')
    magazin = Magazin('01', 'asd', 'asd')
    magazin_repository.create(magazin)
    assert len(magazin_repository.get_all()) == 1

    clear_file('aliment_test.txt')
    aliment_repository = FileRepository('aliment_test.txt')
    aliment = Aliment('01', '01', 'asd', '11.11.2020')
    aliment_repository.create(aliment)
    assert len(aliment_repository.get_all()) == 1
