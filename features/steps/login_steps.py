# features/steps/login_steps.py
from behave import given, when, then
from pages.login_page import LoginPage
import os

@given("que el usuario abre la página de inicio")
def step_open_home(context):
    base_url = os.getenv("BASE_URL", "https://www.saucedemo.com")
    context.login_page = LoginPage(context.page, base_url)
    context.login_page.open()

@when('ingresa las credenciales "{user}" y "{password}"')
def step_login(context, user, password):
    context.login_page.login(user, password)

@then("debería ver la página de productos")
def step_verify_login(context):
    context.login_page.assert_logged_in()
    
@then('debería ver el mensaje de error "{msg}"')
def step_error_msg(context, msg):
    context.login_page.assert_error(msg)
