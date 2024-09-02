import pytest
import selenium.webdriver.chrome.webdriver
from selenium.webdriver.common.by import By


def get_homepage_buttons(browser: selenium.webdriver.Chrome):
    browser.get('https://www.qa-practice.com/')
    return browser.find_element(By.CLASS_NAME, 'rectangle').find_elements(By.TAG_NAME, 'li')


@pytest.mark.smoke
def test_homepage(browser):
    browser.get('https://www.qa-practice.com/')
    assert 'QA Practice' in browser.title


@pytest.mark.smoke
class TestHomepageButtons:
    @staticmethod
    def test_text_input(browser):
        buttons = get_homepage_buttons(browser)
        first_button = buttons[0]
        first_button.click()
        assert 'Input field' or 'Input Field' in browser.title

    @staticmethod
    def test_simple_button(browser):
        buttons = get_homepage_buttons(browser)
        second_button = buttons[1]
        second_button.click()
        assert 'Buttons' in browser.title

    @staticmethod
    def test_single_checkbox(browser):
        buttons = get_homepage_buttons(browser)
        third_button = buttons[2]
        third_button.click()
        assert 'Checkboxes' in browser.title

    @staticmethod
    def test_text_area(browser):
        buttons = get_homepage_buttons(browser)
        fourth_button = buttons[3]
        fourth_button.click()
        assert 'TextArea' in browser.title

    @staticmethod
    def test_select_input(browser):
        buttons = get_homepage_buttons(browser)
        fifth_button = buttons[4]
        fifth_button.click()
        assert 'Select Input' in browser.title

