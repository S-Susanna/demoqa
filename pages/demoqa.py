from selenium.common.exceptions import NoSuchFrameException
from pages.base_page import BasePage
from components.components import WebElement

class DemoQa(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement (driver, '#app > header > a')
        self.elem1 = WebElement(driver, '#app > footer > span')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.elem2 = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')
        self.element = WebElement(driver, ' div.card-body')






