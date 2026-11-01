import pytest
from playwright.sync_api import Page, expect
from login_page import LoginPage
from inventory_page import InventoryPage
from checkout_page import CheckoutPage

def test_full_purchase(page: Page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    checkout = CheckoutPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    inventory.add_backpack()
    expect(inventory.cart_badge).to_have_text("1")

    inventory.open_cart()
    checkout.fill_info("Althair", "Test", "15111")
    checkout.finish()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")

@pytest.mark.parametrize("user,pwd,pesan", [
    ("standard_user", "salah", "do not match"),
    ("locked_out_user", "secret_sauce", "locked out"),
    ("", "", "Username is required"),
])
def test_login_negative(page: Page, user, pwd, pesan):
    login = LoginPage(page)
    login.open()
    login.login(user, pwd)
    expect(login.error).to_contain_text(pesan)