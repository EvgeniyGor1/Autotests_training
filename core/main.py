from selenium import webdriver
from selenium.webdriver.common.by import By


class Calculator:
    @staticmethod
    def sum(addend_1: int | float, addend_2: int | float) -> int | float:
        if not isinstance(addend_1, (int, float)) or not isinstance(addend_2, (int, float)):
            raise TypeError
        return addend_1 + addend_2

    @staticmethod
    def divide(numerator: int | float, denominator: int | float) -> int | float:
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise TypeError
        if denominator == 0:
            raise ZeroDivisionError
        return numerator / denominator

    @staticmethod
    def sum_all(*addend: tuple[int]) -> int:
        sum_ = 0
        for value in addend:
            if not isinstance(value, int):
                raise TypeError(f'Value - "{value}" is unavailable. Only type int is available')
            sum_ += value

        return sum_


class Parser:
    def __init__(self, options: webdriver.ChromeOptions | None):
        self.driver = webdriver.Chrome(options=options)

    def go_to(self, url: str):
        self.driver.get(url)
        assert 'Not Found' not in self.driver.title, 'Incorrect url'

    def press_email_field(self):
        temp_elem = self.driver.find_element(By.NAME)
        temp_elem.find_elements(By.CLASS_NAME, 'tab')[1].click()


def main_loop(url):
    options = webdriver.ChromeOptions()

    parser = Parser(options)
    parser.go_to(url)
    parser.press_email_field()
    ...


if __name__ == "__main__":
    TARGET_URL = 'https://www.qa-practice.com/elements/input/simple'
    main_loop(url=TARGET_URL)
