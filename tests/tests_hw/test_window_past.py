from pages.window_past import WindowPast
import time


def test_home_window(browser):
    home_window = WindowPast(browser)

    home_window.visit()

    assert home_window.btn_home.exist()
    assert home_window.check_name_home.get_text() == 'Home'
    assert home_window.check_href_home.get_dom_attribute('href') == 'https://demoqa.com'
    assert len(browser.window_handles) == 1
    home_window.btn_home.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2


