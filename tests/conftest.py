import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

DEBUG_MODE = 0

SUBMIT = (By.ID, 'submit-id-submit')
RESULT = (By.ID, 'result-text')


@pytest.fixture(scope='module')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-search-engine-choice-screen')
    options.add_argument('--window-size=1920,1080')
    if not DEBUG_MODE:
        options.add_argument('--headless')

    with webdriver.Chrome(options=options) as browser:
        browser.implicitly_wait(5)
        yield browser
