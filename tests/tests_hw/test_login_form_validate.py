from pages.form_page import FormPage
import time

def test_login_form_validate (browser):
    test_login_form_validate = FormPage(browser)

    test_login_form_validate.visit()

    assert test_login_form_validate. first_name.get_dom_attribute('placeholder') == 'First Name'
    assert test_login_form_validate.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert test_login_form_validate.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert test_login_form_validate.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    test_login_form_validate.btn_submit.click_force()
    test_login_form_validate.was_validated.exist()

