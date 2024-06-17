from pages.modal_dialogs import ModalDialog
import time

def test_modal_elements(browser):
    modal_elements = ModalDialog(browser)
    modal_elements.visit()

    assert modal_elements.menu_list.check_count_elements(count=5)


def test_navigation_modal(browser):
    modal_elements = ModalDialog(browser)
    modal_elements.visit()

    modal_elements.refresh()
    time.sleep(2)
    modal_elements.icon_click.click()
    time.sleep(2)
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    browser.back()
    assert modal_elements.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
