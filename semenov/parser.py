import pytest
from pages.base_page import BasePage


@pytest.mark.parser_item
class TestParserItem():

    def test_parser_item(self, browser):
        link = "https://market.yandex.ru/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_search_link()
        page.go_to_tele_link()

