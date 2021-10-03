from Domain.aliment import Aliment
from Domain.magazin import Magazin


def test_domain():
    magazin = Magazin('01', 'asd', 'asd')
    assert magazin.id_entitate == '01'
    assert magazin.nume == 'asd'
    assert magazin.cateogire == 'asd'

    aliment = Aliment('01', '01', 'asd', '11.11.2020')
    assert aliment.id_entitate == '01'
    assert aliment.id_magazin == '01'
    assert aliment.nume == 'asd'
    assert aliment.data_valabilitate == '11.11.2020'
