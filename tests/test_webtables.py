from pages.demoqa_webtables import WebTables
import time


def test_webtables(browser):
    #проверка блока, что нет в таблице No rows found
    page_webtables = WebTables(browser)

    page_webtables.visit()
    assert not page_webtables.no_data.exist()

# удаляем все записи
    while page_webtables.btn_delete_row.exist():
        page_webtables.btn_delete_row.click()
    assert not page_webtables.btn_delete_row.exist()

    time.sleep(5)
    assert page_webtables.no_data.exist()



def test_webtable(browser):
    page_webtable = WebTables(browser)
    page_webtable.visit()

    page_webtable.btn_add.click()

    assert page_webtable.user_form.exist()
    time.sleep(2)
    page_webtable.first_name.send_keys('Anton')
    page_webtable.last_name.send_keys('Foidl')
    page_webtable.user_email.send_keys('test@tt.tt')
    page_webtable.age.send_keys('25')
    page_webtable.salary.send_keys('200000')
    page_webtable.department.send_keys('IT')
    page_webtable.submit.click()
    time.sleep(2)
    assert page_webtable.rt_table_group.exist()
    time.sleep(2)
    assert page_webtable.first_name_table.get_text() == 'Anton'
    # assert not page_webtable.user_form.visible()


    page_webtable.edit.click()
    assert page_webtable.user_form.get_text()
    time.sleep(2)
    # assert page_webtable.first_name_input.get_text() == 'Anton'
    page_webtable.first_name.click()
    page_webtable.first_name_delete.clear()


    page_webtable.first_name.send_keys('SSS')
    page_webtable.submit.click()
    time.sleep(2)
    assert page_webtable.first_name_table.get_text() == 'SSS'
    #
    page_webtable.btn_delete_row_4.click()
    assert not page_webtable.btn_delete_row_4.exist()




def test_webtable_2(browser):
    page_webtable_2 = WebTables(browser)
    page_webtable_2.visit()
    assert not page_webtable_2.desabled_btn_next.click_force()
    assert not page_webtable_2.desabled_btn_previous.click_force()
    assert not page_webtable_2.alert()

    page_webtable_2.btn_add.click()

    name = ['a'], ['h']
    lastname= ['p']
    email = 'sherlok-sherlok@list.ru'
    age = 30
    salary = 50
    department = 'IT'

    page_webtable_2.rt_tr_group = 3
    while page_webtable_2.rt_tr_group < 11:
        page_webtable_2.rt_tr_group = page_webtable_2.rt_tr_group+1
        time.sleep(2)

        for name in name:
            page_webtable_2.first_name.send_keys(name)

        for name in lastname:
            page_webtable_2.last_name.send_keys(lastname)

        for num in range(age):
            page_webtable_2.age.send_keys(age)

        page_webtable_2.first_name.send_keys(name)
        page_webtable_2.last_name.send_keys(lastname)
        page_webtable_2.user_email.send_keys(email)
        page_webtable_2.age.send_keys(age)
        page_webtable_2.salary.send_keys(salary)
        page_webtable_2.department.send_keys(department)
        page_webtable_2.submit.click_force()
        time.sleep(2)
        assert page_webtable_2.rt_table_group.exist()
        time.sleep(2)
        assert page_webtable_2.first_name_table.get_text()

        page_webtable_2.btn_add.click_force()


    time.sleep(3)
    page_webtable_2.desabled_btn_next.exist()
    page_webtable_2.desabled_btn_next.click_force()


    if page_webtable_2.desabled_btn_next:
        return page_webtable_2.page_2.visible()

    page_webtable_2.desabled_btn_previous.exist()
    page_webtable_2.desabled_btn_previous.click_force()

    if page_webtable_2.desabled_btn_previous:
        return page_webtable_2.page_1.visible()
