import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def navigate_to_home(page: Page):
    page.goto("https://automationexercise.com/")
    yield