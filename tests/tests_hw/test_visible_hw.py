from pages.accordion import Accordion #наследование класса Accordion для доступа к сайту https://demoqa.com/accordian
import time # для использования времени при тестировании

def test_accordion(browser):# получение доступа к браузеру
    accordion_page = Accordion(browser) #перейти на страницу https://demoqa.com/accordian
    accordion_page.visit()# посетить страницу

    assert accordion_page.Lorem_Ipsum_text.visible() # проверка на видимость текста

def test_accordion_click(browser):
    accordion_page = Accordion(browser)  # перейти на страницу https://demoqa.com/accordian
    accordion_page.visit()  # посетить страницу
    accordion_page.icon_check.click()#проверка на кликабельность элемента
    time.sleep(3)# задержка времени для проверки
    assert accordion_page.icon_check.visible()#проверка видимости элемента
    assert not accordion_page.Lorem_Ipsum_text.visible()#проверка на невидимость текста


def test_visible_accordion_default(browser):

    accordion_page = Accordion(browser)
    accordion_page.visit()
    # assert accordion_page.section_text1_check.visible()
    assert not accordion_page.section_text1_check.visible()
    # assert accordion_page.section_text2_check.visible()
    assert not accordion_page.section_text2_check.visible()
    # assert accordion_page.section_text3_check.visible()
    assert not accordion_page.section_text3_check.visible()