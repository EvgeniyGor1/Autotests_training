from selenium.webdriver.support.ui import Select
from conftest import *


def test_single_select(browser):
    browser.get('https://www.qa-practice.com/elements/select/single_select')
    slct = Select(browser.find_element(By.ID, 'id_choose_language'))
    slct.select_by_value('1')
    browser.find_element(*SUBMIT).click()
    assert 'Python' in browser.find_element(*RESULT).text


def test_multiple_selects(browser):
    browser.get('https://www.qa-practice.com/elements/select/mult_select')
    slct = Select(browser.find_element(By.ID, 'id_choose_the_place_you_want_to_go'))
    slct.select_by_value('1')
    slct = Select(browser.find_element(By.ID, 'id_choose_how_you_want_to_get_there'))
    slct.select_by_value('2')
    slct = Select(browser.find_element(By.ID, 'id_choose_when_you_want_to_go'))
    slct.select_by_value('3')
    browser.find_element(*SUBMIT).click()
    assert 'to go by bus to the sea next week' in browser.find_element(*RESULT).text
