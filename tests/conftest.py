import pytest
from playwright.sync_api import Page
from dotenv import load_dotenv
import os

load_dotenv()  

EMAIL = os.getenv("USER_EMAIL")
PASSWORD = os.getenv("USER_PASSWORD")

@pytest.fixture(scope="session")
def user_password():
    return PASSWORD

@pytest.fixture(scope="function")
def user_email():
    return EMAIL

@pytest.fixture(scope="function")
def navigate_to_home(page: Page):
    page.goto("https://automationexercise.com/")
    yield

@pytest.fixture(scope="function")
def reg_user(page:Page):
    page.goto("https://automationexercise.com/")
    yield