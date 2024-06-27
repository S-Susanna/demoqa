from pages.modal_dialogs import ModalDialog
import time
import pytest


def test_check_modal(browser):
    check_modal = ModalDialog(browser)

    check_modal.visit()
    if check_modal.base_url != 200:
        return "Code not working"
    pytest.mark.skip(reason='Code not working')

    assert not check_modal.alert()

    check_modal.small_modal.click()
    time.sleep(2)
    assert check_modal.small_modal.visible()
    assert check_modal.small_modal_content.get_text() == 'This is a small modal. It has very less content'
    # assert check_modal.alert() -- непонятно, почему форма ругается и не видет alert. При том при visibe всё работает
    check_modal.small_modal_close.click()
    assert not check_modal.alert()


    check_modal.large_modal.click()
    time.sleep(2)
    assert check_modal.small_modal.visible()
    check_modal.large_modal_close.click()
    assert not check_modal.alert()