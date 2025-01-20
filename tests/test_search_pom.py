import pytest
from tests.pages.search_page import SearchPage


@pytest.mark.search
def test_search_functionality(chrome_browser):
    """
    Test the search functionality of the DuckDuckGo website
    """
    url = "https://duckduckgo.com/"
    search_term = "Pytest with Eric"
    search_page = SearchPage(chrome_browser)

    # Open Page
    search_page.open_page(url)

    # Search for the term
    search_page.search(search_term)

    # Assert that the title contains the search term.
    assert search_term in chrome_browser.title
