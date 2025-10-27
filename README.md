## Descripción del Proyecto

Framework unificado de automatización que combina:
🧩 Playwright para pruebas UI multiplataforma.
💬 Behave (BDD + Gherkin) para escenarios legibles por negocio.
🔗 Requests para pruebas de API reales y mockeadas.
🔐 JWT / PyJWT para autenticación y validación de tokens.
⚙️ CI/CD con GitHub Actions para ejecución continua en 3 navegadores y pytest.

## Estructura del Proyecto

playwright-bdd-python/
├── api_client.py
├── jwt_utils.py
├── features/
│   ├── login.feature
│   ├── api.feature
│   ├── jwt.feature
│   └── steps/
│       ├── login_steps.py
│       ├── api_steps.py
│       └── jwt_steps.py
├── pages/
│   └── login_page.py
├── tests/
│   ├── api/test_public_api.py
│   ├── unit/test_api_client_mock.py
│   └── jwt/test_jwt.py
├── .github/workflows/
│   ├── ci-bdd.yml
│   └── pytest.yml
├── requirements.txt
├── .env.example
└── README.md

## Ejecución Local
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install

## Ejecución de Tests
## Pruebas BDD (Behave)
export PYTHONPATH=.
export BROWSER=chromium
export CHROME_CHANNEL=chrome
export HEADLESS=true
behave

## Pruebas Pytest (API y JWT)
pytest -q

## Pruebas Mockeadas
pytest tests/unit/test_api_client_mock.py -v

# Ver traza
playwright show-trace reports/<Escenario>/trace.zip

## JWT / Cripto (PyJWT HS256)
# Archivo: jwt_utils.py
# Genera y valida tokens JWT HS256
# Maneja ExpiredSignatureError e InvalidTokenError

## CI/CD con GitHub Actions

## BDD Workflow (ci-bdd.yml)

# Instala dependencias
# Corre pruebas Behave en los 3 navegadores
# Sube reportes como artefactos

## Pytest Workflow (pytest.yml)

# Corre unit tests (API + JWT)
# Falla rápido (--maxfail=1)
# Incluye SECRET_KEY para JWT