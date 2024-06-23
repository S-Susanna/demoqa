from pages.demoqa_webtables import WebTables
import time


def test_webtables(browser):
    page_webtables = WebTables(browser)

    page_webtables.visit()
    # page_webtables.head_check.click_force()
    #page_webtables.head_check.sorted()
    assert page_webtables.check_list.exist()
    assert page_webtables.check_list.get_text()

    if page_webtables.head_check.click():
        return page_webtables.check_list.sorted

