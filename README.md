# Webscrapping (Selenium, Playwright, BeautifulSoup) - Testing Suite with Pytest

This repository contains example tests using:
- Playwright (browser automation)
- Selenium (browser automation)
- BeautifulSoup (HTML parsing)
- Requests (for API testing, like Postman)

## Structure

- `tests/`: All test files
- `src/`: (Empty) for your application code
- `conftest.py`: Shared pytest fixtures
- `pytest.ini`: Pytest configuration
- `requirements.txt`: Project dependencies

## Installation

pip install -r requirements.txt
playwright install

## Running Tests

pytest

To run a specific test module:

pytest tests/test_browser_playwright.py

## Notes

- ChromeDriver is required for Selenium.
- Playwright requires one-time installation (`playwright install`).
