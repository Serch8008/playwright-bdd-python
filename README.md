## Cómo correr
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install

# Local (Chrome del sistema)
export BROWSER=chromium
export CHROME_CHANNEL=chrome
export HEADLESS=true
behave

# Ver traza
playwright show-trace reports/<Escenario>/trace.zip
