from components.components import WebElement
from pages.base_page import BasePage

class WindowPast(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/links'
        super().__init__(driver, self.base_url)


        self.btn_home = WebElement(driver, '#simpleLink')
        self.check_name_home = WebElement(driver, '#simpleLink')
        self.check_href_home = WebElement(driver, '#simpleLink')
        self.new_tub = WebElement(driver, '#simpleLink')



