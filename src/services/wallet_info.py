from tronpy import Tron

from src.schemas.wallet_info import Wallet, WalletRequest, WalletResponse
from src.utils.db_manager import DBManager


class WalletInfoService:
    db: DBManager

    def __init__(self, db: DBManager) -> None:
        self.db = db

    async def get_wallet_info_tron(self, address: str) -> WalletResponse:
        tron = Tron()
        account = tron.get_account(address)
        print(account)

        bandwidth = account.get("bandwidth", 0)  # Если ключ отсутствует, вернется 0
        energy = account.get("energy", 0)        # Аналогично для energy
        balance = account.get("balance", 0) / 1_000_000

        return WalletResponse(
            address=address,
            bandwidth=bandwidth,
            energy=energy,
            balance=balance
        )

    async def create_wallet_info(self, wallet_request: WalletRequest) -> Wallet:
        wallet_info = await self.get_wallet_info_tron(wallet_request.address)
        await self.db.wallet_info.create_wallet_info(wallet_info)
        await self.db.commit()
        return wallet_info
    
    async def get_wallet_info_list(self, pagination) -> list[Wallet]:
        per_page = pagination.per_page or 5
        return await self.db.wallet_info.get_wallet_info_list(
            limit=per_page,
            offset=per_page * (pagination.page - 1)
        )