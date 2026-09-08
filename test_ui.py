from playwright.sync_api import sync_playwright

def test_saucedemo_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/", timeout=15000)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        assert "inventory" in page.url, f"не залогинились, url {page.url}"
        print("URL после логина:", page.url)
        browser.close()
        