import selenium.common.exceptions
from conftest import *
from selenium.webdriver.common.by import By


@pytest.mark.checkbox
def test_single_checkbox(browser):
    browser.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = browser.find_element(By.ID, 'id_checkbox_0')
    checkbox.click()
    submit = browser.find_element(*SUBMIT)
    submit.click()
    assert 'select me or not' in browser.find_element(*RESULT).text


@pytest.mark.checkbox
def test_checkboxes_no_choices(browser):
    browser.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
    submit = browser.find_element(*SUBMIT)
    submit.click()
    try:
        browser.implicitly_wait(1)
        browser.find_element(*RESULT)
    except selenium.common.exceptions.NoSuchElementException:
        assert True
        return

    assert False


@pytest.mark.checkbox
def test_checkboxes_two_selected(browser):
    browser.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
    checkbox = browser.find_element(By.ID, 'id_checkboxes_0')
    checkbox.click()
    checkbox = browser.find_element(By.ID, 'id_checkboxes_2')
    checkbox.click()
    submit = browser.find_element(*SUBMIT)
    submit.click()
    assert 'one, three' in browser.find_element(*RESULT).text
