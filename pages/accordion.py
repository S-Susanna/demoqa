from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#item-0 > span')
        self.Lorem_Ipsum_text = WebElement(driver, '#section1Content > p')
        self.icon_check = WebElement(driver, '#section1Heading')
        self.section_text1_check = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section_text2_check = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section_text3_check = WebElement(driver, '#section3Content > p')
