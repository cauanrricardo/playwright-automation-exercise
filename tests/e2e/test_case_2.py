from playwright.sync_api import Page, expect

def test_login_with_email_password(page : Page, navigate_to_home, user_email, user_password) :
#   1. Launch browser

#2. Navigate to url 'http://automationexercise.com'

#3. Verify that home page is visible successfully
    expect(page).to_have_url("https://automationexercise.com/")
#4. Click on 'Signup / Login' button
    page.get_by_role("link", name="Signup / Login").click()
#5. Verify 'Login to your account' is visible
    expect(page.get_by_role("heading", level=2 , name="Login to your account")).to_be_visible()
#6. Enter correct email address and password
    page.locator('[data-qa="login-email"]').fill(user_email)
    page.locator('[data-qa="login-password"]').fill(user_password)
#7. Click 'login' button
    page.get_by_role("button", name="Login").click()
#8. Verify that 'Logged in as username' is visible
    expect(page.get_by_text("Logged in as")).to_be_visible()
#9. Click 'Delete Account' button
    page.get_by_role("link", name=" Delete Account").click()
#10. Verify that 'ACCOUNT DELETED!' is visible
    expect(page.get_by_text("Account Deleted!")).to_be_visible()