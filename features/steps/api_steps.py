import json
from behave import given, when, then
from api_client import ApiClient
from behave import then

@given('un api cliente con base "{base}"')
def step_client_base(context, base):
    context.client = ApiClient(base)

@when('hago GET a "{path}"')
def step_get(context, path):
    context.response = context.client.get(path)

@when('hago POST a "{path}" con json:')
def step_post(context, path):
    payload = json.loads(context.text)
    context.response = context.client.post(path, json=payload)

@then("el status code debe ser 200")
def step_status_200(context):
    assert context.response.status_code == 200

@then("el status code debe ser 201 o 200")
def step_status_201_or_200(context):
    assert context.response.status_code in (200, 201)

@then('el header "{name}" debe incluir "{value}"')
def step_header_contains(context, name, value):
    headers = {k.lower(): v for k, v in context.response.headers.items()}
    assert name.lower() in headers
    assert value.lower() in headers[name.lower()].lower()

@then("el body debe ser una lista con al menos 1 elemento")
def step_body_list(context):
    data = context.response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

@then('el primer elemento debe tener las llaves "{keys_csv}"')
def step_keys(context, keys_csv):
    expected = [k.strip() for k in keys_csv.split(",")]
    first = context.response.json()[0]
    for k in expected:
        assert k in first

@then('el body debe tener la llave "{key}"')
def step_body_has_key(context, key):
    data = context.response.json()
    # Para POST /posts el body es un dict (no una lista)
    assert isinstance(data, dict), f"Se esperaba dict, llegó: {type(data)}"
    assert key in data, f'No se encontró la llave "{key}" en {data}'
