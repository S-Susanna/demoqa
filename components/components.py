from selenium.webdriver.common.by import By
class WebElement:

    def __init__(self, driver, locator='', text=''):
        self.driver = driver
        self.locator = locator
        self.text = text


    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)


    def get_text(self):
        return str(self.find_element().text)


