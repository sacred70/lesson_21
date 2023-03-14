from classes.class_Shop import Shop
from classes.class_Store import Store
from classes.class_Request import Request
from errors import BadInput



store = Store(
    items={
        "печеньки": 25,
        "собачки": 25,
        "елки": 25,
        "пончик": 3,
        "зонт": 5,
        "ноутбук": 1})
"""
Создаем экземпляр класса Store со словарем товаров (наличие на складе)
"""
shop = Shop(
    items={
        "печеньки": 2,
        "собачки": 2,
        "елки": 2,
        "пончик": 1,
        "зонт": 1})
"""
Создаем экземпляр класса Shop со словарем товаров (наличие в магазине)
"""

storages = \
    {
        "склада": store,
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
            "Введите запрос в формате: 'Доставить 3 печеньки со склада в магазин'\n"
            "Введите 'стоп' 'stop' или если хотите закончить\n"
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
            continue
        """
        Если запрос верный создаем экземпляр класса реквест с запросом пользователя и словарем складов
        в случае ошибки выдаем сообщение о неверном запросе и перезапускаем цикл 
        """
        try:
            storages[request.departure].remove(request.product, request.amount)

            print(f'Курьер забрал {request.amount} {request.product} из {request.departure}')
        except:
            print("Ошибка доставки")
        """
        Если запрос верный создаем экземпляр класса реквест с запросом пользователя и словарем складов
        в случае ошибки выдаем сообщение о неверном запросе и перезапускаем цикл 
        """



if __name__ == '__main__':
    main()
