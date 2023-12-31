#Steps to do in terminal :
#cd ..
#pip3 install playwright
#playwright install chromium
#playwright codegen
#two win will pop up

#paste random url and click few fields
#changes will be converted into code in the recorder
#stop the recorder
#copy code in editor
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin")
    page.get_by_text("Welcome, please sign in!").click()
    page.get_by_text("Email: Password: Remember me?").click()
    page.locator("form div").filter(has_text="Email:").nth(1).click()
    page.get_by_label("Email:").click()
    page.get_by_text("Password:", exact=True).click()
    page.get_by_label("Password:").click()
    page.get_by_text("Remember me?").click()
    page.get_by_label("Remember me?").uncheck()
    page.get_by_role("button", name="Log in").click()
    page.get_by_role("link", name=" Promotions ").click()
    page.get_by_role("link", name=" Discounts").click()
    page.wait_for_load_state("Networkidle")
    page.get_by_role("link", name=" Add new").click()
    page.get_by_label("Name").click()
    page.get_by_label("Name").fill("500")
    page.get_by_label("Name").press("CapsLock")
    page.get_by_label("Name").fill("25OFF")
    page.get_by_label("Use percentage").check()
    page.get_by_role("spinbutton", name="0.0000").click()
    page.get_by_label("Discount percentage").fill("50")
    page.get_by_label("Name").click()
    page.get_by_label("Name").click()
    page.get_by_label("Name").fill("20OFF")
    page.get_by_label("Requires coupon code").check()
    page.get_by_label("Coupon code", exact=True).click()
    page.get_by_label("Coupon code", exact=True).fill("20OFF")
    page.get_by_role("button", name=" Save", exact=True).click()
    
    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

#run
