from classes.class_Shop import Shop
from classes.class_Store import Store


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
    with True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')
        """
        Перебираем склады и выводим наименование товаров и их количество на складах
        """



if __name__ == '__main__':
    main()