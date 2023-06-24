
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBearer, HTTPAuthorizationCredentials
# from jose import JWTError, jwt
# from passlib.context import CryptContext
import os
from dotenv import load_dotenv
from models import User

security = HTTPBearer()
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
load_dotenv()

DATA = os.environ.get("DATA")
JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
JWT_TOKEN_DURATION = os.environ.get("JWT_TOKEN_DURATION")
# encoded_jwt = jwt.encode({DATA}, JWT_SECRET, algorithm=JWT_ALGORITHM)
# print(encoded_jwt)
# jwt.decode(encoded_jwt, JWT_SECRET, algorithms=JWT_ALGORITHM)


def encode_token(token: str):
    payload = jwt.encode({"user": token},JWT_SECRET, algorithm=JWT_ALGORITHM)
    return payload


def verify_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return payload
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):

    if credentials.scheme != "Bearer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid authentication scheme")
    if credentials.credentials is None:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication ")

    return verify_token(credentials.credentials)
