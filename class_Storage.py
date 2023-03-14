"""
Шаг 1. Создайте абстрактный класс Storage.
"""
from errors import NotEnoughSpase
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
        Метод add(<название>, <количество>) - увеличивает запас items
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
        if

    def remove(self, title: str, quantity: int) -> None:
        """
        Метод remove(<название>, <количество>)-уменьшает запас items
        """
        pass

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

