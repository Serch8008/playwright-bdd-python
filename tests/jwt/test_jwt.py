import jwt
from datetime import datetime, timedelta, timezone
from jwt_utils import generar_token_hs256, validar_token_hs256, validar_token_seguro

def test_generar_y_validar_token_ok():
    token = generar_token_hs256({"sub": "sergio", "role": "qa"}, exp_seconds=60)
    payload = validar_token_hs256(token)
    assert payload["sub"] == "sergio"
    assert payload["role"] == "qa"
    assert "exp" in payload

def test_token_expirado_ExpiredSignatureError():
    # exp en el pasado: forzamos expiración sin sleep
    token = generar_token_hs256({"sub": "sergio"}, exp_seconds=-1)
    try:
        validar_token_hs256(token)
        assert False, "Debió lanzar ExpiredSignatureError"
    except jwt.ExpiredSignatureError:
        pass  # OK

def test_token_invalido_InvalidTokenError():
    # token manipulado
    token = generar_token_hs256({"sub": "sergio"}, exp_seconds=60)
    # alteramos una letra para romper la firma
    token_invalido = token[:-1] + ("a" if token[-1] != "a" else "b")
    ok, payload, err = validar_token_seguro(token_invalido)
    assert ok is False
    assert payload is None
    assert "inválido" in err.lower()
