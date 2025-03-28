from fastapi import HTTPException


# BaseExceptions
class TronWalletServiceException(Exception):
    detail = "Неожиданная ошибка"

    def __init__(self, *args, **kwargs):
        super().__init__(self.detail, *args, **kwargs)


class ObjectNotFoundException(TronWalletServiceException):
    detail = "Объект не найден"


class WalletInfoNotFoundException(ObjectNotFoundException):
    detail = "Информация о кошельке не найдена"


# HTTPExceptions
class TronWalletServiceHTTPException(HTTPException):
    status_code = 500
    detail = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class WalletInfoNotFoundHTTPException(TronWalletServiceHTTPException):
    status_code = 404
    detail = "Информация о кошельке не найдена"
