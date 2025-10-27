# features/environment.py
import os, pathlib, time
from playwright.sync_api import sync_playwright

REPORTS = pathlib.Path("reports")
REPORTS.mkdir(parents=True, exist_ok=True)

def before_all(context):
    context.playwright = sync_playwright().start()
    browser = os.getenv("BROWSER", "chromium").lower()
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    if browser == "chromium":
        channel = os.getenv("CHROME_CHANNEL", "chrome")
        context.browser = context.playwright.chromium.launch(
            headless=headless, channel=channel
        )
    elif browser == "firefox":
        context.browser = context.playwright.firefox.launch(headless=headless)
    else:
        context.browser = context.playwright.webkit.launch(headless=headless)

def after_all(context):
    context.browser.close()
    context.playwright.stop()

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    # carpeta por escenario
    safe_name = scenario.name.replace(" ", "_").replace("/", "_")
    context.scenario_dir = REPORTS / safe_name
    context.scenario_dir.mkdir(parents=True, exist_ok=True)
    # start tracing
    context.browser.contexts[0].tracing.start(screenshots=True, snapshots=True, sources=True)

def after_scenario(context, scenario):
    # stop tracing y guardar
    trace_path = context.scenario_dir / "trace.zip"
    try:
        context.browser.contexts[0].tracing.stop(path=str(trace_path))
    except Exception:
        pass

    # screenshot al fallar
    if scenario.status == "failed":
        ts = time.strftime("%Y%m%d-%H%M%S")
        fail_png = context.scenario_dir / f"failed-{ts}.png"
        try:
            context.page.screenshot(path=str(fail_png), full_page=True)
        except Exception:
            pass

    if getattr(context, "page", None):
        context.page.close()
