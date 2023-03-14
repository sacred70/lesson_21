from classes.class_Shop import Shop
from classes.class_Store import Store
from classes.class_Request import Request
from errors import BadInput


store = Store(
    items={
        "печенька": 25,
        "собачка": 25,
        "елка": 25,
        "пончик": 3,
        "зонт": 5,
        "ноутбук": 1})
"""
Создаем экземпляр класса Store со словарем товаров (наличие на складе)
"""
shop = Shop(
    items={
        "печенька": 2,
        "собачка": 2,
        "елка": 2,
        "пончик": 1,
        "зонт": 1})
"""
Создаем экземпляр класса Shop со словарем товаров (наличие в магазине)
"""

storages = \
    {
        "склад": store,
        "магазин": shop
    }
"""
Словарь с списком сладов 
"""


def main():
    print("\nДобрый день\n")
    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')
        """
        Перебираем склады и выводим наименование товаров и их количество на складах
        """
        user_input = input(
            "Введите запрос в формате: 'Доставить 3 печеньки со склада в магазин'"
            "Введите 'стоп' 'stop' или если хотите закончить"
        )
        """
        Просим пользователя ввести запрос или закончить 
        """
        if user_input in ('стоп', 'stop'):
            break
        """
        Проверяем на совпадение со стоп-словами и останавливаем если пользователь решил закончить
        """
        try:
            request = Request(request=user_input, storages=storages)
        except BadInput:
            print(BadInput.message)
        """
        Если запрос верный создаем экземпляр класса реквест с запросом пользователя и словарем складов
        в случае ошибки выдаем сообщение о неверном запросе
        """

if __name__ == '__main__':
    main()
