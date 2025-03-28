import requests

from tronpy import Tron
from tronpy.providers import HTTPProvider

from src.exceptions import ObjectNotFoundException, WalletInfoNotFoundException
from src.schemas.wallet_info import Wallet, WalletRequest, WalletResponse
from src.utils.db_manager import DBManager


class WalletInfoService:
    db: DBManager
    api_keys = [
        "f0ebfa71-17d0-4c33-9582-47592527ef0e",
        "bc1c8478-816c-45ad-be86-0413bedc817c",
        "a23d34a3-07e8-4b54-b739-1c198c12f957",
    ]

    def __init__(self, db: DBManager) -> None:
        self.db = db

    async def get_wallet_info_tron(self, address: str) -> WalletResponse:
        # Получение некоторых данных кошелька при помощи tronpy
        # Из-за специфики API Tron, нам нужно инициализировать Tron() с ключами API, чтобы не получать ошибку 401
        provider = HTTPProvider("https://api.trongrid.io", api_key=self.api_keys)
        tron = Tron(provider=provider)
        account = tron.get_account(address)
        account_name = account.get("account_name", None)
        bandwidth = tron.get_bandwidth(address)
        balance = tron.get_account_balance(address)

        # Получение некоторых данных при помощи альтернативного способа с применением requests
        url = f"https://api.tronscan.org/api/account?address={address}"
        response = requests.get(url)
        account_info = response.json()
        energy = account_info["bandwidth"]["energyRemaining"]

        return WalletResponse(
            account_name=account_name,
            address=address,
            bandwidth=bandwidth,
            energy=energy,
            balance=balance,
        )

    async def create_wallet_info(self, wallet_request: WalletRequest) -> Wallet:
        wallet_info_tron = await self.get_wallet_info_tron(wallet_request.address)
        new_wallet_info = await self.db.wallet_info.create_wallet_info(wallet_info_tron)
        await self.db.commit()
        return new_wallet_info

    async def get_wallet_info_list(self, pagination) -> list[Wallet]:
        per_page = pagination.per_page or 5
        try:
            return await self.db.wallet_info.get_wallet_info_list(
                limit=per_page, offset=per_page * (pagination.page - 1)
            )
        except ObjectNotFoundException:
            raise WalletInfoNotFoundException
