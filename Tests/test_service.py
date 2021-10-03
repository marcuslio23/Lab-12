from Repository.entitate_repository import FileRepository
from Service.aliment_service import AlimentService
from Service.magazin_service import MagazinService
from Tests.common import clear_file


def test_service():
    clear_file('magazin_test.txt')
    magazin_repository = FileRepository('magazin_test.txt')
    magazin_service = MagazinService(magazin_repository)
    magazin_service.create('01', 'asd', 'aaa')
    magazin_service.create('02', 'asd', 'aaa')
    assert len(magazin_service.get_all()) == 2
    assert magazin_service.get_all()[0].id_entitate == '01'
    assert magazin_service.get_all()[1].id_entitate == '02'

    clear_file('aliment_test.txt')
    aliment_repository = FileRepository('aliment_test.txt')
    alimen_service = AlimentService(aliment_repository, magazin_repository)
    alimen_service.create('01', '01', 'asd', '10.11.2020')
    alimen_service.create('02', '02', 'asdd', '11.11.2020')
    assert len(alimen_service.get_all()) == 2
    assert alimen_service.get_all()[0].id_entitate == '01'
    assert alimen_service.get_all()[1].id_entitate == '02'
