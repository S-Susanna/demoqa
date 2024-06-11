from pages.accordion import Accordion
import time

def test_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    assert accordion_page.Lorem_Ipsum_text.visible()

    accordion_page.icon_check.click()
    time.sleep(2)
    assert accordion_page.icon_check.visible()
    # assert not accordion_page.icon_check.visible()


def test_visible_accordion_default(browser):

    accordion_page = Accordion(browser)
    accordion_page.visit()
    # assert accordion_page.section_text1_check.visible()
    assert not accordion_page.section_text1_check.visible()
    # assert accordion_page.section_text2_check.visible()
    assert not accordion_page.section_text2_check.visible()
    # assert accordion_page.section_text3_check.visible()
    assert not accordion_page.section_text3_check.visible()