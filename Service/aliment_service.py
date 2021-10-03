from tkinter import filedialog
from Domain.aliment import Aliment
from Repository.entitate_repository import FileRepository
from datetime import datetime
import pandas as pd
import tkinter as tk


class AlimentService:
    def __init__(self, aliment_repository: FileRepository, magazin_repository: FileRepository):
        self.__aliment_repository = aliment_repository
        self.__magazin_repository = magazin_repository

    def create(self, id_aliment, id_magazin, nume, data_valabilitate):
        """
        Creeaza un aliment

        :param id_aliment: id-ul alimentului
        :param id_magazin:id-ul magazinului
        :param nume: numele alimentului
        :param data_valabilitate: data de valabilitate
        :return: -
        """
        if self.__magazin_repository.find_by_id(id_magazin) is None:
            raise KeyError("Magazinul cu id-ul introdus nu exista!")
        if nume == '':
            raise ValueError("Numele trebuie sa fie un string nenul!")
        aliment = Aliment(id_aliment, id_magazin, nume, data_valabilitate)
        self.__aliment_repository.create(aliment)

    def get_all(self):
        """
        Returneaza toate alimentele
        :return: toate alimentele
        """
        return self.__aliment_repository.get_all()

    def magazine_cresc_dupa_nr_alimente(self):
        """
        Ordoneaza magazinele crescator dupa numarul de alimente

        :return: magazinele ordonate crescator dupa numarul de alimente
        """
        magazine_alimente = {}
        categorii_alimente = {}
        for aliment in self.__aliment_repository.get_all():
            if aliment.id_magazin not in magazine_alimente:
                magazine_alimente[aliment.id_magazin] = 1
            else:
                magazine_alimente[aliment.id_magazin] = magazine_alimente[aliment.id_magazin] + 1
        magazine_alimente_sortate = sorted(magazine_alimente.items(), key=lambda x: x[1])
        rez_mag = []
        for magazin in magazine_alimente_sortate:
            rez_mag.append(self.__magazin_repository.find_by_id(magazin[0]))

        for aliment in self.__aliment_repository.get_all():
            magazin = self.__magazin_repository.find_by_id(aliment.id_magazin)
            if magazin.cateogire not in categorii_alimente:
                categorii_alimente[magazin.cateogire] = 1
            else:
                categorii_alimente[magazin.cateogire] = categorii_alimente[magazin.cateogire] + 1

        return rez_mag, magazine_alimente, categorii_alimente

    def alimente_ok(self):
        """
        Returneaza alimentele ce se gasesc in mai mult de doua magazine si nu sunt expirate

        :return: alimenele ce se gasesc in mai mult de doua magzine si nu sunt expirate
        """
        # data = '14.12.2020'
        # data = datetime.strptime(data, '%d.%m.%Y')
        data = datetime.today()
        aliment_magazin = {}
        for aliment in self.__aliment_repository.get_all():
            if aliment.data_valabilitate >= data:
                if aliment.nume not in aliment_magazin:
                    aliment_magazin[aliment.nume] = 1
                else:
                    aliment_magazin[aliment.nume] = aliment_magazin[aliment.nume] + 1
        aliment_magazin = list(aliment_magazin.items())
        return aliment_magazin
    """
    def export_excel(self, file_name):
        d = {}
        l = []
        for magazin in self.__magazin_repository.get_all():
            d[magazin.cateogire] = []
            if magazin.cateogire not in l:
                l.append(magazin.cateogire)
        for magazin in self.__magazin_repository.get_all():
            for aliment in self.__aliment_repository.get_all():
                if aliment.id_magazin == magazin.id_entitate:
                    if aliment.nume not in d[magazin.cateogire]:
                        d[magazin.cateogire].append(aliment.nume)

        dnew = {}
        for element in d:
            res = {i: d[element][i] for i in range(0, len(d[element]))}
            dnew[element] = res

        df = pd.DataFrame(dnew)
        df.to_excel(file_name)
    """

    def export_excel(self):
        d = {}
        l = []
        for magazin in self.__magazin_repository.get_all():
            d[magazin.cateogire] = []
            if magazin.cateogire not in l:
                l.append(magazin.cateogire)
        for magazin in self.__magazin_repository.get_all():
            for aliment in self.__aliment_repository.get_all():
                if aliment.id_magazin == magazin.id_entitate:
                    if aliment.nume not in d[magazin.cateogire]:
                        d[magazin.cateogire].append(aliment.nume)

        dnew = {}
        for element in d:
            res = {i: d[element][i] for i in range(0, len(d[element]))}
            dnew[element] = res
        df = pd.DataFrame(dnew)

        root = tk.Tk()

        canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
        canvas1.pack()

        def exportExcel():

            export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
            df.to_excel(export_file_path, index=False, header=True)
            root.destroy()

        saveAsButtonExcel = tk.Button(text='Export Excel', command=exportExcel, bg='green', fg='white',
                                      font=('helvetica', 12, 'bold'))
        canvas1.create_window(150, 150, window=saveAsButtonExcel)

        root.mainloop()