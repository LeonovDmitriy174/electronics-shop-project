"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    item = Item('Milk', 100, 100)
    assert item.calculate_total_price() == 10000
    item.apply_discount()
    assert item.price == 100
