import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

DEBUG_MODE = 0


@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    if not DEBUG_MODE:
        options.add_argument('--headless')
        options.add_argument('--log-level=3')
    else:
        options.add_argument('--disable-search-engine-choice-screen')

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.close()
