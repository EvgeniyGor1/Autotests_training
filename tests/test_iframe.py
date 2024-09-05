import selenium.webdriver.chrome.webdriver
from selenium.webdriver.common.by import By


def test_iframe(browser):
    def first_assert(frame: selenium.webdriver.chrome.webdriver.WebDriver):
        button_main_call = frame.find_element(By.CSS_SELECTOR, '.btn.btn-primary.my-2')
        assert 'Main call to action' in button_main_call.text

    def second_assert(frame: selenium.webdriver.chrome.webdriver.WebDriver):
        button_second_action = frame.find_element(By.CSS_SELECTOR, '.btn.btn-secondary.my-2')
        assert 'Secondary action' in button_second_action.text

    def third_assert(frame: selenium.webdriver.chrome.webdriver.WebDriver):
        link_home = frame.find_element(By.CLASS_NAME, 'mb-0')
        link_home = link_home.find_element(By.TAG_NAME, 'a').get_attribute('href')
        frame.get(link_home)
        assert 'QA Practice' in browser.title

    browser.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(iframe)
    first_assert(browser)
    second_assert(browser)
    third_assert(browser)
