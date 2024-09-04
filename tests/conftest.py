from selenium import webdriver
import pytest

DEBUG_MODE = 0


@pytest.fixture(scope='module')
def browser():
    options = webdriver.ChromeOptions()
    if not DEBUG_MODE:
        options.add_argument('--headless')
    else:
        options.add_argument('--disable-search-engine-choice-screen')

    with webdriver.Chrome(options=options) as browser:
        browser.implicitly_wait(5)
        yield browser
