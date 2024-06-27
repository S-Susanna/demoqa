import time


from pages.alerts import Alerts

def test_check_alert(browser):
    check_alert = Alerts(browser)
    check_alert.visit()
    check_alert.timerButton.click()

    start = time.time()
    print(check_alert.alert())
    time.sleep(5)
    end = time.time()
    execution_time = end - start
    print(f'execution_time: {execution_time}s')

    assert check_alert.alert()


