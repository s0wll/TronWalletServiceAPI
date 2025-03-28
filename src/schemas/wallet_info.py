from pydantic import BaseModel


class WalletRequest(BaseModel):
    address: str


class WalletResponse(BaseModel):
    account_name: str | None = None
    address: str
    bandwidth: int
    energy: int
    balance: float


class Wallet(WalletResponse):
    id: int