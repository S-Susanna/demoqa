from selenium.common.exceptions import NoSuchFrameException
from pages.base_page import BasePage
from components.components import WebElement

class DemoQa(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement (driver, locator='#app > header > a')
        # self.get_text = WebElement(driver, text='[© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.]')
        self.btn_elements = WebElement (driver, locator='#app > div > div > div.home-body > div > div:nth-child(1)')
        self.get_text = WebElement(driver, text='Please select an item from left to start practice.')

    def exist_icon(self):
        try:
            self.icon.find_element()
        except NoSuchFrameException:
            return False
        return True


