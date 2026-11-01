class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.checkout_btn = page.locator("[data-test='checkout']")
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal = page.locator("[data-test='postalCode']")
        self.continue_btn = page.locator("[data-test='continue']")
        self.finish_btn = page.locator("[data-test='finish']")
        self.complete_header = page.locator("[data-test='complete-header']")

    def fill_info(self, first, last, postal):
        self.checkout_btn.click()
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal.fill(postal)
        self.continue_btn.click()

    def finish(self):
        self.finish_btn.click()