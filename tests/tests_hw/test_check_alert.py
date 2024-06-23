import time

from pages.alerts import Alerts

def test_check_alert(browser):
    check_alert = Alerts(browser)

    check_alert.visit()
    check_alert.timerButton.click()
    time.sleep(5)
    assert check_alert.alert()