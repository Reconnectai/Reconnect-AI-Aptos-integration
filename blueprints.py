import jwt
from fastapi import APIRouter, Body, HTTPException
from starlette.responses import JSONResponse

from config import settings
from dto import AuthRequest, TokenData, TransactionInfo
from sections import aptos, auth

router = APIRouter()


@router.post('/')
async def get_token(request: AuthRequest):
    if address := await aptos.verify(request):
        return auth.generate_jwt(address)
    # TODO: graceful exit
    raise Exception()


@router.post('/transaction')
async def check_transaction(request: TransactionInfo):
    try:
        aptos_client = settings.aptos_client
        txn = await aptos_client.transaction_by_hash(request.transaction_hash)

        if not txn or 'success' not in txn or not txn['success']:
            raise HTTPException(
                status_code=400, detail="Transaction not found or failed")

        if txn['sender'] != request.sender_wallet:
            raise HTTPException(
                status_code=400, detail="Sender wallet does not match")

        payload = txn['payload']
        if payload['function'] != '0x1::coin::transfer':
            raise HTTPException(
                status_code=400, detail="Not a transfer transaction")
        recipient = payload['arguments'][0]
        amount = payload['arguments'][1]
        if recipient != settings.RECONNECT_WALLET:
            raise HTTPException(
                status_code=400, detail="Recipient wallet does not match")
        return {'amount': int(amount) * 10 ** -8}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/verification', response_model=TokenData)
def verify_token(token: str = Body()):
    try:
        return auth.verify_jwt(token)
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError) as e:
        return JSONResponse(status_code=401, content={'msg': str(e)})
