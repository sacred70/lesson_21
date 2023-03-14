class NotEnoughSpase(BaseException):
    message = 'Нет места на складе!\n'


class NotProduct(BaseException):
    message = 'Нет данного товара!\n'


class NotQuantityProduct(BaseException):
    message = 'Недостаточное количество товара!\n'
