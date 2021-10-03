from Tests.test_domain import test_domain
from Tests.test_functionalities import test_functionalities
from Tests.test_repository import test_repository
from Tests.test_service import test_service


def run_all_tests():
    test_domain()
    test_repository()
    test_service()
    test_functionalities()
