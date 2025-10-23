"""
FastAPI depnendencies for login functionality.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel

from auth import JWTAuth
from db_mongo.register_and_login import get_login_user

#Security scheme for HTTP Bearer authentication
security = HTTPBearer()

# Initialize JWTAuth with your secret key and algorithm
SECRET_KEY = "mySecretKey123" # change this in production
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 5 # Token expiry time in minutes ( configurable )

jwt_auth = JWTAuth(secret_key=SECRET_KEY, alg=ALGORITHM, token_expiry_minutes=TOKEN_EXPIRE_MINUTES)

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """
    Dependency to get the current user from the JWT token.

    - **credentials**: HTTPAuthorizationCredentials provided by the HTTPBearer scheme.

    Returns the user information if the token is valid.

    Raises HTTPException if the token is invalid or expired.
    """
    token = credentials.credentials
    payload = jwt_auth.verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Get user from database or any other source
    user = get_login_user(user_id=payload.get("sub"))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user