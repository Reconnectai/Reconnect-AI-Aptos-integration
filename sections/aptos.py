from aptos_sdk import ed25519
from aptos_sdk.account_address import AccountAddress
from aptos_sdk.authenticator import Ed25519Authenticator
from nacl.signing import VerifyKey

from config import settings
from dto import AuthRequest


async def verify(request: AuthRequest) -> str | None:
    public_key_bytes = bytes.fromhex(request.public_key[2:])
    public_key = ed25519.PublicKey(VerifyKey(public_key_bytes))

    account = await settings.aptos_client.account(
        AccountAddress.from_key(public_key))

    signature_bytes = bytes.fromhex(request.signature)
    signature = ed25519.Signature(signature_bytes)

    auth = Ed25519Authenticator(public_key, signature)
    if auth.verify(request.full_message.encode('utf-8')):
        return account['authentication_key']
