from playwright.sync_api import Page, expect

def test_login_and_add_to_cart(page: Page):
    page.goto("https://www.saucedemo.com")

    # Login
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # Tambah ke keranjang
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1") # pastiin ui berubah jadi nambah 1

    # check cart
    page.locator("[data-test='shopping-cart-link']").click()

    # checkout
    page.locator("[data-test='checkout']").click()

    # Isi form checkout
    page.locator("[data-test='firstName']").fill("John")
    page.locator("[data-test='lastName']").fill("Doe") 
    page.locator("[data-test='postalCode']").fill("12345") 

    # click continue
    page.locator("[data-test='continue']").click()

    # click finish
    page.locator("[data-test='finish']").click()
      
    # Screenshot
    page.screenshot(path="cart.png")