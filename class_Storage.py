"""
Шаг 1. Создайте абстрактный класс Storage.
"""
from errors import NotEnoughSpase, NotProduct, NotQuantityProduct
"""
Импорт ошибок
"""
from base_class import Base
"""
Импортируем абстрактный, родительский классов.
"""


class Storage(Base):
    """
    Создаем абстрактный класс наследованный от ABC
    """
    def __init__(self, items: dict[str:int], capacity: int):
        self.__items = items
        """
        Добавляем поле items которое будет словарем (название предмета:количество штук)
        """
        self.__capacity = capacity
        """
        Добавляем поле capacity которое будет целым числом(int) (емкость склада))
        """
    def add(self, title: str, quantity: int) -> None:
        """
        Метод add(<название>, <количество>) - увеличивает запас items (добавляет товар)
        """
        """
        Проверяем, хватает ди места на складе
        """
        if self.get_free_space() < quantity:
            """
            Если количество свободных мест меньше количества товара
            """
            raise NotEnoughSpase
        """
        Возвращаем ошибку
        """
        if title in self.__items:
            self.__items[title] += quantity
            """
            Если такое название товар  в списке товаров, то увеличиваем его количество
            """
        else:
            self.__items[title] = quantity
            """
            Иначе оставляем как есть то есть 0
            """

    def remove(self, title: str, quantity: int) -> None:
        """
        Метод remove(<название>, <количество>)-уменьшает запас items (удаляет товар)
        """
        if title not in self.__items:
            raise NotProduct
        """
        Проверяем наличие данной позиции товара на складе, если нет возвращаем ошибку
        """
        if self.__items[title] < quantity:
            raise NotQuantityProduct
        """
        Проверяем на наличие товара, если меньше чем надо, выдаем ошибку
        """
        self.__items -= quantity
        """
        Вычитаем определенное количество товара
        """
        if self.__items[title] == 0:
            del(self.__items[title])
        """
        Если товара осталось 0, удаляем этот товар из списка товаров (словаря) 
        """


    def get_free_space(self):
        """
        Метод get_free_space() - вернуть количество свободных мест
        """
        return self.__capacity - sum(self.__items.values())
    """
    Возвращает свободное место на складе, путем вычитания суммы количества 
    вещей из общего количества места на складе.
    """

    def get_items(self):
        """
        Метод get_items() - возвращает содержание склада в словаре {товар: количество}
        """
        return self.__items
    """
    возвращает словарь с содержимым склада
     """

    def get_unique_items_count(self):
        """
        Метод get_unique_items_count() - возвращает количество уникальных товаров
        """
        return len(self.__items)
    """
    Возвращает количество записей словаря
    """
        # return len(self.__items.keys())
    """
    Возвращает количество ключей словаря
    """

