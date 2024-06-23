from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, 'delete')

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.user_form = WebElement(driver, 'body > div.fade.modal.show > div > div')

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.submit = WebElement(driver, '#submit')
        self.rt_table_group = WebElement(driver, 'div.rt-table>div.rt-tbody')

    # def dialog(self, first_name,last_name, user_email, age, salary, department):
    #     if first_name or last_name or user_email or age or salary or department-> str or None:
    #         return ("fill in all the fields")
    #     return False     #get_dom_attribute ('placeholder') == 'Full Name'

        self.edit = WebElement(driver, '#edit-record-4 > svg')
        self.first_name_table= WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.first_name_delete = WebElement(driver, '#firstName')
        self.first_name_input = WebElement(driver, 'input#firstName')
        self.btn_delete_row_4 = WebElement(driver, '#delete-record-4 > svg > path')

#к задаче 2 занятие 11
        self.desabled_btn_next = WebElement(driver, 'div.-next > button')
        self.desabled_btn_previous = WebElement(driver, ' div.-previous > button')
        self.str_rowgroup = WebElement(driver, 'rowgroup')
        self.rt_tr_group = WebElement(driver, 'rt-tr-group')
        self.page_2 = WebElement(driver, 'input[type=number]')
        self.page_1 = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[1]/div/input')



#к задаче 3 занятие 12
        self.head_check = WebElement(driver, 'rt-tr')
        self.find_elements_by_class_name = WebElement(driver,"event-date-time__time")
        self.check_list = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody')
