from pages.demoqa_webtables import WebTables
import time


def test_webtables(browser):
    page_webtables = WebTables(browser)

    page_webtables.visit()
    page_webtables.head_check.click()
    time.sleep(5)

    assert page_webtables.check_sort.exist()
    assert page_webtables.check_sort.get_text()

    if page_webtables.head_check.click():
        print(page_webtables.check_sort.sort(reverse=True))


