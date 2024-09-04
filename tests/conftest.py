from selenium import webdriver
import pytest

DEBUG_MODE = 0


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
