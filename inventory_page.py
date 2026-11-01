class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def add_backpack(self):
        self.page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    def open_cart(self):
        self.cart_link.click()