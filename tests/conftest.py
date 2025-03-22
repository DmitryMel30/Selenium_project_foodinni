import pytest


@pytest.fixture()
def set_up():
    print("\nStart")
    yield
    print("Finish")


@pytest.fixture(scope="module")
def set_group():
    print("\nEnter system")
    yield
    print("Exit system")