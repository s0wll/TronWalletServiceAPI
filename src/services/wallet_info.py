from tronpy import Tron
import requests

from src.schemas.wallet_info import Wallet, WalletRequest, WalletResponse
from src.utils.db_manager import DBManager


class WalletInfoService:
    db: DBManager

    def __init__(self, db: DBManager) -> None:
        self.db = db

    async def get_wallet_info_tron(self, address: str) -> WalletResponse:
        # Получение некоторых данных кошелька при помощи tronpy
        tron = Tron()
        account = tron.get_account(address)
        account_name = account.get("account_name", None)
        bandwidth = tron.get_bandwidth(address)
        balance = tron.get_account_balance(address)

        # Получение некоторых данных при помощи альтернативного способа с применением requests
        url = f"https://api.tronscan.org/api/account?address={address}"
        response = requests.get(url)

        if response.status_code == 200:
            account_info = response.json()
            energy = account_info["bandwidth"]["energyRemaining"]
        else:
            print(f"Ошибка при получении данных: {response.status_code}")
            return None

        return WalletResponse(
            account_name=account_name,
            address=address,
            bandwidth=bandwidth,
            energy=energy,
            balance=balance
        )

    async def create_wallet_info(self, wallet_request: WalletRequest) -> Wallet:
        wallet_info_tron = await self.get_wallet_info_tron(wallet_request.address)
        new_wallet_info = await self.db.wallet_info.create_wallet_info(wallet_info_tron)
        await self.db.commit()
        return new_wallet_info
    
    async def get_wallet_info_list(self, pagination) -> list[Wallet]:
        per_page = pagination.per_page or 5
        return await self.db.wallet_info.get_wallet_info_list(
            limit=per_page,
            offset=per_page * (pagination.page - 1)
        )