from pages.demoqa import DemoQa  # наследование класса DemoQa для доступа к сайту https://demoqa.com/
from pages.elements_page import ElementsPage  # наследование класса ElementsPage для доступа к сайту 'https://demoqa.com/elements'

def test_check_text(browser): # получение доступа к браузеру
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()  # посетить страницу
    assert demo_qa_page.equal_url()  # проверка на возможность успешно попасть на страницу
    # assert demo_qa_page.get_text.text()  # проверить на наличие текста на странице в подвале
    demo_qa_page.btn_elements.click()  # кликнуть на окно 'Elements'
    assert elements_page.equal_url()  # проверка наличия страницы после клика
    assert demo_qa_page.get_text.text()  # проверить на наличие текста на странице
