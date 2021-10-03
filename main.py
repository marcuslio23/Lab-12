from Repository.entitate_repository import FileRepository
from Service.magazin_service import MagazinService
from Service.aliment_service import AlimentService
from Tests.run_all_tests import run_all_tests
from UserInterface.console import Console


def main():
    magazin_repository = FileRepository("magazin.txt")
    magazin_service = MagazinService(magazin_repository)

    aliment_repository = FileRepository("aliment.txt")
    aliment_service = AlimentService(aliment_repository, magazin_repository)

    user_interface = Console(magazin_service, aliment_service)
    user_interface.run_console()


run_all_tests()
main()
