import pytest
from selenium import webdriver
import os

from selenium.webdriver.chrome.options import Options

from heracles.pages.general_page import GeneralPage

# chromedriver should be in root directory of repository
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(executable_path=os.getcwd() + '/chromedriver', chrome_options=chrome_options)
INCORRECT_VALUE_ERROR = 'Please enter any number in next format (1234.1234)'

positive_data = [
    (5, '5.00'),
    (-1000000000, '-1 000 000 000.00'),
    (0, '0.00'),
    (0.456, '0.46'),
    (68738711241412.17481371891377561374613756138956135681, '68 738 711 241 412.17'),
    (100000000000000000, '100 000 000 000 000 000.00')
]

negative_data = [
    (''),
    ('    '),
    ('dfafadadf'),
    ('*&!$^%!#&)_+?'),
    ('汉字')
]


# Open base page before each test
@pytest.fixture(scope="function", autouse=True)
def run_around_tests(environment):
    browser.get(environment)


# Close driver after all test suite
@pytest.fixture(scope="module", autouse=True)
def run_around_file():
    yield
    browser.quit()


# Positive tests
@pytest.mark.parametrize('entered_value, expected_value', positive_data)
def test_positive_scenarios(entered_value, expected_value):
    page = GeneralPage(browser)
    page.send_keys(page.get_enter_data_input(), str(entered_value))
    page.click_on_element(page.get_submit_button())
    assert page.get_text(page.get_result_input()) == expected_value


# Negative tests
@pytest.mark.parametrize('entered_value', negative_data)
def test_negative_scenarios(entered_value):
    page = GeneralPage(browser)
    page.send_keys(page.get_enter_data_input(), str(entered_value))
    page.click_on_element(page.get_submit_button())
    assert page.get_text(page.get_error_label()) == INCORRECT_VALUE_ERROR
