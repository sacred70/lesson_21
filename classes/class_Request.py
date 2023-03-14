"""
Шаг 4. Создайте класс Request в котором будет храниться запрос.
"""
from classes.base_class import Base
from errors import BadInput
from errors import BadStorageName


class Request:
    def __init__(self, request: str, storages: dict[str, Base]):
        """
        Создаем класс реквест для чтения полученного запроса от пользователя
        """
        parsed_request = request.lower().split(' ')  # делим запрос по пробелам
        if len(parsed_request) != 7:
            raise BadInput
        """
        Если в запросе не 7 слов, выдаем ошибку о неправильном запросе
        """
        self.amount = int(parsed_request[1])  # выводим из запроса количество товара(преобразовываем в число)
        self.product = parsed_request[2]  # выводим из запроса наименование товара
        self.departure = parsed_request[4]  # выводим из запроса откуда перемещаем товар товара
        self.destination = parsed_request[6]  # выводим из запроса куда перемещаем товар товара

        if self.departure not in storages or self.destination not in storages:
            raise BadStorageName
        """
        Если вида склада от откуда перемещаем нет в списках складов или 
        вида склада от куда перемещаем нет в списках складов, выводим ошибку о неверном складе
        """
