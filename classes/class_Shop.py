"""
Шаг 3. Реализуйте класс Shop.
"""
from classes.class_Storage import Storage  # импортируем родительский класс
from errors import ShopFull  # импортируем ошибку


class Shop(Storage):  # создаем класс наследуемый от родительского класса Storage
    def __init__(self, items: dict, quantity: int = 20):
        super().__init__(items, quantity)  # наследуем поля из родительского класса

    def add(self, title: str, quantity: int) -> None:
        if title not in self.get_items() and self.get_unique_items_count() >= 5:
            raise ShopFull
        """
        Если товара нет в списке(словаре) товаров и количество наименований товара больше или равно 5, выдаем ошибку 
        """
        super().add(title, quantity)
        """
        В противном случае подтягиваем метод из родительского класса
        """