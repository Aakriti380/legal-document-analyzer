from jose import jwt
from datetime import datetime, timedelta
from config.settings import (
    JWT_SECRET,
    JWT_ALGORITHM
)

def create_access_token(data: dict):

    payload = data.copy()

    expire = datetime.utcnow() + timedelta(days=7)

    payload.update({
        "exp": expire
    })

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )