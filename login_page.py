class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button", name="Login")
        self.error = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(self.URL)

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()