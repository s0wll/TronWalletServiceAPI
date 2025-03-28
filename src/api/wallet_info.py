import logging

from fastapi import APIRouter

from src.exceptions import WalletInfoNotFoundException, WalletInfoNotFoundHTTPException
from src.services.wallet_info import WalletInfoService
from src.schemas.wallet_info import WalletRequest
from src.api.dependencies import DBDep, PaginationDep


router = APIRouter(prefix="/wallet_info", tags=["WalletInfo"])


@router.post("")
async def create_wallet_info(db: DBDep, wallet_request: WalletRequest):
    logging.info("Добавление новой информации о кошельке /create_wallet_info")
    wallet_info = await WalletInfoService(db).create_wallet_info(wallet_request)
    logging.info("Успешное добавление информации о кошельке")
    return {"status": "OK", "data": wallet_info}


@router.get("")
async def get_wallet_info_list(db: DBDep, pagination: PaginationDep):
    try:
        logging.info("Получение списка информации о кошельках /get_wallet_info_list")
        wallet_info_list = await WalletInfoService(db).get_wallet_info_list(pagination=pagination)
        logging.info("Успешное получение списка информации о кошельках")
        return wallet_info_list
    except WalletInfoNotFoundException:
        logging.error("Ошибка получения списка информации о кошельках")
        raise WalletInfoNotFoundHTTPException
