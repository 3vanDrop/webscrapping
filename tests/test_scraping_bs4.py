
import requests
from bs4 import BeautifulSoup


def test_parse_example_dot_com():
    response = requests.get("https://example.com")
    soup = BeautifulSoup(response.text, "html.parser")
    assert soup.title.string == "Example Domain"


def test_find_paragraph():
    response = requests.get("https://example.com")
    soup = BeautifulSoup(response.text, "html.parser")
    paragraph = soup.find("p")
    assert "illustrative examples" in paragraph.text


def test_link_exists():
    response = requests.get("https://example.com")
    soup = BeautifulSoup(response.text, "html.parser")
    link = soup.find("a")
    assert link is not None and "https://" in link.get("href", "")
