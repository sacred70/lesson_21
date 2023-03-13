from abstractstorage import Storage  # импортируем родительский абстрактный класс


class Store(Storage):  # создаем класс наследуемый от абстрактного класса Storage
    def __init__(self, items: dict, quantity: int = 100):
        super().__init__(items, quantity)
