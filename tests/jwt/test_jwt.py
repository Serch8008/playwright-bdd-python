import jwt
from jwt_utils import generar_token_hs256, validar_token_seguro

def test_token_invalido_InvalidTokenError():
    token = generar_token_hs256({"sub": "sergio"}, exp_seconds=60)

    # Romper SIEMPRE la firma alterando el SEGMENTO DEL PAYLOAD (segundo).
    header, payload, signature = token.split(".")
    # flip de un carácter del payload para que cambie el contenido firmado
    flip_char = "A" if payload[-1] != "A" else "B"
    payload_tampered = payload[:-1] + flip_char
    token_invalido = ".".join([header, payload_tampered, signature])

    ok, payload_decoded, err = validar_token_seguro(token_invalido)
    assert ok is False
    assert payload_decoded is None
    assert "inválido" in err.lower() or "signature" in err.lower()
