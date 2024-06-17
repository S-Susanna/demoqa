from pages.text_box import TextBox
import time

def test_text_box_pg (browser):
    text_box_pg = TextBox(browser)

    text_box_pg.visit()
    text_box_pg.name.click()
    text_box_pg.name.send_keys('Susanna')
    text_box_pg.current_address.send_keys('Nikolskoye')
    time.sleep(2)
    text_box_pg.btn_submit.click()
    time.sleep(2)
    text_box_pg.name_borden.exist()
    assert text_box_pg.name_borden.get_text() == 'Name:Susanna'
    text_box_pg.current_address_borden.exist()
    assert text_box_pg.current_address_borden.get_text() == 'Current Address :Nikolskoye'
