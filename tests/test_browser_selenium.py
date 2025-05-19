
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_google(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title


def test_input_field_present(browser):
    browser.get("https://www.google.com")
    input_box = browser.find_element(By.NAME, "q")
    assert input_box is not None


def test_footer_text(browser):
    browser.get("https://www.google.com")
    footer = browser.find_element(By.TAG_NAME, "footer")
    assert "About" in footer.text or "Privacy" in footer.text
