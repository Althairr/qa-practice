from playwright.sync_api import Page, expect

BASE = "https://the-internet.herokuapp.com"

def test_dropdown(page: Page):
    page.goto(f"{BASE}/dropdown")
    page.select_option("#dropdown", "2")            # pilih by value
    expect(page.locator("#dropdown")).to_have_value("2")

def test_checkbox(page: Page):
    page.goto(f"{BASE}/checkboxes")
    cb = page.locator("input[type='checkbox']").first
    cb.check()
    expect(cb).to_be_checked()
    cb.uncheck()
    expect(cb).not_to_be_checked()

def test_js_alert(page: Page):
    page.goto(f"{BASE}/javascript_alerts")
    page.once("dialog", lambda d: d.accept())       # pasang handler SEBELUM klik
    page.get_by_role("button", name="Click for JS Alert").click()
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")

def test_js_confirm_dismiss(page: Page):
    page.goto(f"{BASE}/javascript_alerts")
    page.once("dialog", lambda d: d.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")

def test_js_prompt(page: Page):
    page.goto(f"{BASE}/javascript_alerts")
    page.once("dialog", lambda d: d.accept("halo QA"))
    page.get_by_role("button", name="Click for JS Prompt").click()
    expect(page.locator("#result")).to_have_text("You entered: halo QA")

def test_iframe(page: Page):
    page.goto(f"{BASE}/iframe")
    frame = page.frame_locator("#mce_0_ifr")
    editor = frame.locator("#tinymce")
    editor.fill("Teks dari Playwright")
    expect(editor).to_have_text("Teks dari Playwright")

def test_dynamic_loading(page: Page):
    page.goto(f"{BASE}/dynamic_loading/1")
    page.get_by_role("button", name="Start").click()
    # auto-wait: tidak perlu sleep
    expect(page.locator("#finish")).to_have_text("Hello World!", timeout=10000)

def test_new_tab(page: Page):
    page.goto(f"{BASE}/windows")
    with page.context.expect_page() as new_page_info:
        page.get_by_role("link", name="Click Here").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page.locator("h3")).to_have_text("New Window")

def test_file_upload(page: Page, tmp_path):
    f = tmp_path / "contoh.txt"
    f.write_text("isi file")
    page.goto(f"{BASE}/upload")
    page.set_input_files("#file-upload", str(f))