from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class WalletInfoORM(Base):
    __tablename__ = "wallet_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str]
    bandwidth: Mapped[float]
    energy: Mapped[float]
    balance: Mapped[float]