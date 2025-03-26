from fastapi import APIRouter, Body, Query

from src.services.wallet_info import WalletInfoService
from src.schemas.wallet_info import WalletRequest
from src.api.dependencies import DBDep, PaginationDep


router = APIRouter(prefix="/wallet_info", tags=["WalletInfo"])


@router.post("")
async def create_wallet_info(db: DBDep, wallet_request: WalletRequest):
    wallet_info = await WalletInfoService(db).create_wallet_info(wallet_request)
    return {"status": "OK", "data": wallet_info}


@router.get("")
async def get_wallet_info_list(db: DBDep, pagination: PaginationDep):
    wallet_info_list = await WalletInfoService(db).get_wallet_info_list(pagination=pagination)
    return wallet_info_list