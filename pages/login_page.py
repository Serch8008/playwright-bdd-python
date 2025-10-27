# pages/login_page.py
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.products_title = page.locator(".title")
        self.error = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(self.base_url)

    def login(self, user, password):
        self.username.fill(user)
        self.password.fill(password)
        self.login_button.click()

    def assert_logged_in(self):
        expect(self.products_title).to_have_text("Products")


    def assert_error(self, contains_text: str):
        from playwright.sync_api import expect
        expect(self.error).to_contain_text(contains_text)