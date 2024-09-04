import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.buttons
def test_buttons(browser):
    browser.get('https://www.qa-practice.com/')
    buttons = browser.find_element(By.CLASS_NAME, 'rectangle')
    buttons.find_elements(By.TAG_NAME, 'li')[1].click()
    assert 'button' in browser.current_url


@pytest.mark.buttons
def test_simple_button(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    click_button = browser.find_element(By.ID, 'submit-id-submit')
    click_button.click()
    assert 'Submitted' in browser.find_element(By.ID, 'result-text').text


@pytest.mark.buttons
def test_looks_like_a_button(browser):
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    # all_inner_buttons = browser.find_element(By.CLASS_NAME, 'tabs').find_elements(By.TAG_NAME, 'li')
    # looks_like_a_button = all_inner_buttons[1]
    # looks_like_a_button.click()
    browser.find_element(By.CLASS_NAME, 'a-button').click()
    assert 'Submitted' in browser.find_element(By.ID, 'result-text').text


@pytest.mark.buttons
def test_disabled_button(browser):
    browser.get('https://www.qa-practice.com/elements/button/disabled')
    # all_inner_buttons = browser.find_element(By.CLASS_NAME, 'tabs').find_elements(By.TAG_NAME, 'li')
    # disabled_button = all_inner_buttons[2]
    # disabled_button.click()
    state = Select(browser.find_element(By.ID, 'id_select_state'))
    state.select_by_value('enabled')
    browser.find_element(By.ID, 'submit-id-submit').click()
    assert 'Submitted' in browser.find_element(By.ID, 'result-text').text
