from src.keyboard import Keyboard


keyboard = Keyboard("Razer", 10000, 10)


def test_init():
    assert keyboard.name == "Razer"
    assert keyboard.language == "EN"


def test_repr_and_str():
    assert repr(keyboard) == "Keyboard('Razer', 10000, 10, 'EN')"
    assert str(keyboard) == 'Razer'


def test_change_language():
    try:
        keyboard.language = "RU"
    except AttributeError:
        keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"
