from pages.demoqa import DemoQa
import time
import pytest


# @pytest.mark.skip()
def test_decor(browser):
    decor = DemoQa(browser)
    decor.visit()
    decor.element.check_count_elements(6)

    for element in decor.element.find_elements():
        assert element.text != " "

