from playwright.sync_api import Page, expect 

def test_login_user_incorrect_email_password(page : Page, navigate_to_home):
#1. Launch browser
#2. Navigate to url 'http://automationexercise.com'
#3. Verify that home page is visible successfully
    expect(page).to_have_url("https://automationexercise.com/")
#4. Click on 'Signup / Login' button
    page.get_by_role("link", name="Signup / Login").click()
#5. Verify 'Login to your account' is visible
    expect(page.get_by_role("heading", level=2 , name="Login to your account")).to_be_visible()
#6. Enter incorrect email address and password
    page.locator('[data-qa="login-email"]').fill("carric@gmail.com")
    page.locator('[data-qa="login-password"]').fill("SenhaWrong")
#7. Click 'login' button
    page.get_by_role("button", name="Login").click()
#8. Verify error 'Your email or password  
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()