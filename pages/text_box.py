from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.borden = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div:nth-child(4)')
        self.name_borden = WebElement(driver, '#name')
        self.current_address_borden = WebElement(driver, 'p#currentAddress')