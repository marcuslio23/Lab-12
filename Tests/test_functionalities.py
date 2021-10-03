from Repository.entitate_repository import FileRepository
from Service.aliment_service import AlimentService
from Service.magazin_service import MagazinService
from Tests.common import clear_file
from datetime import datetime

def test_functionalities():
    clear_file('magazin_test.txt')
    magazin_repository = FileRepository('magazin_test.txt')
    magazin_service = MagazinService(magazin_repository)
    magazin_service.create('01', 'asd', 'aaa')
    magazin_service.create('02', 'asd', 'aaa')

    clear_file('aliment_test.txt')
    aliment_repository = FileRepository('aliment_test.txt')
    aliment_service = AlimentService(aliment_repository, magazin_repository)
    aliment_service.create('01', '01', 'afsddsaffsd', datetime.strptime('10.11.2020', '%d.%m.%Y'))
    aliment_service.create('02', '02', 'wqerwe', datetime.strptime('20.12.2020', '%d.%m.%Y'))

    assert len(aliment_service.alimente_ok()) == 0

    magazine_sortate, nr, x = aliment_service.magazine_cresc_dupa_nr_alimente()
    assert magazine_sortate[0].id_entitate == '01'
