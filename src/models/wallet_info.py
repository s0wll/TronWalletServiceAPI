from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class WalletInfoORM(Base):
    __tablename__ = "wallet_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_name: Mapped[str | None]
    address: Mapped[str]
    bandwidth: Mapped[int]
    energy: Mapped[int]
    balance: Mapped[float]