from pages.base_page import BasePage
from components.components import WebElement

class ModalDialog(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.menu_list = WebElement(driver, '#item-2')
        self.icon_click = WebElement(driver, '#app > header > a > img')
