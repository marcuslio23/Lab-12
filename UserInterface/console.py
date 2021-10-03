from Service.magazin_service import MagazinService
from Service.aliment_service import AlimentService
from datetime import datetime


class Console:
    def __init__(self, magazin_service: MagazinService, aliment_service: AlimentService):
        self.__magazin_service = magazin_service
        self.__aliment_service = aliment_service

    def run_console(self):
        while True:
            print('1. Create magazint.')
            print('2. Create aliment.')
            print('3. Show all magazine')
            print('4. Show all alimente')
            print('5. Afisarea magazinelor in ordine crescatoare dupa numarul alimentelor.')
            print('6. Afisarea tuturor alimentelor ce se gasesc in mai multe magazine si nu sunt expirate')
            print('7. Export excel.')
            print('x. Iesire.')
            option = input('Alegeti optiunea: ')
            if option == '1':
                self.run_create_magazin()
            elif option == '2':
                self.run_create_aliment()
            elif option == '3':
                self.run_show_all_magazine()
            elif option == '4':
                self.run_show_all_alimente()
            elif option == '5':
                self.run_afis_magazine_ord_cresc_dupa_nr_alimente()
            elif option == '6':
                self.run_afis_alimante_ce_is_in_mai_mult_de_doua_mag_si_neexpirate()
            elif option == '7':
                self.run_export_excel()
            elif option == 'x':
                break
            else:
                print('Optiune invalida. Reincercati!')

    def run_create_magazin(self):
        try:
            id_magazin = input('Dati id-ul magazinului: ')
            nume = input('Dati numele magazinului: ')
            categorie = input('Dati categoria: ')
            self.__magazin_service.create(id_magazin, nume, categorie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as ex:
            print(ex)

    def run_create_aliment(self):
        try:
            id_aliment = input('Dati id-ul alimentului: ')
            id_magazin = input('Dati id-ul magazinului: ')
            nume = input('Dati numele alimentului: ')
            data_valabilitate = input('Dati data valabilitatii: ')
            data_valabilitate = datetime.strptime(data_valabilitate, '%d.%m.%Y')
            self.__aliment_service.create(id_aliment, id_magazin, nume, data_valabilitate)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as ex:
            print(ex)

    def run_show_all_magazine(self):
        for magazin in self.__magazin_service.get_all():
            print(magazin)

    def run_show_all_alimente(self):
        for aliment in self.__aliment_service.get_all():
            print(aliment)

    def run_afis_magazine_ord_cresc_dupa_nr_alimente(self):
        rez_mag, mag_al, ctg_al = self.__aliment_service.magazine_cresc_dupa_nr_alimente()
        for magazin in rez_mag:
            print(magazin, '| nr alimente: ', mag_al[magazin.id_entitate])
        print('\n')
        for categorie in ctg_al:
            print(categorie, '| nr alimente din categorie: ', ctg_al[categorie])

    def run_afis_alimante_ce_is_in_mai_mult_de_doua_mag_si_neexpirate(self):
        rez = self.__aliment_service.alimente_ok()
        for aliment in rez:
            if aliment[1] >= 2:
                print(aliment[0], '| nr magazine: ', aliment[1])

    def run_export_excel(self):
        #file_name = input('Dati numele fisierului: ')
        #file_name = file_name + '.xlsx'
        self.__aliment_service.export_excel()
