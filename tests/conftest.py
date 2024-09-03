import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

DEBUG_MODE = 0


@pytest.fixture(scope='module')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-search-engine-choice-screen')
    if not DEBUG_MODE:
        options.add_argument('--headless')

    with webdriver.Chrome(options=options) as browser:
        browser.implicitly_wait(3)
        yield browser

