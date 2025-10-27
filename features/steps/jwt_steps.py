from behave import given, when, then
from jwt_utils import generar_token_hs256, validar_token_hs256

@given('un payload con "sub"="{sub}" y "role"="{role}"')
def step_payload(context, sub, role):
    context.payload = {"sub": sub, "role": role}

@when('genero un token HS256 con expiracion de {secs:d}')
def step_generate(context, secs):
    context.token = generar_token_hs256(context.payload, exp_seconds=secs)

@then('validar el token debe devolver "{sub}"')
def step_validate(context, sub):
    payload = validar_token_hs256(context.token)
    assert payload["sub"] == sub
