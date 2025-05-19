
import pytest
from playwright.sync_api import sync_playwright


def test_title_contains_google():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "Google" in page.title()
        browser.close()


def test_search_input_exists():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert page.query_selector("input[name='q']") is not None
        browser.close()


def test_privacy_link_text():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.google.com")
        link = page.query_selector("a[href*='privacy']")
        assert link is not None and "Privacy" in link.inner_text()
        browser.close()
