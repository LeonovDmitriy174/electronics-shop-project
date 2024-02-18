from src.item import Item


class Mixing:

    def __init__(self, name, price, quantity, language="EU"):
        self.__language = language
        super().__init__(name, price, quantity)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "RU":
            self.__language = "EN"
        else:
            self.__language = "RU"


class Keyboard(Mixing, Item):

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity, language)

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', {self.price}, "
                f"{self.quantity}, '{self.language}')")
