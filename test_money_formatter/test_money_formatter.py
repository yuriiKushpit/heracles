import pytest
from selenium import webdriver
import os

browser = webdriver.Chrome(executable_path=os.getcwd() + '/chromedriver')
BASE_URL = 'http://localhost:5000/'
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


@pytest.fixture(scope="function", autouse=True)
def run_around_tests():
    browser.get(BASE_URL)


@pytest.fixture(scope="module", autouse=True)
def run_around_file():
    yield
    browser.quit()


@pytest.mark.parametrize('entered_value, expected_value', positive_data)
def test_positive_scenarios(entered_value, expected_value):
    browser.find_element_by_id('data').send_keys(str(entered_value))
    browser.find_element_by_css_selector('input[type="submit"]').click()
    assert browser.find_element_by_id('result').text == expected_value


@pytest.mark.parametrize('entered_value', negative_data)
def test_negative_scenarios(entered_value):
    browser.find_element_by_id('data').send_keys(str(entered_value))
    browser.find_element_by_css_selector('input[type="submit"]').click()
    assert browser.find_element_by_id('error').text == INCORRECT_VALUE_ERROR
    assert browser.find_element_by_id('data').text == ''

