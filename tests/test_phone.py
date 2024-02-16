import pytest
from src.phone import Phone

phone1 = Phone("Iphone 15", 120000, 15, 2)
phone2 = Phone("Iphone 14", 100000, 10, 2)


def test_init():
    assert phone1.name == "Iphone 15"
    assert phone1.number_of_sim == 2


def test_add():
    assert phone1 + phone2 == 25
    with pytest.raises(TypeError):
        phone1 + 1


def test_number_of_sim():
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_repr():
    assert repr(phone1) == "Phone('Iphone 15', 120000, 15, 2)"
