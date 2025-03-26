from sqlalchemy import insert, select

from src.schemas.wallet_info import Wallet, WalletResponse
from src.models.wallet_info import WalletInfoORM


class WalletInfoCRUD:
    model = WalletInfoORM
    schema = Wallet

    def __init__(self, session) -> None:
        self.session = session

    async def create_wallet_info(self, wallet_info: WalletResponse) -> Wallet:
        create_stmt = insert(WalletInfoORM).values(**wallet_info.model_dump()).returning(WalletInfoORM)
        result = await self.session.execute(create_stmt)
        model = self.schema.model_validate(result.scalars().one(), from_attributes=True)
        return model

    async def get_wallet_info_list(self, limit: int, offset: int) -> list[Wallet]:
        query = select(WalletInfoORM).limit(limit).offset(offset)
        result = await self.session.execute(query)
        models = [Wallet.model_validate(one, from_attributes=True) for one in result.scalars().all()]
        return models
