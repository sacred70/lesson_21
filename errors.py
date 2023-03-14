class NotEnoughSpase(BaseException):
    message = 'Нет места на складе!\n'


class NotProduct(BaseException):
    message = 'Нет данного товара!\n'


class NotQuantityProduct(BaseException):
    message = 'Недостаточное количество товара!\n'


class ShopFull(BaseException):
    message = 'Магазин полон товара!\n'


class BadInput(BaseException):
    message = 'Не верный запрос!\n'


class BadStorageName(BaseException):
    message = 'Указан не верный склад отправления или получения!\n'

