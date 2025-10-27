import os
import jwt
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional, Tuple
from dotenv import load_dotenv

load_dotenv()
DEFAULT_ALG = "HS256"

def _secret() -> str:
    secret = os.getenv("SECRET_KEY")
    if not secret:
        # para entorno de demo, pero en prod debes forzar .env
        secret = "dev-secret-change-me"
    return secret

def generar_token_hs256(payload: Dict[str, Any], exp_seconds: int = 300) -> str:
    """
    Genera un JWT HS256 con expiración (exp).
    """
    to_encode = payload.copy()
    to_encode["exp"] = datetime.now(tz=timezone.utc) + timedelta(seconds=exp_seconds)
    token = jwt.encode(to_encode, _secret(), algorithm=DEFAULT_ALG)
    # PyJWT>=2 retorna str (no bytes) para HS256
    return token

def validar_token_hs256(token: str) -> Dict[str, Any]:
    """
    Valida y decodifica un JWT HS256. Si es inválido, PROPAGA la excepción específica.
    """
    decoded = jwt.decode(token, _secret(), algorithms=[DEFAULT_ALG])
    return decoded

def validar_token_seguro(token: str) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
    """
    Wrapper seguro que NO lanza excepción. Devuelve (ok, payload, error_msg).
    """
    try:
        payload = validar_token_hs256(token)
        return True, payload, None
    except jwt.ExpiredSignatureError:
        return False, None, "Token expirado"
    except jwt.InvalidTokenError as e:
        return False, None, f"Token inválido: {e}"
