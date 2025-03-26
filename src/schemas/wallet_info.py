from pydantic import BaseModel

class WalletRequest(BaseModel):
    address: str

class WalletResponse(BaseModel):
    id: int
    address: str
    bandwidth: float
    energy: float
    balance: float
