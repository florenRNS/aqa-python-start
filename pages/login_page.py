class LoginPage:
    URL = "https://www.saucedemo.com/"
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"

    def __init__(self, page):
         self.page = page

    def open(self):
         self.page.goto(self.URL, timeout=15000)

    def login(self, username, password):
         self.page.fill(self.USERNAME, username)
         self.page.fill(self.PASSWORD, password)
         self.page.click(self.LOGIN_BTN)
