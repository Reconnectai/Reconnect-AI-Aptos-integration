from datetime import datetime

from pydantic import BaseModel


class AuthRequest(BaseModel):
    public_key: str
    full_message: str
    signature: str


class TransactionInfo(BaseModel):
    transaction_hash: str
    sender_wallet: str


class TokenData(BaseModel):
    address: str
    exp: datetime
