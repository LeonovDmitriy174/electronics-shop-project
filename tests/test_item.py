"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item = Item('Milk', 100, 100)


def test_item():
    assert item.calculate_total_price() == 10000


def test_apply_discount():
    assert item.price == 100
    item.apply_discount()
    assert item.price == 150


def test_name():
    assert item.name == 'Milk'
    item.name = 'Cucumber'
    assert item.name == 'Cucumber'
    item.name = 'fishing rod'
    assert item.name == 'fishing ro'


def test_string_to_number():
    assert item.string_to_number('5') == 5
    assert item.string_to_number('6.2') == 6


def test_instantiate_from_csv():
    item.instantiate_from_csv('test.csv')
    assert len(item.all) == 1
