from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_saucedemo_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login = LoginPage(page)
        login.open()
        login.login("standard_user", "secret_sauce")
        assert "inventory" in page.url
        browser.close()

def test_login_locked_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login = LoginPage(page)
        login.open()
        login.login("locked_out_user", "secret_sauce")
        assert "Sorry, this user has been locked out" in page.content()
        browser.close()

