from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Element:
    def __init__(self, browser):
        self._browser = browser

    @property
    def get_browser(self):
        return self._browser

    def send_keys(self, element, text_to_send):
        element.send_keys(text_to_send)

    def click_on_element(self, element):
        element.click()

    def get_text(self, element):
        return element.text

    def wait_by_condition(self, element, condition, strategy, time_for_wait=60):
        WebDriverWait(self.get_browser, time_for_wait).until(condition((strategy, element)))


class GeneralPage(Element):

    def __init__(self, browser):
        super().__init__(browser)

    @property
    def get_browser(self):
        return self._browser

    def get_enter_data_input(self):
        self.wait_by_condition('data', EC.element_to_be_clickable, By.ID)
        return self.get_browser.find_element_by_id('data')

    def get_submit_button(self):
        self.wait_by_condition('input[type="submit"]',
                               EC.element_to_be_clickable, By.CSS_SELECTOR)
        return self.get_browser.find_element_by_css_selector('input[type="submit"]')

    def get_result_input(self):
        self.wait_by_condition('result', EC.element_to_be_clickable, By.ID)
        return self.get_browser.find_element_by_id('result')

    def get_error_label(self):
        self.wait_by_condition('error', EC.element_to_be_clickable, By.ID)
        return self.get_browser.find_element_by_id('error')
