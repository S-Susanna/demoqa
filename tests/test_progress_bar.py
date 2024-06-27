from pages.progress_bar import ProgressBar
import time


def test_progress_bar(browser):
    progress_bar = ProgressBar(browser)

    progress_bar.visit()
    # time.sleep(2)
    progress_bar.start_bar.click()
    time.sleep(2)
    # if progress_bar.bar == '51%': #тоже прошел проверку и, возможно, можно использовать
    #     progress_bar.stop_bar.click()

    while True:
        if progress_bar.bar.get_dom_attribute('aria-valuenow') == '51%':
            progress_bar.start_bar.click()
        break










    # start = time.time()
    # print(stop_bar.alert())
    # time.sleep(5)
    # end = time.time()
    # execution_time = end - start
    # print(f'execution_time: {execution_time}s')

