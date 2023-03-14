"""
Шаг 0. Создайте абстрактный родительский класс.
"""

from abc import ABC, abstractmethod  # импортируем модули и декораторы для создания абстрактных классов


class Base(ABC):
    """
    Создаем абстрактный класс наследованный от ABC
    """
    @abstractmethod  # декоратор абстрактного метода
    def add(self, title: str, quantity: int) -> None:  # метод add(<название>, <количество>) - увеличивает запас items
        pass

    @abstractmethod  # декоратор абстрактного метода
    def remove(self, title: str, quantity: int) -> None:  # метод remove(<название>, <количество>)-уменьшает запас items
        pass

    @abstractmethod  # декоратор абстрактного метода
    def get_free_space(self):  # метод get_free_space() - вернуть количество свободных мест
        pass

    @abstractmethod  # декоратор абстрактного метода
    def get_items(self):  # метод get_items() - возвращает содержание склада в словаре {товар: количество}
        pass

    @abstractmethod  # декоратор абстрактного метода
    def get_unique_items_count(self):  # метод get_unique_items_count() - возвращает количество уникальных товаров
        pass
