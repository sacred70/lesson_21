"""
Шаг 2. Реализуйте класс Store. В нем хранится любое количество любых товаров.
"""

from class_Storage import Storage  # импортируем родительский класс


class Store(Storage):  # создаем класс наследуемый от родительского класса Storage
    def __init__(self, items: dict, quantity: int = 100):
        super().__init__(items, quantity)  # наследуем поля из родительского класса
