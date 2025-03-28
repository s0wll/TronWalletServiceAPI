from src.schemas.wallet_info import WalletResponse


async def test_create_wallet_info(db):
    wallet_info_data = WalletResponse(
        account_name="test_account_name",
        address="test_address",
        bandwidth=100,
        energy=100,
        balance=100.9,
    )
    # Добавление данных в БД
    await db.wallet_info.create_wallet_info(wallet_info_data)
    await db.commit()

    # Получение этих данных, чтобы удостовериться, что они есть в БД
    wallet_info_list = await db.wallet_info.get_wallet_info_list(limit=5, offset=1)
    assert wallet_info_list
    assert isinstance(wallet_info_list, list)
    assert len(wallet_info_list) > 0
