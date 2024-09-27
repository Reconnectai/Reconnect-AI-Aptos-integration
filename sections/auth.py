import datetime

import jwt

from config import settings
from dto import TokenData


def generate_jwt(
        address: str,
        algorithm: str = 'HS256',
        expiration_minutes: int = 60,
) -> str:
    """
    Generates a JWT token.

    :param address: User Aptos address to be included in the token.
    :param algorithm: Signing algorithm (default is HS256).
    :param expiration_minutes: Token expiration time in minutes.
    :return: JWT token as a string.
    """
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=expiration_minutes)
    payload = TokenData(
        address=address,
        exp=expiration_time,
    )
    return jwt.encode(payload.dict(), settings.SECRET_KEY, algorithm=algorithm)


def verify_jwt(token: str, algorithm: str = 'HS256') -> TokenData:
    """
    Verifies a JWT token.

    :param token: JWT token to verify.
    :param algorithm: Signing algorithms to use for verification.
    :return: Decoded data from the token if verification is successful.
    :raises: jwt.ExpiredSignatureError, jwt.InvalidTokenError
    """
    decoded_payload = jwt.decode(
        token, settings.SECRET_KEY, algorithms=[algorithm])
    return TokenData(**decoded_payload)
