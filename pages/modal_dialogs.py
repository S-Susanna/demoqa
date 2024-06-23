from pages.base_page import BasePage
from components.components import WebElement

class ModalDialog(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.menu_list = WebElement(driver, '#item-2')
        self.icon_click = WebElement(driver, '#app > header > a > img')


        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.small_modal_close = WebElement(driver, '#closeSmallModal')
        self.large_modal_close = WebElement(driver, '#closeLargeModal')

        self.small_modal_content = WebElement(driver, 'body > div.fade.modal.show > div > div > div.modal-body')
        self.large_modal_content = WebElement(driver, 'body > div.fade.modal.show > div > div > div.modal - body > p')