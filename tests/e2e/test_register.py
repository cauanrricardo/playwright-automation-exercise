from playwright.sync_api import Page, expect 

def test_register_user_sucefully(page: Page, navigate_to_home):
# Navigate to url 'http://automationexercise.com'
# Verify that home page is visible successfully
    print(page.url)
    expect(page).to_have_url("https://automationexercise.com/")

# Click on 'Signup / Login' button
    page.get_by_role("link", name="login").click()
    expect(page).to_have_url("https://automationexercise.com/login")
    print(page.url)

# Verify 'New User Signup!' is visible
    expect(page.get_by_role("heading", level=2 , name="New User Signup!"))
# Enter name and email address
    page.get_by_placeholder("Name").fill("Cauan Ricardo")
    page.locator('[data-qa="signup-email"]').fill("cauanrricardo@gmail.com")
  
# Click 'Signup' button
    page.get_by_role("button", name="Signup").click()
# Verify that 'ENTER ACCOUNT INFORMATION' is visible
    page.get_by_text("Enter Account Information").is_visible
# Fill details: Title, Name, Email, Password, Date of birth
    page.locator('[data-qa="password"]').fill("224508rS.")
    page.locator('[data-qa="days"]').select_option("21")
    page.locator('[data-qa="months"]').select_option("June")
    page.locator('[data-qa="years"]').select_option("2005")

# Select checkbox 'Sign up for our newsletter!'
    page.get_by_label("Sign up for our newsletter!").check()
# Select checkbox 'Receive special offers from our partners!'
    page.get_by_label("Receive special offers from our partners!").check()
# Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    page.locator('[data-qa="first_name"]').fill("Cauan Ricardo")
    page.locator('[data-qa="last_name"]').fill("Ribeiro")
    page.locator('[data-qa="company"]').fill("UFC")
    page.locator('[data-qa="address"]') .fill("Rua autran moreno 127, centro - Quixadá")
    page.locator('[data-qa="address2"]').fill("Rua Stella Hanriot 127, buritis - Belo Horioznte")
    page.get_by_label("country").select_option("Canada")
    page.locator('[data-qa="state"]').fill("Ceara")
    page.locator('[data-qa="city"]').fill("Belo Horizonte")
    page.locator('[data-qa="zipcode"]').fill("63900-105")
    page.locator('[data-qa="mobile_number"]').fill("31997814542")
# Click 'Create Account button'
    page.get_by_role("button", name="Create Account").click()
# Verify that 'ACCOUNT CREATED!' is visible
    expect(page.get_by_text("Account Created!")).to_be_visible()
    expect(page).to_have_url("https://automationexercise.com/account_created")
# Click 'Continue' button
    page.locator('[data-qa="continue-button"]').click()
# Verify that 'Logged in as username' is visible
    expect(page.get_by_text("Logged in as")).to_be_visible()
# Click 'Delete Account' button
    page.get_by_role("link", name=" Delete Account").click()
# Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    expect(page.get_by_text("Account Deleted!")).to_be_visible()
    